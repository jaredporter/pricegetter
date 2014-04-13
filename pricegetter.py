from selenium import webdriver
class Task():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.home.co.uk/guides/sold_house_prices.htm?location=e13&month=01&year=2002"

    def ave_price(self):
        driver = self.driver
        driver.get(self.base_url)
        price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
	limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
        price_list = open("Prices.txt", "w")
        while limit.text != "Summary of Properties Sold in E13 in January 2014":
            price_list.write(price.text.replace(u"\xa3", "") + "\n")
            driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(19) > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()
            price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
            limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
        price_list.close()

t = Task()
t.ave_price()
