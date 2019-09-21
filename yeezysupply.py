

# this is the final version of the yeezysupply bot (works on any v2 350 shoe); just change the variable sit_up to the name of the shoe
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for backspace
import time #add time delays
import random
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException

# ---------------------------- password page opens -----------------------------
# --------------------------- open for sale ------------------------------------

email = "poptarts@gmail.com"
first_name = "UR"
last_name = "mom"
address = "1999 canada ave"
city = "Houston"
state = "California"
ZIP_code = "90210"
phone = "111-111-1111"
creditcardnum = "12345678"
creditcardname = "bob smith"
expiration_date = "1111"
security_code = "999"
'''
email = "tejas@niroola.com"
first_name = "Tejas"
last_name = "Niroola"
address = "4097 Princeton Place"
city = "Yorba Linda"
state = "California"
ZIP_code = "92886"
phone = "657-274-9874"
creditcardnum = "379578153441009"
creditcardname = "Nihsant Niroola"
expiration_date = "0321"
security_code = "616"
'''
size = "9"

#size = "M"

#-------------------- headless mode --------------------
'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(chrome_options=options)
'''
#------------------------------- upload user data for recaptcha ----------------

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);

wait = ui.WebDriverWait(driver,100000)



driver.get("https://yeezysupply.com/")


timer = datetime.datetime(2019, 9, 21, 6, 50, 0)
while datetime.datetime.now() < timer:
    time.sleep(1)

item_num = 3;
wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[{}]/div/div[2]/div[1]".format(item_num)))
itemName = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[{}]/div/div[2]/div[1]".format(item_num))

if("YEEZY BOOST 350 V2" in itemName.text):
#if(itemName.text == "YZY DSRT BT"):
    el = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[{}]/div/div[2]/form/div[2]/div/select".format(item_num))
    #el = driver.find_element_by_id("SIZE")

    for option in el.find_elements_by_tag_name('option'):
        if size in option.text:
            option.click() # select() in earlier versions of webdriver
            break
    wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[{}]/div/div[2]/form/input[3]'.format(item_num)))
    driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[{}]/div/div[2]/form/input[3]'.format(item_num)).click()
    wait.until(lambda driver: driver.find_element_by_name('checkout'))
    element = driver.find_element_by_name("checkout")
    driver.execute_script("arguments[0].click();", element)



# ------------------------------------ first page ------------------------------
wait.until(lambda driver: driver.find_element_by_id('checkout_email'))

driver.execute_script('document.getElementById("checkout_email").value="{}";'.format(email))
driver.execute_script('document.getElementById("checkout_shipping_address_first_name").value="{}";'.format(first_name))
driver.execute_script('document.getElementById("checkout_shipping_address_last_name").value="{}";'.format(last_name))
driver.execute_script('document.getElementById("checkout_shipping_address_address1").value="{}";'.format(address))
driver.execute_script('document.getElementById("checkout_shipping_address_city").value="{}";'.format(city))
driver.execute_script('document.getElementById("checkout_shipping_address_zip").value="{}";'.format(ZIP_code))
driver.execute_script('document.getElementById("checkout_shipping_address_phone").value="{}";'.format(phone))
driver.find_element_by_id("salesFinal").click()


# -------------------------- click on the recaptcha ----------------------------
'''
iframe = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div[1]/div[4]/div/div/div/div/div/div/iframe")
driver.switch_to.frame(iframe)


driver.find_element_by_id("recaptcha-anchor-label").click() #click on recaptcha

wait.until(lambda driver: driver.find_element_by_id('recaptcha-anchor').get_attribute('aria-checked') == ('true'))

'''

# -------------------------- move past page with recaptcha ---------------------


driver.switch_to.default_content()

wait.until(lambda driver: driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div[2]/button/span"))
element = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div[2]/button/span")


webdriver.ActionChains(driver).move_to_element(element[0]).click(element[0]).perform()


wait.until(lambda driver: driver.find_element_by_name('button'))
driver.find_element_by_name("button").click()

wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/div/div[1]/iframe'))
dif_address = "true"


creditnum=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/div/div[1]/iframe")
driver.switch_to.frame(creditnum)
driver.execute_script('document.getElementById("number").value="{}";'.format(creditcardnum))

driver.switch_to.default_content()
creditname = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div/iframe")
driver.switch_to.frame(creditname)
driver.execute_script('document.getElementById("name").value="{}";'.format(creditcardname))

driver.switch_to.default_content()
expirframe = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[3]/div[3]/div[3]/div/div/iframe")
driver.switch_to.frame(expirframe)
driver.execute_script('document.getElementById("expiry").value="{}";'.format(expiration_date))

driver.switch_to.default_content()
securityframe = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[3]/div[3]/div[4]/div/div[1]/iframe")
driver.switch_to.frame(securityframe)
driver.execute_script('document.getElementById("verification_value").value="{}";'.format(security_code))

driver.switch_to.default_content()

driver.find_element_by_id("checkout_different_billing_address_false").click()
checkout_final = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[3]/div[1]/button")

driver.execute_script("arguments[0].click();", checkout_final)
print("This was a success")
