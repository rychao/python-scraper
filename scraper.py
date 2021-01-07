from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import string

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
        cardNum0 = cardNum[0]
        cardNum1 = cardNum[1]
        cardNum2 = cardNum[2]
        cardNum3 = cardNum[3]
        cardName = self.cardName
        cardExp = self.cardExp.split()
        cardExp0 = cardExp[0]
        cardExp1 = cardExp[1]
        ccv = self.ccv

        if size == 'S' or size == 'M' or size == 'L' or size == "XL":         # CLOTHING SIZE (missing XS)
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.lower())).click()

        if '.5' in size:         # SHOE SIZES (Mens US 3-15, EU 36-46)
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size.replace(".5", "-5"))).click()
        else:
            driver.find_element_by_xpath('//div[@data-value="{}" and @class="swatch-element {}"]'.format(size, size)).click()

        driver.find_element_by_name('add').click()
        driver.implicitly_wait(5) # wait for cart button
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
        iframe = driver.find_element_by_class_name('card-fields-iframe')
        driver.switch_to.frame(iframe)

        #driver.find_element_by_name('number').send_keys(cardNum0, cardNum1, cardNum2, cardNum3, Keys.TAB, cardName, Keys.TAB, cardExp0, cardExp1, Keys.TAB, ccv)

        cardPayment = driver.find_element_by_name('number')
        cardPayment.send_keys(cardNum0)
        cardPayment.send_keys(cardNum1)
        cardPayment.send_keys(cardNum2)
        cardPayment.send_keys(cardNum3)

        # cardPayment.send_keys(cardName)
        # cardPayment.send_keys(cardExp0)
        # cardPayment.send_keys(cardExp1)

        driver.find_element_by_name('name').send_keys(cardName)
        driver.find_element_by_name('expiry').send_keys(cardExp0)
        driver.find_element_by_name('expiry').send_keys(cardExp1)
        driver.find_element_by_name('verification_value').send_keys(ccv)


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
