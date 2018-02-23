# Reference USA Scraper

Scrapes data from Reference USA results tables, which are populated with the results of a POST request. Generally, you should perform your query from the [Search Page](http://www.referenceusa.com/UsBusiness/Search/Custom/). You'll then need to pull your `requestKey` by investigating POST requests passed to the server using your Browser's developer tools. Take note of the number of page results in the upper-left corner of the page, and pass that value to the `run` function.
