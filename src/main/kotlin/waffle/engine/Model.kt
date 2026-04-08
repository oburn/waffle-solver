package waffle.engine

import waffle.engine.CellState.ALONG
import waffle.engine.CellState.EXACT
import waffle.engine.CellState.MISS
import waffle.engine.Direction.HORIZONTAL
import waffle.engine.Direction.VERTICAL
import waffle.engine.Fact.CANNOT_BE
import waffle.engine.Fact.MAY_BE
import waffle.engine.Fact.MUST_BE

enum class CellState {
    EXACT, ALONG, MISS;

    fun rotate(): CellState {
        return when (this) {
            EXACT -> ALONG
            ALONG -> MISS
            MISS -> EXACT
        }
    }
}

data class Point(val x: Int, val y: Int)
data class Cell(val point: Point, val letter: Char, val state: CellState)

// Have optional to support the empty cells
typealias Row = List<Cell>

enum class Direction { HORIZONTAL, VERTICAL }

data class Word(val direction: Direction, val cells: List<Cell>)

data class WordStart(val point: Point, val direction: Direction)

enum class Fact {
    MUST_BE, CANNOT_BE, MAY_BE
}

data class CellFact(val point: Point, val fact: Fact, val letter: Char)

data class WordCandidates(val start: WordStart, val candidates: List<String>)
data class Solution(val candidates: List<WordCandidates>, val singleLetters: List<Cell>)

fun Int.isEven() = this % 2 == 0

data class WaffleState(val rows: List<Row>) {
    fun asString(): String {
        return rows.joinToString("\n") { r ->
            r.map { it.letter }.joinToString("")
        }
    }

    fun cellsInline(with: Point): Set<Cell> {
        val allowedValues = setOf(0, 2, 4)
        return rows.flatten()
            .filter { it.point != with }
            .filter {
                (with.x in allowedValues && with.x == it.point.x)
                        || (with.y in allowedValues && with.y == it.point.y)
            }.toSet()
    }

    fun cellAt(point: Point): Cell =
        if (point.y.isEven()) rows[point.y][point.x] else rows[point.y][point.x / 2]

    fun basicFactsAt(point: Point): Set<CellFact> {
        val cell = cellAt(point)
        val result = mutableSetOf<CellFact>()

        when (cell.state) {
            EXACT -> {
                result.add(CellFact(cell.point, MUST_BE, cell.letter))
            }

            ALONG -> {
                result.add(CellFact(cell.point, CANNOT_BE, cell.letter))
                cellsInline(point)
                    .filterNot { it.state == EXACT }
                    .filterNot { it.letter == cell.letter }
                    .map { CellFact(it.point, MAY_BE, cell.letter) }
                    .toCollection(result)
            }

            MISS -> {
                result.add(CellFact(cell.point, CANNOT_BE, cell.letter))
                val cannotBeCells = cellsInline(point)
                    .filterNot { it.state == EXACT }
                    .filterNot { it.letter == cell.letter }
                cannotBeCells.map { CellFact(it.point, CANNOT_BE, cell.letter) }.toCollection(result)
                nonExactCells()
                    .asSequence()
                    .filter { !cannotBeCells.contains(it) }
                    .filter { it.point != point }
                    .filterNot { it.letter == cell.letter }
                    .map { CellFact(it.point, MAY_BE, cell.letter) }
                    .toCollection(result)
            }
        }
        return result.toSet()
    }

    fun impliedFacts(): Set<CellFact> {
        val result = mutableSetOf<CellFact>()

        // Look for where there are 2 or more cells containing the same letter and are ALONG
        // Look for whether there is an intersection on adjacent lines, because if there is
        // then other non-adjacent cells could have the letter

        val letterToCells = nonExactCells()
            .filter { it.state == ALONG }
            .groupBy { it.letter }
        letterToCells.entries.filter { it.value.size > 1 }.forEach { entry ->
            val allCellsInline = entry.value.flatMap { cellsInline(it.point) }
            val dedupedCellsInline = allCellsInline.toSet()
            if (allCellsInline.size != dedupedCellsInline.size) {
                val candidates = nonExactCells() - dedupedCellsInline - entry.value.toSet()
                candidates.map { CellFact(it.point, letter = entry.key, fact = MAY_BE)}.toCollection(result)
            }
        }

        return result.toSet()
    }

