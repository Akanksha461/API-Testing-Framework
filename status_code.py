import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chromepath = "/home/aj/going_headless/chromedriver"
driver=webdriver.Chrome(chromepath)
# chrome_options = Options()
# chrome_options.add_extension("/home/aj/Downloads/way2sms_v3.8.crx")
# DesiredCapabilities.desiredcapabilities=DesiredCapabilities.CHROME()
# DesiredCapabilities.setCapability(chrome_options.CAPABILITY, chrome_options)
# driver= webdriver.Chrome(desired_capabilities=DesiredCapabilities)
# # driver = webdriver.Firefox(capabilities=capabilities)
# #
# # 		DesiredCapabilities desiredcapabilities=DesiredCapabilities.chrome();
# # 		desiredcapabilities.setCapability(chromeoption.CAPABILITY, chromeoption);
# # 		driver=new ChromeDriver(desiredcapabilities);
driver.get("http://lotteryadmin.sia.co.in/#/login")
r = requests.get("http://lotteryadmin.sia.co.in/#/login")
print (r.status_code)

if r.status_code ==100:
    print("server is working fine")


else:
    driver.get("http://site21.way2sms.com/content/index.html?")
    driver.find_element_by_id("username").send_keys("8591771290")
    driver.find_element_by_id("password").send_keys("P5879N")
    driver.find_element_by_id("loginBTN").click()
    driver.find_element_by_id("sendSMS").click()
    driver.switch_to.frame("frame")
    driver.find_element_by_id("mobile").send_keys("8591771290")
    driver.find_element_by_id("message").send_keys("hi")
    time.sleep (4)
    # driver.find_element_by_id("Send").click()
    # time.sleep (10)
    # print("way to sms")

# driver.quit()