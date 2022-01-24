from selenium import webdriver
from lxml import html
from time import sleep


driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
for i in range(0,20,10):
    driver.get('https://hamrobazaar.com/c112-real-estate?catid=112&order=popularad&offset={}'.format(i))
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(1)
    tree = html.fromstring(driver.page_source)
    for product_tree in tree.xpath('(//table[@class="mainbody"]//table)[30]'):
        if tree.xpath('.//table[@id="mbuzz"]'):
            title = tree.xpath('(//td[@id="tab_cat1"]//table)[*]/tbody[1]/tr[2]/td[2]/a[1]/font[1]/b[1]/text()')
            price = tree.xpath('(//td[@id="tab_cat1"]//table)[*]/tbody[1]/tr[2]/td[4]/b[1]/text()')
            seller = tree.xpath('(//td[@id="tab_cat1"]//table)[*]/tbody[1]/tr[2]/td[2]/a[2]/text()')
            date = tree.xpath('(.//td[@id="tab_cat1"]//table)[*]/tbody[1]/tr[2]/td[3]/text()')
        if tree.xpath('(.//table)[*]/tbody[1]/tr[1]/td[*]'):
            title = tree.xpath('(.//table)[*]/tbody[1]/tr[1]/td[3]/a[1]/font[1]/b[1]/b[1]/text()')
            price = tree.xpath('(.//td//table)[*]/tbody[1]/tr[1]/td[5]/b/text()')
            seller = tree.xpath('(.//table)[*]/tbody[1]/tr[1]/td[3]/a[2]/text()')
            date = tree.xpath('(.//table)[*]/tbody[1]/tr[1]/td[4]/text()')


    with open("output_data.csv",'w') as out_file:
        for i in range((len(seller))):
            out_string = ""
            out_string += str(title[i])
            out_string += ", " + str(price[i])
            out_string += ", " + str(seller[i])
            out_string += ", " + str(date[i])
            print (out_string)
        
driver.close()