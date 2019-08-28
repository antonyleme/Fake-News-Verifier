from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome('chromedriver')
browser.get('https://seoseotools.com/mozrank-checker')
browser.find_element_by_xpath('//*[@id="url"]').send_keys('https://www.facebook.com')
browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div/input').click()
print('Nota: '+browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/table/tbody/tr[2]/td[2]/strong').text)
print('Rank: '+browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/table/tbody/tr[3]/td[2]/strong').text)

browser.close()

