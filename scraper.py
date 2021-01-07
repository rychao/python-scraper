from selenium import webdriver
#import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.keys import Keys

import json

class Scraper(object):

    global driver # webdriver crashes, changing to global seems to fix
    driver = webdriver.Chrome()

    def __init__(self, url, size, email, firstName, lastName, address, city, zip, phone):
        self.url = url
        self.size = size
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone


    def scrape_init(self):

        #driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
        url = self.url
        size = self.size
        #size = input("Size: ")
        print("Requested Size: ", size)
        driver.get(url)

        email = self.email
        firstName = self.firstName
        lastName = self.lastName
        address = self.address
        city = self.city
        zip = self.zip
        phone = self.phone
        cardNum1 = "4444"
        cardNum2 = "5555"
        cardNum3 = "6666"
        cardNum4 = "7777"
        cardName = "john smith"
        cardExp1 = "7" #07/21
        cardExp2 = "21"
        ccv = "666"


        # determines size to click before carting
        if size == 'S':
            driver.find_element_by_xpath('//div[@data-value="S" and @class="swatch-element s"]').click()
        elif size == 'M':
            driver.find_element_by_xpath('//div[@data-value="M" and @class="swatch-element m"]').click()
        elif size == 'L':
            driver.find_element_by_xpath('//div[@data-value="L" and @class="swatch-element l"]').click()
        else:
            driver.find_element_by_xpath('//div[@data-value="XL" and @class="swatch-element xl"]').click()

        driver.find_element_by_name('add').click()
        #Takes a moment to add to cart, buffer for 5sec
        driver.implicitly_wait(5)
        driver.find_element_by_name('checkout').click()
        driver.implicitly_wait(60) #waits up to 60s if queue

        #emailInput = driver.find_element_by_xpath('//*[@id="checkout_email"]')
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
        iframe = driver.find_element_by_class_name('card-fields-iframe')
        driver.switch_to.frame(iframe)

        #driver.find_element_by_name('number').send_keys(cardNum1, cardNum2, cardNum3, cardNum4, Keys.TAB, cardName, Keys.TAB, cardExp1, cardExp2, Keys.TAB, ccv)

        cardPayment = driver.find_element_by_name('number')
        cardPayment.send_keys(cardNum1)
        cardPayment.send_keys(cardNum2)
        cardPayment.send_keys(cardNum3)
        cardPayment.send_keys(cardNum4, Keys.TAB)
        cardPayment.send_keys(cardName, Keys.TAB)
        cardPayment.send_keys(cardExp1, Keys.TAB)
        cardPayment.send_keys(cardExp2)

        #driver.find_element_by_name('name').send_keys(cardName)

        #driver.find_element_by_name('expiry').send_keys(cardExp)
        #driver.find_element_by_name('verification_value').send_keys(ccv)


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
    #print(phone)

    test = Scraper(url, size, email,firstName,lastName,address,city,zip,phone)
    test.scrape_init()

if __name__ == "__main__":
 	main()
