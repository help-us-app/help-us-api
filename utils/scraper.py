from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, body, cart_type):
        self.cart_type = cart_type
        self.soup = BeautifulSoup(body, 'html.parser')

    def scrape_body(self):
        if self.cart_type == 'amazon':
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
