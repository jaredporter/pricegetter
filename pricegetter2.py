from selenium import webdriver

with open("postcode.txt") as codes:
    postcodes = codes.read().splitlines()

class Task():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "http://www.home.co.uk/guides/sold_house_prices.htm?location=%s&month=01&year=2002"

    def update_postcodes(self):
        postcodes.remove(i)
        open("postcode.txt", "w").close()
        with open("postcode.txt", "w") as codes:
            codes.write(postcodes)

    def to_next_page(self):
        driver = self.driver
        driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(19) > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()

    def ave_price(self):
        driver = self.driver
        with open("prices.txt", "w") as price_list:
            for i in postcodes:
                driver.get(self.base_url % i)
                price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
                num_sold = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
                limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
                while limit.text != "Summary of Properties Sold in %s in January 2014" % i:
                    price_list.write(price.text.replace(u"\xa3", "") + " ")
                    price_list.write(num_sold.text + "\n")
                    self.to_next_page()
                    price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
                    num_sold = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
                    limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
                price_list.write("\n\n")
                price.flush()
                postcodes.remove(i)
                open.("postcode.txt", "w").close



t = Task()
t.ave_price()

