package waffle.engine

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test
import waffle.engine.CellState.*
import waffle.engine.Direction.HORIZONTAL
import waffle.engine.Direction.VERTICAL
import waffle.engine.Fact.CANNOT_BE
import waffle.engine.Fact.MAY_BE
import waffle.engine.Fact.MUST_BE
import waffle.engine.Samples.SAMPLE1
import waffle.engine.Samples.SAMPLE2

class WaffleStateTest {
    @Test
    fun `test asString`() {
        assertThat(SAMPLE1.asString()).isEqualTo(
            "crmvp\nerg\nlaivy\nenb\nelouy")
    }

    @Test
    fun words() {
        val state = SAMPLE1
        assertThat(state.words()).containsExactlyInAnyOrder(
            Word(
                direction = HORIZONTAL, cells = listOf(
                    Cell(point = Point(x = 0, y = 0), letter = 'c', state = EXACT),
                    Cell(point = Point(x = 1, y = 0), letter = 'r', state = EXACT),
                    Cell(point = Point(x = 2, y = 0), letter = 'm', state = MISS),
                    Cell(point = Point(x = 3, y = 0), letter = 'v', state = MISS),
                    Cell(point = Point(x = 4, y = 0), letter = 'p', state = EXACT),
                )
            ), Word(
                direction = HORIZONTAL, cells = listOf(
                    Cell(point = Point(x = 0, y = 2), letter = 'l', state = ALONG),
                    Cell(point = Point(x = 1, y = 2), letter = 'a', state = MISS),
                    Cell(point = Point(x = 2, y = 2), letter = 'i', state = EXACT),
                    Cell(point = Point(x = 3, y = 2), letter = 'v', state = MISS),
                    Cell(point = Point(x = 4, y = 2), letter = 'y', state = ALONG),
                )
            ), Word(
                direction = HORIZONTAL, cells = listOf(
                    Cell(point = Point(x = 0, y = 4), letter = 'e', state = EXACT),
                    Cell(point = Point(x = 1, y = 4), letter = 'l', state = MISS),
                    Cell(point = Point(x = 2, y = 4), letter = 'o', state = ALONG),
                    Cell(point = Point(x = 3, y = 4), letter = 'u', state = MISS),
                    Cell(point = Point(x = 4, y = 4), letter = 'y', state = EXACT),
                )
            ), Word(
                direction = VERTICAL, cells = listOf(
                    Cell(point = Point(x = 0, y = 0), letter = 'c', state = EXACT),
                    Cell(point = Point(x = 0, y = 1), letter = 'e', state = MISS),
                    Cell(point = Point(x = 0, y = 2), letter = 'l', state = ALONG),
                    Cell(point = Point(x = 0, y = 3), letter = 'e', state = MISS),
                    Cell(point = Point(x = 0, y = 4), letter = 'e', state = EXACT),
                )
            ), Word(
                direction = VERTICAL, cells = listOf(
                    Cell(point = Point(x = 2, y = 0), letter = 'm', state = MISS),
                    Cell(point = Point(x = 2, y = 1), letter = 'r', state = MISS),
                    Cell(point = Point(x = 2, y = 2), letter = 'i', state = EXACT),
                    Cell(point = Point(x = 2, y = 3), letter = 'n', state = MISS),
                    Cell(point = Point(x = 2, y = 4), letter = 'o', state = ALONG),
                )
            ), Word(
                direction = VERTICAL, cells = listOf(
                    Cell(point = Point(x = 4, y = 0), letter = 'p', state = EXACT),
                    Cell(point = Point(x = 4, y = 1), letter = 'g', state = ALONG),
                    Cell(point = Point(x = 4, y = 2), letter = 'y', state = ALONG),
                    Cell(point = Point(x = 4, y = 3), letter = 'b', state = MISS),
                    Cell(point = Point(x = 4, y = 4), letter = 'y', state = EXACT)
                )
            )
        )
    }

