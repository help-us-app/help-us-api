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
        elif self.cart_type == self.constants.ebay_cart_url:
            return self.scrape_ebay()
        elif self.cart_type == self.constants.target_cart_url:
            return self.scrape_target()
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

    def scrape_ebay(self):
        scraped_items = self.soup.find_all('ul', class_='cart-bucket__vendor-list')
        items = []
        for item in scraped_items:
            item_link = item.find_all_next('a', attrs={'data-test-id': 'cart-item-link'})
            quantity = item.find_all_next('select', attrs={'data-test-id': 'qty-dropdown'})

            items.append({
                'title': item_link[0].text.strip(),
                'price': item.find('div', class_='item-price').text.strip().replace('US', ''),
                'productImage': item.find('div', class_='image-display').find('img').attrs['src'],
                'productLink': item_link[0].attrs['href'],
                'quantity': quantity[0].findNext('option', attrs={'selected': ''}).attrs['value'],
            })
        return items

    def scrape_target(self):
        scraped_items = self.soup.find_all('div', attrs={'data-test': 'cartItem'})
        items = []

        for item in scraped_items:
            quantity = "1"
            url = item.find_all('a', attrs={'data-test': 'cartItem-title-url'})
            image = item.find_all('picture', attrs={'data-test': 'cartItem-image'})
            price = item.find_all('p', attrs={'data-test': 'cartItem-price'})[0].text.strip().replace('$', '')
            unit_price = item.find_all('p', attrs={'data-test': 'cartItem-unitPrice'})
            if len(unit_price) > 0:
                unit_price = unit_price[0].text.strip().replace('each ', '').replace('$', '')
                quantity = f"{int(float(price) / float(unit_price))}"
                price = f"${unit_price}"

            items.append({
                'title': item.find('div', attrs={'data-test': 'cartItem-title'}).text.strip(),
                'quantity': quantity,
                'productImage': image[0].find('source').attrs['srcset'],
                'productLink': url[0].attrs['href'],
                'price': price,
            })
            print(items[-1])

        return items
