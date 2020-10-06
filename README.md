# IECA-member-scraping
Scrape profile member from https://www.iecaonline.com/quick-links/member-directory/ using following library

1. request
2. json
3. BeautifulSoup
4. Selenium

Flow of scraper are following
1. Using https://www.iecaonline.com/wp-content/plugins/netforum-importer-with-sync/memberSearchAjax.php for getting whole informations in member directory page since the actual data displayed using jquery table
2. According to response result, extract the url in href for getting detailed profile of the member
3. Export extracted data into pandas

