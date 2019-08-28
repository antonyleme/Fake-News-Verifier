from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
options.add_argument("--headless")
options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=options, executable_path='/home/gear/Downloads/chromedriver')
browser.get('https://seoseotools.com/alexa-rank-checker')
browser.find_element_by_xpath('//*[@id="url"]').send_keys('https://www.facebook.com')
browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div/input').click()
print('Rank Global: '+ browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td[2]').text)
print('Rank Regional: '+browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]').text)
browser.close()

