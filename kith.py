from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import string
import sys
import datetime

class Scraper(object):
    global driver # webdriver crashes, changing to global seems to fix
    driver = webdriver.Chrome()

    def __init__(self, url, email, firstName, lastName, address, city, zip, phone, cardNum, cardName, cardExp):
        self.url = url
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

    def scrape_init(self):
        url = self.url
        size = sys.argv[2]
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
        ccv = sys.argv[3]

        if '.5' in size:         # SHOE SIZES (Mens US 3-15, EU 36-46)
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.replace(".5", "-5"))).click()
        else:
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.lower())).click()

        f = open("status.txt", "w+")
        driver.find_element_by_name('add').click()
        product = driver.find_element_by_class_name('product-single__title').text
        f.write("{} | Added \'{}\' size {} to cart.\n".format(str(datetime.datetime.now()).split('.')[0], product, size))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'checkout'))).click() # wait for cart button
        f.write("{} | Successfully retrieved contact information page.\n".format(str(datetime.datetime.now()).split('.')[0]))

        WebDriverWait(driver, 900).until(EC.element_to_be_clickable((By.NAME, 'button'))) # wait 5 min in case of QUEUE
        driver.find_element_by_id('checkout_email').send_keys(email)
        driver.find_element_by_id('checkout_buyer_accepts_marketing').click()
        driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(firstName)
        driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(lastName)
        driver.find_element_by_id('checkout_shipping_address_address1').send_keys(address)
        driver.find_element_by_id('checkout_shipping_address_city').send_keys(city)
        driver.find_element_by_id('checkout_shipping_address_zip').send_keys(zip)
        driver.find_element_by_id('checkout_shipping_address_phone').send_keys(phone)
        driver.find_element_by_name('button').click()
        f.write("{} | Successfully inputted all contact information.\n".format(str(datetime.datetime.now()).split('.')[0]))

        # shipping button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'button'))).click()
        f.write("{} | Successfully submitted shipping page.\n".format(str(datetime.datetime.now()).split('.')[0]))

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'continue_button')))
        iframe = driver.find_element_by_class_name('card-fields-iframe') #cardNumber iframe
        driver.switch_to.frame(iframe)

        driver.find_element_by_name('number').send_keys(cardNum[0]) # w/o splitting, returns '4447'
        driver.find_element_by_name('number').send_keys(cardNum[1])
        driver.find_element_by_name('number').send_keys(cardNum[2])
        driver.find_element_by_name('number').send_keys(cardNum[3])

        driver.switch_to.default_content() #resets iframe
        iframe2 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-name")]') #card name iframe
        driver.switch_to.frame(iframe2)
        driver.find_element_by_xpath('//input[@id="name"]').send_keys(cardName)

        driver.switch_to.default_content()
        iframe3 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-expiry")]')
        driver.switch_to.frame(iframe3)
        driver.find_element_by_xpath('//input[@id="expiry"]').send_keys(cardExp[0])
        driver.find_element_by_xpath('//input[@id="expiry"]').send_keys(cardExp[1])

        driver.switch_to.default_content()
        iframe4 = driver.find_element_by_xpath('//iframe[contains(@id, "card-fields-verification_value")]')
        driver.switch_to.frame(iframe4)
        driver.find_element_by_xpath('//input[@id="verification_value"]').send_keys(ccv)
        f.write("{} | Successfully filled out payment information.\n".format(str(datetime.datetime.now()).split('.')[0]))

        driver.switch_to.default_content()
        driver.find_element_by_id('continue_button').click()
        f.write("{} | Finalized checkout and submitted \'pay now\' button.\n".format(str(datetime.datetime.now()).split('.')[0]))

def main():
    file = open(sys.argv[1])
    elements = json.loads(file.read())
    url = (elements['url'])
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

    test = Scraper(url, email, firstName, lastName, address, city, zip, phone, cardNum, cardName, cardExp)
    test.scrape_init()

if __name__ == "__main__":
    sys.argv[:]
    main()
