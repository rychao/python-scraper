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
  "ccv" : "456"
 }
 ```

 After downloading locally, fill in the link of the desired product and your checkout information. When file.json is configured, kith.py will open an instance of Chrome an automatically cart and checkout the product.

 Once navigating to the proper directory, you will have to input the corresponding json file AND size (see example) as system arguments.

 EXAMPLE:
 ```
 python3 kith.py file.json XL
 ```
