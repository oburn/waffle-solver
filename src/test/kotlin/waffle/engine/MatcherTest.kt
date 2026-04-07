package waffle.engine

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test

class MatcherTest {
    @Test
    fun `no matches`() {
        val matches = Matcher.search("^zzzzz$")
        assertThat(matches).isEmpty()
    }

    @Test
    fun `single match`() {
        val matches = Matcher.search("^seria$")
        assertThat(matches).containsExactlyInAnyOrder("seria")
    }

    @Test
    fun `multiple match`() {
        val matches = Matcher.search("^able[dr]$")
        assertThat(matches).containsExactlyInAnyOrder("abled", "abler")
    }
}