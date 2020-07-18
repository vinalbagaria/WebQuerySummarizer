# WebQuerySummarizer
A Web application which generates an extractive summary of single domain multi documents (scraped web pages) based on user web query using web scraping, NLP


Flow of the system:
  1. Allow users to enter queries on a web application.
  2. Get the results from searching the query on google.
  3. From the multiple results, extract all the links on the first page as they are highly relevant to user query
  4. Scrape and clean the data from all these links and store it in a text file.
  5. Send the data to NLP based models to generate a summary.


User can enter any query based on single domain.

![Alt text](screenshots/index.png?raw=true "Query")


Lemmatization, Stop words removal and punctuation etc. are used for preprocessing the text and cosine similarity and the TextRank algorithm is used for the extractive summary generation.

![Alt text](screenshots/result.png?raw=true "Summary")