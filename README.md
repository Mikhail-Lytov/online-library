# online-library
##A program that provides the following set of procedures for accessing it using the rest api

- /library — getting a list of available authors (no more than 3 to choose from)
- /library/{author} – getting a list of the author's name, whose name will be specified instead of {author}. If an author is specified that is not included in the list of authors, an error message with the 404 code should be returned.
- /library/{author}/{work} – getting the text of the author's name, whose name will be specified instead of {work}. If a work is specified that is not included in the list, an error message with the 404 code should be returned. In addition, this request should be able to process additional parameters:
   * begin — the first character of the output from which it should be returned on request.
   * end — the last character of the work to be returned on request.G
