package waffle.app

import io.javelit.components.text.MarkdownComponent
import io.javelit.core.Jt
import io.javelit.core.Server
import waffle.engine.Cell
import waffle.engine.CellState
import waffle.engine.Fact
import waffle.engine.Samples
import waffle.engine.Solution
import waffle.engine.WaffleState
import waffle.engine.buildState
import waffle.engine.isEven

class AppRunner(
    var state: WaffleState,
    val port: Int = 9999,
    var solution: Solution? = null
) {
    fun app() {
        val currentPage = Jt.navigation(
            Jt.page("/home", { homePage() }).home(),
            Jt.page("/bulkLetters", { buildLettersPage() }),
            Jt.page("/bulkStates", { buildStatesPage() }),
        )
            .hidden()
            .use()
        currentPage.run()
    }

    fun homePage() {
        state.rows.forEachIndexed { rowIndex, cells ->
            val row = Jt.columns(5).key("row-${rowIndex}").use()
            cells.forEachIndexed { cellIndex, cell ->
                val adjustedCellIndex = if (rowIndex.isEven()) cellIndex else cellIndex * 2
                cell.markdown().use(row.col(adjustedCellIndex))
            }
        }

        Jt.divider().use()
        val buttons = Jt.columns(4).use()
        if (Jt.button("Bulk letters").use(buttons.col(0))) {
            Jt.switchPage("/bulkLetters")
        }
        if (Jt.button("Bulk states").use(buttons.col(1))) {
            Jt.switchPage("/bulkStates")
        }
        if (Jt.button("Solve").use(buttons.col(2))) {
            solution = state.solve()
            state = state.copy(extraFacts = state.allFacts().filter { it.fact == Fact.CANNOT_BE }.toSet())
        }
        if (Jt.button("Wipe").use(buttons.col(3))) {
            solution = null
            state = state.copy(extraFacts = emptySet())
        }

        val soln = solution
        if (soln != null) {
            Jt.subheader("Candidates:").use()
            Jt.text(soln.candidates
                .joinToString("\n") { "${it.start.point} - ${it.start.direction} - ${it.candidates}" })
                .use()
            if (soln.singleLetters.isNotEmpty()) {
                Jt.subheader("Single letters:").use()
                Jt.text(soln.singleLetters.joinToString("\n") { "${it.point} - ${it.letter}" }).use()
            }
            Jt.subheader("All Facts (${state.allFacts().size})").use()
            Jt.text(state.allFacts().sortedBy { it.point }.joinToString("\n") { "$it" }).use()
        }

        Jt.subheader("Extra Facts (${state.extraFacts.size})").use()
        Jt.text(state.extraFacts.joinToString("\n") { "$it" }).use()
    }

    fun buildLettersPage() {
        Jt.header("Enter letters:").use()

        val input = Jt.textArea("Letters")
            .value(state.asString())
            .use()

        if (input.isNotEmpty() && input != state.asString()) {
            state = buildState(input, state)
            Jt.switchPage("/home")
        }
    }

    fun buildStatesPage() {
        state.rows.forEachIndexed { rowIndex, cells ->
            val row = Jt.columns(5).key("row-${rowIndex}").use()
            cells.forEachIndexed { cellIndex, cell ->
                val adjustedCellIndex = if (rowIndex.isEven()) cellIndex else cellIndex * 2
                if (Jt.button(cell.state.toString())
                        .icon(cell.icon())
                        .key("button-$rowIndex-$adjustedCellIndex")
                        .use(row.col(adjustedCellIndex))
                ) {
                    state = state.rotateState(rowIndex, cellIndex)
                    Jt.switchPage("/bulkStates")
                }
            }
        }
        Jt.divider().use()

        if (Jt.button("Back").use()) {
            Jt.switchPage("/home")
        }
    }

    fun run(): Int {
        println("Starting waffle using port: $port")
        val server = Server.builder({ app() }, port).build()
        server.start()
        return 0
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val app = AppRunner(state = Samples.SAMPLE3)
            app.run()
            // Don't exit, as the HTTP server is running.
        }
    }
}

fun Cell.markdown(): MarkdownComponent.Builder {
    val color = when (this.state) {
        CellState.EXACT -> "#90EE90"
        CellState.ALONG -> "#FFFF00"
        CellState.MISS -> "#FFFFFF"
    }
    return Jt.markdown("# <span style='background-color: ${color}; padding: 10px 10px;'>**${this.letter}**</span>")
}

fun Cell.icon(): String {
    return when (this.state) {
        CellState.EXACT -> ":check:"
        CellState.ALONG -> ":compare_arrows:"
        CellState.MISS -> ":close:"
    }
}