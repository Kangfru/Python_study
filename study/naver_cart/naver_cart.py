# book
from selenium.webdriver import Firefox, FirefoxOptions

USER = "id"
PASS = "pw"

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options = options)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()

browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
products = browser.find_elements_by_css_selector(".p_info span")
print(products)
for product in products:
    print("-", product.text)