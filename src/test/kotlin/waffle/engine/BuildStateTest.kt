package waffle.engine

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.assertThrows
import org.junit.jupiter.api.Test
import waffle.engine.CellState.MISS

class BuildStateTest {
    @Test
    fun `not enough lines`() {
        assertThrows<IllegalArgumentException> {
            buildState(from = "abc")
        }
    }

    @Test
    fun `short lines`() {
        val ex = assertThrows<IllegalArgumentException> {
            buildState(from = "12345\n2\n3\n4\n5")
        }

        assertThat(ex).hasMessage("Not correct chars on line 1")
    }

    @Test
    fun goldilocks() {
        val state = buildState(from = "abcde\nfgh\nijklm\nnop\nqrstu\nignored")
        val expecting = listOf<Row>(
            listOf(
                Cell(Point(x = 0, y = 0), letter = 'a', state = MISS),
                Cell(Point(x = 1, y = 0), letter = 'b', state = MISS),
                Cell(Point(x = 2, y = 0), letter = 'c', state = MISS),
                Cell(Point(x = 3, y = 0), letter = 'd', state = MISS),
                Cell(Point(x = 4, y = 0), letter = 'e', state = MISS),
            ),
            listOf(
                Cell(Point(x = 0, y = 1), letter = 'f', state = MISS),
                Cell(Point(x = 2, y = 1), letter = 'g', state = MISS),
                Cell(Point(x = 4, y = 1), letter = 'h', state = MISS),
            ),
            listOf(
                Cell(Point(x = 0, y = 2), letter = 'i', state = MISS),
                Cell(Point(x = 1, y = 2), letter = 'j', state = MISS),
                Cell(Point(x = 2, y = 2), letter = 'k', state = MISS),
                Cell(Point(x = 3, y = 2), letter = 'l', state = MISS),
                Cell(Point(x = 4, y = 2), letter = 'm', state = MISS),
            ),
            listOf(
                Cell(Point(x = 0, y = 3), letter = 'n', state = MISS),
                Cell(Point(x = 2, y = 3), letter = 'o', state = MISS),
                Cell(Point(x = 4, y = 3), letter = 'p', state = MISS),
            ),
            listOf(
                Cell(Point(x = 0, y = 4), letter = 'q', state = MISS),
                Cell(Point(x = 1, y = 4), letter = 'r', state = MISS),
                Cell(Point(x = 2, y = 4), letter = 's', state = MISS),
                Cell(Point(x = 3, y = 4), letter = 't', state = MISS),
                Cell(Point(x = 4, y = 4), letter = 'u', state = MISS),
            ),
        )
        assertThat(state.rows).isEqualTo(expecting)
    }
}