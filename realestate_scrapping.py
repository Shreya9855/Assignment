from selenium import webdriver
from lxml import html
from time import sleep

driver = webdriver.Edge("C:/Program Files (x86)/msedgedriver.exe")
driver.get('https://hamrobazaar.com/i2994194-3-2-plus-land-kalimati.html')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(1)
tree = html.fromstring(driver.page_source)
for product_tree in tree.xpath('(//table[@class="mainbody"]//table)[27]/tbody[1]/tr[1]/td[1]'):
    details = product_tree.xpath('.//td[@id="white"][2]/text()')
print(details.strip())
print(len(details))
driver.close()

