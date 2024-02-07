# USD/MXN
# $ MXN

# convert USD and MXN interchangeably
import requests
from bs4 import BeautifulSoup


def get_usd_mxn_rate():
    url = "https://www.investing.com/currencies/usd-mxn"
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
            return price
        else:
            return "Price couldn't be found."
    else:
        return "Failed to load pages"


if __name__ == "__main__":
    print(get_usd_mxn_rate())