    @Test
    fun cellsInline_top_corner() {
        val state = SAMPLE1
        assertThat(state.cellsInline(with = Point(0, 0))).containsExactlyInAnyOrder(
            SAMPLE1.rows[0][1], SAMPLE1.rows[0][2], SAMPLE1.rows[0][3], SAMPLE1.rows[0][4],
            SAMPLE1.rows[1][0], SAMPLE1.rows[2][0], SAMPLE1.rows[3][0], SAMPLE1.rows[4][0],
        )
    }

    @Test
    fun cellsInline_offset_middle_horizontal() {
        val state = SAMPLE1
        assertThat(state.cellsInline(with = Point(1, 2))).containsExactlyInAnyOrder(
            SAMPLE1.rows[2][0], SAMPLE1.rows[2][2], SAMPLE1.rows[2][3], SAMPLE1.rows[2][4],
        )
    }

    @Test
    fun cellsInline_offset_middle_vertical() {
        val state = SAMPLE1
        assertThat(state.cellsInline(with = Point(2, 1))).containsExactlyInAnyOrder(
            SAMPLE1.rows[0][2], SAMPLE1.rows[2][2], SAMPLE1.rows[3][1], SAMPLE1.rows[4][2],
        )
    }

    @Test
    fun cellsInline_middle() {
        val state = SAMPLE1
        assertThat(state.cellsInline(with = Point(2, 2))).containsExactlyInAnyOrder(
            SAMPLE1.rows[2][0], SAMPLE1.rows[2][1], SAMPLE1.rows[2][3], SAMPLE1.rows[2][4],
            SAMPLE1.rows[0][2], SAMPLE1.rows[1][1], SAMPLE1.rows[3][1], SAMPLE1.rows[4][2],
        )
    }

    @Test
    fun basicFactsAt_exact() {
        val state = SAMPLE1
        assertThat(state.basicFactsAt(Point(0, 0))).containsExactlyInAnyOrder(
            CellFact(point = Point(x = 0, y = 0), letter = 'c', fact = MUST_BE)
        )
    }

