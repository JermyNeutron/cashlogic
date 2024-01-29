# convert USD and PHP interchangeably
import requests
from bs4 import BeautifulSoup


def get_usd_php_rate():
    url = "https://www.investing.com/currencies/usd-php"
    response = requests.get(url)

    # specify which html targets
    price_class_el = "text-5xl/9"
    price_data_el = "instrument-price-last"

    # fetching data
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # find html targets
        price_div = soup.find(
            "div", {"class": price_class_el, "data-test": price_data_el}
        )

        if price_div:
            # extract price
            price = price_div.text.strip()
            return float(price)
        else:
            return "Price couldn't be found."
    else:
        return "Failed to load pages"

def am_bookmarked():
    print(f"Current rate is $1 USD to ₱{get_usd_php_rate()} PHP")

if __name__ == "__main__":
    print(get_usd_php_rate())
