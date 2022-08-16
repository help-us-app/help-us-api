from bs4 import BeautifulSoup

from constants.constants import Constants


class Scraper:
    def __init__(self, body, url):
        self.cart_type = url
        self.constants = Constants()
        self.soup = BeautifulSoup(body, 'html.parser')

    def scrape_body(self):
        if self.cart_type == self.constants.amazon_cart_url:
            return self.scrape_amazon()
        return None

    def scrape_amazon(self):
        scraped_items = self.soup.find_all('div',
                                           class_='a-row sc-list-item sc-list-item-border sc-java-remote-feature')
        items = []
        for item in scraped_items:
            items.append({
                'title': item.find('span', class_='sc-product-title').text.strip(),
                'price': item.find('span', class_='sc-product-price').text.strip(),
                'productImage': item.find('img', class_='sc-product-image').attrs['src'],
                'productLink': item.find('a', class_='sc-product-link').attrs['href'],
                'quantity': item.attrs['data-quantity'],
            })
        return items
