# Web Scraper

This script (Python 3) uses Selenium with Google Chrome to automate carting and checkout processes.


## Requires
- Selenium driver for appropriate browser version
  - [Chrome Drivers](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Link to specific product on [Kith](kith.com)
- Specified size
  - SHOES: Mens US 3-15, EU 36-46 (includes .5 sizes)
  - CLOTHING: XS - XXL

## Usage
   The product and checkout information (contact, shipping, credit card information, etc.) is supplied to the script via [file.json](https://github.com/rychao/python-scraper/blob/main/file.json):

```
{
  "url" : "https://website.com",
  "email" : "johnsmith@gmail.com",
  "firstName" : "John",
  "lastName" : "Smith",
  "address" : "8888 Kith Avenue",
  "city" : "Night City",
  "zip" : "88888",
  "phone" : "555 666 7777",
  "card number" : "4444 5555 6666 7777",
  "card name" : "John Smith",
  "card expiry" : "07 21",
 }
 ```

 After downloading locally, fill in the link of the desired product and your checkout information. When file.json is configured, kith.py will open an instance of Chrome an automatically cart and checkout the product.

 Once navigating to the proper directory, you will have to input the corresponding json file AND size (see example) as system arguments.

 For security purposes, the ccv of your card is taken as a system argument (see example)

 EXAMPLE:
 ```
 python3 kith.py file.json XL CCV
 ```

 After running the function, kith.py will output a file "status.txt" in your local directory. The purpose of this file is to diagnose how far the script got through the checkout process in the case there are any errors.

 ```
 2021-01-27 13:17:18 | Added 'KITH TREATS CHRONICLES BREAKFAST L/S TEE' size XS to cart.
 2021-01-27 13:17:21 | Successfully retrieved contact information page.
 2021-01-27 13:17:39 | Successfully inputted all contact information.
 2021-01-27 13:17:44 | Successfully submitted shipping page.
 2021-01-27 13:17:45 | Successfully filled out payment information.
 2021-01-27 13:17:45 | Finalized checkout and submitted 'pay now' button.
```
