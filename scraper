from selenium import webdriver
#import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
url = "https://kith.com/collections/kith/products/kh2603-102"
driver.get(url)

email = "johnsmith@gmail.com"
firstName = "John"
lastName = "Smith"
address = "8888 Kith Avenue"
city = "Night City"
zip = "88888"
phone = "5556667777"

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