    fun allFacts(): Set<CellFact> {
        val allBasicFacts = rows.flatten()
            .flatMap { basicFactsAt(it.point) }
            .toSet()
        return impliedFacts() + allBasicFacts
    }

    fun wordRegex(word: Word): String {
        var result = "^"
        val allCellFacts = allFacts()
        word.cells.forEach { cell ->
            val cellFacts = allCellFacts.filter { it.point == cell.point }
            val mustBeChars = cellFacts.filter { it.fact == MUST_BE }
                .map { it.letter }
                .toSet()
            if (mustBeChars.isNotEmpty()) {
                result += mustBeChars.first()
            } else {
                val mayBeChars = cellFacts.filter { it.fact == MAY_BE }
                    .map { it.letter }
                    .toSet()
                val cannotBeChars = cellFacts.filter { it.fact == CANNOT_BE }
                    .map { it.letter }
                    .toSet()
                val refinedMayBeChars = mayBeChars - cannotBeChars
                result += "[${refinedMayBeChars.sorted().joinToString(separator = "")}]"
            }
        }
        result += "$"
        return result
    }

    fun solve(): Solution {
        val candidates = words()
            .map { WordCandidates(WordStart(it.cells.first().point, it.direction), Matcher.search(wordRegex(it))) }
            .toList()
        val singleLetters = nonExactCells()
            .groupBy { it.letter }
            .entries
            .filter { it.value.size == 1 }
            .sortedBy { it.key }
            .flatMap { it.value }
        return Solution(candidates = candidates, singleLetters = singleLetters)
    }

    fun nonExactCells(): Set<Cell> =
        rows.flatten()
            .filter { it.state != EXACT }
            .toSet()

    fun verticalCells(x: Int): List<Cell> =
        rows.mapIndexed { y, cells ->
            if (y.isEven()) cells[x] else cells[x / 2]
        }

    fun words(): List<Word> {
        return listOf(
            Word(direction = HORIZONTAL, cells = rows[0]),
            Word(direction = HORIZONTAL, cells = rows[2]),
            Word(direction = HORIZONTAL, cells = rows[4]),
            Word(direction = VERTICAL, cells = verticalCells(0)),
            Word(direction = VERTICAL, cells = verticalCells(2)),
            Word(direction = VERTICAL, cells = verticalCells(4)),
        )
    }

    fun rotateState(row: Int, col: Int): WaffleState {
        val newRows = mutableListOf<Row>()

        rows.forEachIndexed { index, oldRow ->
            if (index != row) {
                newRows.add(oldRow)
            } else {
                val oldCell = oldRow[col]
                val newCell = oldCell.copy(state = oldCell.state.rotate())
                val newRow = oldRow.take(col) + newCell + oldRow.drop(col + 1)
                newRows.add(newRow)
            }
        }

        return WaffleState(newRows)
    }
}

fun buildState(from: String, retainingFrom: WaffleState? = null): WaffleState {
    val lines = from.lines().take(5)
    require(lines.size == 5) { "Input must have at least 5 lines" }

    val rows = lines.mapIndexed { y, line ->
        val trimmed = line.trim()

        // Ensure row lengths are correct (5 for even, 3 for odd)
        require(trimmed.length == if (y.isEven()) 5 else 3) { "Not correct chars on line $y" }

        trimmed.mapIndexed { charIndex, char ->
            // Even rows use x = 0,1,2,3,4 | Odd rows use x = 0,2,4
            val x = if (y.isEven()) charIndex else charIndex * 2
            val point = Point(x, y)
            Cell(
                point = point,
                letter = char,
                state = retainingFrom?.cellAt(point)?.state ?: MISS,
            )
        }
    }

    return WaffleState(rows)
}
