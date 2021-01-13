from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import string

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Scraper(object):
    global driver # webdriver crashes, changing to global seems to fix
    driver = webdriver.Chrome()

    def __init__(self, url, size, email, firstName, lastName, address, city, zip, phone, cardNum, cardName, cardExp, ccv):
        self.url = url
        self.size = size
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone
        self.cardNum = cardNum
        self.cardName = cardName
        self.cardExp = cardExp
        self.ccv = ccv

    def scrape_init(self):
        #kith US SHOE: https://kith.com/collections/mens-footwear/products/vn0a4uud1mk
        #kith gloves: https://kith.com/collections/kith/products/kh9588-101
        url = self.url
        size = self.size
        print("Requested Size: ", size)
        driver.get(url)

        email = self.email
        firstName = self.firstName
        lastName = self.lastName
        address = self.address
        city = self.city
        zip = self.zip
        phone = self.phone
        cardNum = self.cardNum.split()
        cardName = self.cardName
        cardExp = self.cardExp.split()
        ccv = self.ccv

        # if size == 'S' or size == 'M' or size == 'L' or size == "XL":         # CLOTHING SIZE (missing XS)
        #     driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.lower())).click()

        if '.5' in size:         # SHOE SIZES (Mens US 3-15, EU 36-46)
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.replace(".5", "-5"))).click()
        else:
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.lower())).click()

        driver.find_element_by_name('add').click()
        driver.implicitly_wait(60) # wait for cart button
        driver.find_element_by_name('checkout').click()
        driver.implicitly_wait(60) # wait 1 min in case of QUEUE

        emailInput = driver.find_element_by_id('checkout_email')
        emailInput.send_keys(email)
        driver.find_element_by_id('checkout_buyer_accepts_marketing').click()
        driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(firstName)
        driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(lastName)
        driver.find_element_by_id('checkout_shipping_address_address1').send_keys(address)
        driver.find_element_by_id('checkout_shipping_address_city').send_keys(city)
        driver.find_element_by_id('checkout_shipping_address_zip').send_keys(zip)
        driver.find_element_by_id('checkout_shipping_address_phone').send_keys(phone)
        driver.find_element_by_name('button').click()

        #shipping button
        driver.find_element_by_name('button').click()

        driver.implicitly_wait(60)
        iframe = driver.find_element_by_class_name('card-fields-iframe') #cardNumber iframe
        driver.switch_to.frame(iframe)

        driver.find_element_by_name('number').send_keys(cardNum[0]) # w/o splitting, returns '4447'
        driver.find_element_by_name('number').send_keys(cardNum[1])
        driver.find_element_by_name('number').send_keys(cardNum[2])
        driver.find_element_by_name('number').send_keys(cardNum[3])

        driver.switch_to_default_content() #resets iframe
        iframe2 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-name")]') #card name iframe
        driver.switch_to.frame(iframe2)
        driver.find_element_by_xpath('//input[@id="name"]').send_keys(cardName)

        driver.switch_to_default_content()
        iframe3 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-expiry")]')
        driver.switch_to.frame(iframe3)
        driver.find_element_by_xpath('//input[@id="expiry"]').send_keys(cardExp[0])
        driver.find_element_by_xpath('//input[@id="expiry"]').send_keys(cardExp[1])

        driver.switch_to_default_content()
        iframe4 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-verification_value")]')
        driver.switch_to.frame(iframe4)
        driver.find_element_by_xpath('//input[@id="verification_value"]').send_keys(ccv)

        driver.switch_to_default_content()
        driver.find_element_by_id('continue_button').click()


def main():
    file = open('file.json')
    elements = json.loads(file.read())
    url = (elements['url'])
    size = (elements['size'])
    email = (elements['email'])
    firstName = (elements['firstName'])
    lastName = (elements['lastName'])
    address = (elements['address'])
    city = (elements['city'])
    zip = (elements['zip'])
    phone = (elements['phone'])
    cardNum = (elements['card number'])
    cardName = (elements['card name'])
    cardExp = (elements['card expiry'])
    ccv = (elements['ccv'])

    test = Scraper(url, size, email, firstName, lastName, address, city, zip, phone, cardNum, cardName, cardExp, ccv)
    test.scrape_init()

if __name__ == "__main__":
 	main()
