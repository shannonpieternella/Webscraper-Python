import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.bbc.com/news"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and print the titles and links of top news articles
    articles = soup.find_all("div", class_="gs-c-promo")
    
    for article in articles:
        headline = article.find("h3", class_="gs-c-promo-heading__title")
        link = article.find("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
        
        if headline and link:
            article_title = headline.get_text(strip=True)
            article_link = link["href"]
            print(f"Title: {article_title}")
            print(f"Link: {article_link}")
            print("\n")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