    @Test
    fun basicFactsAt_miss_1() {
        val state = SAMPLE1
        assertThat(state.basicFactsAt(Point(3, 0))).containsExactlyInAnyOrder(
            CellFact(point = Point(x = 2, y = 0), letter = 'v', fact = CANNOT_BE),
            CellFact(point = Point(x = 3, y = 0), letter = 'v', fact = CANNOT_BE),
            CellFact(point = Point(x = 0, y = 1), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 0, y = 2), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 0, y = 3), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 1, y = 2), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 1, y = 4), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 2, y = 1), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 2, y = 3), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 2, y = 4), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 3, y = 4), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 4, y = 1), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 4, y = 2), letter = 'v', fact = MAY_BE),
            CellFact(point = Point(x = 4, y = 3), letter = 'v', fact = MAY_BE),
        )
    }

    @Test
    fun basicFactsAt_miss_2() {
        val state = SAMPLE1
        assertThat(state.basicFactsAt(Point(0, 3))).containsExactlyInAnyOrder(
            CellFact(Point(x = 0, y = 3), letter = 'e', fact = CANNOT_BE),
            CellFact(Point(x = 0, y = 2), letter = 'e', fact = CANNOT_BE),
            CellFact(Point(x = 2, y = 0), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 3, y = 0), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 2, y = 1), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 4, y = 1), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 1, y = 2), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 3, y = 2), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 4, y = 2), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 2, y = 3), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 4, y = 3), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 1, y = 4), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 2, y = 4), letter = 'e', fact = MAY_BE),
            CellFact(Point(x = 3, y = 4), letter = 'e', fact = MAY_BE),
        )
    }

    @Test
    fun basicFactsAt_along_1() {
        val state = SAMPLE1
        assertThat(state.basicFactsAt(Point(4, 1))).containsExactlyInAnyOrder(
            CellFact(Point(x = 4, y = 1), letter = 'g', fact = CANNOT_BE),
            CellFact(Point(x = 4, y = 2), letter = 'g', fact = MAY_BE),
            CellFact(Point(x = 4, y = 3), letter = 'g', fact = MAY_BE),
        )
    }

    @Test
    fun basicFactsAt_along_2() {
        val state = SAMPLE1
        assertThat(state.basicFactsAt(Point(2, 4))).containsExactlyInAnyOrder(
            CellFact(point = Point(x = 2, y = 4), letter = 'o', fact = CANNOT_BE),
            CellFact(point = Point(x = 2, y = 0), letter = 'o', fact = MAY_BE),
            CellFact(point = Point(x = 2, y = 1), letter = 'o', fact = MAY_BE),
            CellFact(point = Point(x = 2, y = 3), letter = 'o', fact = MAY_BE),
            CellFact(point = Point(x = 1, y = 4), letter = 'o', fact = MAY_BE),
            CellFact(point = Point(x = 3, y = 4), letter = 'o', fact = MAY_BE),
        )
    }

    @Test
    fun wordRegex_1() {
        val state = SAMPLE1
        val words = state.words()
        assertThat(state.wordRegex(words[0])).isEqualTo("^cr[abelou][abelnru]p$")
        assertThat(state.wordRegex(words[1])).isEqualTo("^[bmnruy][belmnruy]i[belmnruy][eglmnru]$")
        assertThat(state.wordRegex(words[2])).isEqualTo("^e[abemnorv][abev][abemnorv]y$")
        assertThat(state.wordRegex(words[5])).isEqualTo("^p[aelmnruvy][eglmnru][aeglmnruvy]y$")
    }

    @Test
    fun `testing solving sample1`() {
        val state = SAMPLE1
        val soln = state.solve()
        assertThat(soln).containsExactly(
            Pair(WordStart(Point(x = 0, y = 0), direction = HORIZONTAL), listOf("creep", "croup")),
            Pair(
                WordStart(Point(x = 0, y = 4), direction = HORIZONTAL),
                listOf("embay", "emery", "enemy", "envoy", "every")
            ),
            Pair(
                WordStart(Point(x = 2, y = 0), direction = VERTICAL),
                listOf("alive", "baile", "blive", "oliva", "olive")
            ),
            Pair(
                WordStart(Point(x = 0, y = 0), direction = VERTICAL),
                listOf("cable", "cabre", "carle", "carne", "carve", "cruve", "cryne", "curve")
            ),
            Pair(
                WordStart(Point(x = 0, y = 2), direction = HORIZONTAL), listOf(
                    "being", "bling", "bribe", "brier", "brill", "brine",
                    "bring", "nying", "reine", "reing", "ruing", "urine"
                )
            ),
            Pair(
                WordStart(Point(x = 4, y = 0), direction = VERTICAL), listOf(
                    "palay", "pally", "palmy", "panny", "parly", "parry", "peely",
                    "peery", "peggy", "penny", "permy", "perry", "pervy", "plumy",
                    "premy", "pruny", "puggy", "pully", "pungy", "punny", "purry",
                    "pygmy"
                )
            )
        )
    }

    @Test
    fun `testing impliedFacts`() {
        assertThat(SAMPLE2.impliedFacts()).containsExactlyInAnyOrder(
            CellFact(point=Point(x=0, y=1), fact=MAY_BE, letter='e'),
            CellFact(point=Point(x=4, y=1), fact=MAY_BE, letter='e'),
            CellFact(point=Point(x=4, y=3), fact=MAY_BE, letter='e'),
            CellFact(point=Point(x=1, y=0), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=3, y=0), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=0, y=1), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=4, y=1), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=0, y=2), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=1, y=2), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=3, y=2), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=4, y=2), fact=MAY_BE, letter='r'),
            CellFact(point=Point(x=4, y=3), fact=MAY_BE, letter='r'),
        )
    }
}
