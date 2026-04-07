package waffle.engine

object Matcher {
    // File is loaded lazily the first time 'wordList' is accessed
    private val wordList: List<String> by lazy {
        val inputStream = this::class.java.classLoader.getResourceAsStream("valid-words.txt")
            ?: throw IllegalStateException("Resource 'valid-words.txt' not found on the classpath")

        inputStream.bufferedReader().use { reader ->
            reader.readLines()
        }
    }

    /**
     * Searches the loaded word list using the supplied regular expression.
     */
    fun search(regex: Regex): List<String> {
        return wordList.filter { regex.containsMatchIn(it) }
    }

    fun search(regex: String): List<String> = search(regex.toRegex())
}
