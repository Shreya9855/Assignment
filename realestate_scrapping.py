from selenium import webdriver
from lxml import html
from time import sleep


driver = webdriver.Edge("C:/Program Files (x86)/msedgedriver.exe")


for i in range(0,20,10):
    driver.get('https://hamrobazaar.com/c112-real-estate?catid=112&order=popularad&offset={}'.format(i))
    sleep(1)
    driver.maximize_window()
    sleep(1)
    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('(//table[@class="mainbody"]//table)[27]/tbody[1]/tr[1]/td[1]'):
        pages = tree.xpath('(//table[@class="mainbody"]//table)[*]/tbody[1]/tr[1]/td[3]/a[1]/@href')
        for page in pages:
            new_page = ("https://hamrobazaar.com/" +page)
            
            driver.switchTo.window("new_page")
            driver.get(new_page)
            sleep(5)
            #for info in new_page.xpath('(//table[@class="mainbody"]//table)[*]/tbody[1]/tr[1]/td[3]/a[1]/@href'):
            #General Details
            Product_tree = html.fromstring(driver.execute(new_page)) 
            ad_Id = product_tree.xpath('.//table[@id="lblue"][1]/tbody/tr[2]/td[2]/text()')
            ad_Views = product_tree.xpath('.//table[@id="lblue"][1]/tbody/tr[3]/td[2]/text()')
            ad_Post_Date = product_tree.xpath('.//table[@id="lblue"][1]/tbody/tr[4]/td[2]/text()')
            ad_Expiry_Date = product_tree.xpath('.//table[@id="lblue"]/tbody[1]/tr[5]/td[2]/b[1]/text()')
            #Seller Details
            sold_by = product_tree.xpath('//table[@id="lblue"][2]/tbody/tr[2]/td[2]/text()')
            member_Since=product_tree.xpath('//table[@id="lblue"][2]/tbody/tr[3]/td[2]/text()')
            email=product_tree.xpath('//table[@id="lblue"][2]/tbody/tr[4]/td[2]/a/@href')
            location=product_tree.xpath('//table[@id="lblue"][2]/tbody/tr[5]/td[2]/text()')
            mobile=product_tree.xpath('//table[@id="lblue"][2]/tbody/tr[6]/td[2]/text()')
            #Description
            des = product_tree.xpath('(//table[@class="mainbody"]//table)[22]/tbody[1]/tr[2]/td[1]/text()')
            #Price
            price = product_tree.xpath('//table[@id="lblue"][3]/tbody/tr[2]/td[2]/font/text()')
            negotiable = product_tree.xpath('//table[@id="lblue"][3]/tbody/tr[3]/td[2]/text()')
            #Property Details
            propertyLocation = product_tree.xpath('//table[@id="lblue"][4]/tbody/tr[2]/td[2]/text()')
            propertyAddress = product_tree.xpath('//table[@id="lblue"][4]/tbody/tr[3]/td[2]/text()')
            propertyType = product_tree.xpath('//table[@id="lblue"][4]/tbody/tr[4]/td[2]/text()')
            landSize = product_tree.xpath('//table[@id="lblue"][4]/tbody/tr[5]/td[2]/text()')
        
        with open("output_data.csv",'w') as out_file:
            for i in range(len(ad_Id)):
                out_string = ""
                out_string += str(ad_Id[i])
                out_string += str(sold_by[i])
                out_string += str(des[i])
                out_string += str(price[i])
                out_string += str(propertyLocation[i]) 
                print (out_string)
                print('Thank you')

driver.close()
