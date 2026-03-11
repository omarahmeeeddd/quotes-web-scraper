import requests
from bs4 import BeautifulSoup

for page in range(1, 11):

    url = f"http://quotes.toscrape.com/page/{page}"
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        
        print(text)
        print(author)
        print("------")