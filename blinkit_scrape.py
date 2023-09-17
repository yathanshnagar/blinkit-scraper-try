# Author : Yathansh Nagar

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "https://blinkit.com/prn/india-gate-mogra-basmati-rice-broken/prid/10968"

browser = webdriver.Chrome()

try:
    browser.get(url)
except Exception as e:
    print("Error:", str(e))
else:
    try:
        soup = BeautifulSoup(browser.page_source, "html.parser")

        unit_containers = soup.find_all("div", class_="ProductVariants__VariantCardContainer-sc-1unev4j-3 eYDcMS")

        grocery_names = []
        unit_sizes = []
        original_prices = []
        discount_prices = []

        for unit_container in unit_containers:
            unit_size_elem = unit_container.find("p", class_="ProductVariants__VariantUnitText-sc-1unev4j-6 dhCxof")
            unit_discount_elem = unit_container.find("div", class_="ProductVariants__PriceContainer-sc-1unev4j-7 gGENtH")
            unit_price_elem = unit_container.find("span", class_="ProductVariants__MRPText-sc-1unev4j-8 dopEwT")

            if unit_size_elem and unit_price_elem:
                unit_size = unit_size_elem.text.strip()
                unit_price = unit_price_elem.text.strip().split(' ')[0] 
                unit_discount_price = unit_discount_elem.text.strip().split(' ')[0] if unit_discount_elem else None

                grocery_names.append("India Gate Mogra Basmati Rice (Broken)") 
                unit_sizes.append(unit_size)
                original_prices.append(unit_price)
                discount_prices.append(unit_discount_price)

        product_data = {
            "Grocery Name": grocery_names,
            "Unit Size": unit_sizes,
            "Original Price": original_prices,
            "Discount Price": discount_prices,
        }

        df = pd.DataFrame(product_data)

        print(df)

    except Exception as e:
        print("Error:", str(e))

    browser.quit()
