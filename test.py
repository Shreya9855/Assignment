for page in pages:
page.click()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            
            
            #General Details
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
