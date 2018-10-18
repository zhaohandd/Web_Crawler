from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('http://www.baidu.com')

# 保存网站当前屏幕截图
chrome.save_screenshot('baidu.jpg')

# 网站html源码
html = chrome.page_source
print(html)