from selenium import webdriver
import chromedriver_binary  # chromedriver_binaryをインポートしてパスを設定
from selenium.webdriver.common.by import By
import time
import datetime

dt_now = datetime.datetime.now()
filename = str(dt_now.year) + '-' + str(dt_now.month) + '-' + str(dt_now.day) + '.txt'

options = webdriver.chrome.options.Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.yahoo.co.jp/')
time.sleep(3)

genre = ['2', '3', '4', '5', '6', '7', '8', '1']

with open(filename, 'a', encoding='utf-8') as fw:
    for j in genre:
        genre_set = driver.find_element(By.XPATH, '//*[@id="tabTopics' + j + '"]/a').click()
        time.sleep(3)
        for i in range(1, 9):
            title = driver.find_element(By.XPATH, '//*[@id="tabpanelTopics' + j + '"]/div/div[1]/ul/li[' + str(i) + ']/article/a/div/div/h1/span')
            fw.write(title.text + '\n')
        #print(title.text)

driver.close()
