# Analyzing Wikipedia Pages

In this guided project, you'll be working with data scraped from Wikipedia, a popular online encyclopedia. Wikipedia is maintained by volunteer content contributors and editors who continuously improve content. Anyone can edit Wikipedia, and you can read more about how to make an edit here. Because Wikipedia is crowdsourced, it's been able to rapidly assemble a huge library of articles.

In this guided project, we'll be analyzing 54 megabytes worth of articles to figure out patterns in the Wikipedia writing and content presentation style. The articles were scraped by hitting random pages on Wikipedia, then downloading the contents using the requests package. The scraping code is in this folder, in the scrape_random.py file. If you need a refresher on web scraping and HTML, you may want to check out our course before trying this guided project.

Articles were saved using the last component of their URLs. For example, a page on Wikipedia has the URL structure https://en.wikipedia.org/wiki/Yarkant_County. If we were saving the article with the previous URL, we'd save it to the file Yarkant_County.html. All the data files are stored in the wiki folder. Note that the files are raw HTML

Note that the page is a fairly standard HTML page, and has embedded Javascript code. We'll be able to ignore the embedded Javascript during our analysis, so don't worry too much about it right now.

Our main goals will be to:

    Extract only the text from the Wikipedia pages, and remove all HTML and Javascript markup.
    Remove common page headers and footers from the Wikipedia pages.
    Figure out what tags are the most common in Wikipedia pages.
    Figure out patterns in the text.
