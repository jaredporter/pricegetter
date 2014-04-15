from selenium import webdriver

postcodes = ["E13", "E14", "E15", "E16", "E17", "E20", "EC1", "EC2", "EC3", "EC4", "N1", "N2","N3", "N4", "N5", "N6", "N7", "N8", "N10", "N15", "N16", "N17", "N19", "N22", "NW1", "NW2", "NW3", "NW4", "NW5", "NW6", "NW8", "NW11", "SE1", "SE3", "SE4", "SE5", "SE7", "SE8", "SE10", "SE11", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE22", "SE24", "SW1", "SW2", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW10", "SW11", "SW12", "SW18", "W1", "W2", "W3", "W4", "W5", "W6", "W8", "W9", "W10", "W11", "W12", "W14", "WC1", "WC2"]

class Task():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "http://www.home.co.uk/guides/sold_house_prices.htm?location=e10&month=01&year=2002"

    def ave_price(self):
        driver = self.driver
        price_list = open("Prices.txt", "w")
        for i in postcodes:
            self.base_url.replace("e10", i)
            driver.get(self.base_url)
            price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
            num_sold = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
            limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
            while limit.text != "Summary of Properties Sold in %s in January 2014" % (i):
                price_list.write(price.text.replace(u"\xa3", "") + ", ")
                price_list.write(num_sold.text + "\n")
                driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(19) > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()
                price = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
                num_sold = driver.find_element_by_css_selector(".homeco_pr_content > div:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
                limit = driver.find_element_by_css_selector(".homeco_pr_content > h2:nth-child(3)")
            price_list.write("\n\n")
        price_list.close()

t = Task()
t.ave_price()
