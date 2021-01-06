from selenium import webdriver
#import chromedriver_binary  # Adds chromedriver binary to path

import json

class Scraper(object):
     def __init__(self, email, firstName, lastName, address, city, zip, phone):
         self.email = email
         self.firstName = firstName
         self.lastName = lastName
         self.address = address
         self.city = city
         self.zip = zip
         self.phone = phone


     def scrape_init(self):

         driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
         url = "https://kith.com/collections/kith/products/kh9588-101"
         driver.get(url)

         email = self.email
         firstName = self.firstName
         lastName = self.lastName
         address = self.address
         city = self.city
         zip = self.zip
         phone = self.phone

         # change data-value and class to specific size
         driver.find_element_by_xpath('//div[@data-value="XL" and @class="swatch-element xl"]').click()
         driver.find_element_by_name('add').click()

         #Takes a moment to add to cart, buffer for 5sec
         driver.implicitly_wait(5)
         driver.find_element_by_name('checkout').click()

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

         driver.implicitly_wait(5)
         driver.find_element_by_id('cards-fields-number-qgj5rasctgc00000').send_keys(creditCardNum)

def main():
     file = open('file.json')
     elements = json.loads(file.read())
     email = (elements['email'])
     firstName = (elements['firstName'])
     lastName = (elements['lastName'])
     address = (elements['address'])
     city = (elements['city'])
     zip = (elements['zip'])
     phone = (elements['phone'])
     #print(email)

     test = Scraper(email,firstName,lastName,address,city,zip,phone)
     test.scrape_init()

if __name__ == "__main__":
 	main()
