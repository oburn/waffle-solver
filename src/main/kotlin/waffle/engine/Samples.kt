package waffle.engine

import waffle.engine.CellState.ALONG
import waffle.engine.CellState.EXACT
import waffle.engine.CellState.MISS

object Samples {
    val SAMPLE1 = WaffleState(
        listOf(
            listOf(
                Cell(point = Point(0, 0), letter = 'c', state = EXACT),
                Cell(point = Point(1, 0), letter = 'r', state = EXACT),
                Cell(point = Point(2, 0), letter = 'm', state = MISS),
                Cell(point = Point(3, 0), letter = 'v', state = MISS),
                Cell(point = Point(4, 0), letter = 'p', state = EXACT),
            ),
            listOf(
                Cell(point = Point(0, 1), letter = 'e', state = MISS),
                Cell(point = Point(2, 1), letter = 'r', state = MISS),
                Cell(point = Point(4, 1), letter = 'g', state = ALONG),
            ),
            listOf(
                Cell(point = Point(0, 2), letter = 'l', state = ALONG),
                Cell(point = Point(1, 2), letter = 'a', state = MISS),
                Cell(point = Point(2, 2), letter = 'i', state = EXACT),
                Cell(point = Point(3, 2), letter = 'v', state = MISS),
                Cell(point = Point(4, 2), letter = 'y', state = ALONG),
            ),
            listOf(
                Cell(point = Point(0, 3), letter = 'e', state = MISS),
                Cell(point = Point(2, 3), letter = 'n', state = MISS),
                Cell(point = Point(4, 3), letter = 'b', state = MISS),
            ),
            listOf(
                Cell(point = Point(0, 4), letter = 'e', state = EXACT),
                Cell(point = Point(1, 4), letter = 'l', state = MISS),
                Cell(point = Point(2, 4), letter = 'o', state = ALONG),
                Cell(point = Point(3, 4), letter = 'u', state = MISS),
                Cell(point = Point(4, 4), letter = 'y', state = EXACT),
            ),
        )
    )

    val SAMPLE2 = WaffleState(
        listOf(
            listOf(
                Cell(point = Point(0, 0), letter = 'c', state = EXACT),
                Cell(point = Point(1, 0), letter = 'i', state = MISS),
                Cell(point = Point(2, 0), letter = 'e', state = ALONG),
                Cell(point = Point(3, 0), letter = 'n', state = MISS),
                Cell(point = Point(4, 0), letter = 'e', state = EXACT),
            ),
            listOf(
                Cell(point = Point(0, 1), letter = 'w', state = MISS),
                Cell(point = Point(2, 1), letter = 'r', state = ALONG),
                Cell(point = Point(4, 1), letter = 'o', state = MISS),
            ),
            listOf(
                Cell(point = Point(0, 2), letter = 'x', state = MISS),
                Cell(point = Point(1, 2), letter = 'e', state = ALONG),
                Cell(point = Point(2, 2), letter = 'n', state = EXACT),
                Cell(point = Point(3, 2), letter = 'p', state = MISS),
                Cell(point = Point(4, 2), letter = 'u', state = ALONG),
            ),
            listOf(
                Cell(point = Point(0, 3), letter = 's', state = EXACT),
                Cell(point = Point(2, 3), letter = 'l', state = MISS),
                Cell(point = Point(4, 3), letter = 's', state = MISS),
            ),
            listOf(
                Cell(point = Point(0, 4), letter = 's', state = EXACT),
                Cell(point = Point(1, 4), letter = 'h', state = MISS),
                Cell(point = Point(2, 4), letter = 'e', state = ALONG),
                Cell(point = Point(3, 4), letter = 'r', state = ALONG),
                Cell(point = Point(4, 4), letter = 'e', state = EXACT),
            ),
        )
    )

    val SAMPLE3 = WaffleState(
        listOf(
            listOf(
                Cell(point = Point(0, 0), letter = 'f', state = EXACT),
                Cell(point = Point(1, 0), letter = 'b', state = MISS),
                Cell(point = Point(2, 0), letter = 'o', state = MISS),
                Cell(point = Point(3, 0), letter = 'u', state = EXACT),
                Cell(point = Point(4, 0), letter = 'e', state = EXACT),
            ),
            listOf(
                Cell(point = Point(0, 1), letter = 'g', state = MISS),
                Cell(point = Point(2, 1), letter = 'i', state = MISS),
                Cell(point = Point(4, 1), letter = 'u', state = MISS),
            ),
            listOf(
                Cell(point = Point(0, 2), letter = 'l', state = EXACT),
                Cell(point = Point(1, 2), letter = 's', state = ALONG),
                Cell(point = Point(2, 2), letter = 'o', state = EXACT),
                Cell(point = Point(3, 2), letter = 'o', state = ALONG),
                Cell(point = Point(4, 2), letter = 'm', state = ALONG),
            ),
            listOf(
                Cell(point = Point(0, 3), letter = 'g', state = MISS),
                Cell(point = Point(2, 3), letter = 'e', state = ALONG),
                Cell(point = Point(4, 3), letter = 'l', state = MISS),
            ),
            listOf(
                Cell(point = Point(0, 4), letter = 'o', state = EXACT),
                Cell(point = Point(1, 4), letter = 'e', state = ALONG),
                Cell(point = Point(2, 4), letter = 'm', state = ALONG),
                Cell(point = Point(3, 4), letter = 'n', state = MISS),
                Cell(point = Point(4, 4), letter = 'a', state = EXACT),
            ),
        )
    )
}
