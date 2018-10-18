from selenium import webdriver


# 开启谷歌浏览器的无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options=options)

chrome.get('http://www.baidu.com')
print(chrome.page_source)

chrome.find_element_by_id('kw').send_keys('python')

chrome.find_element_by_id('su').click()