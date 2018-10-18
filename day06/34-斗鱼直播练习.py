from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.douyu.com/g_jdqs'
driver.get(url)
num = 1
while True:
    print('打印第' + str(num) + '页-------')
    num += 1
    html = driver.page_source
    # 主播名称
    names = driver.find_elements_by_xpath('//p/span[@class="dy-name ellipsis fl"]')
    # 主播热度(观众人数)
    counts = driver.find_elements_by_xpath('//p/span[@class="dy-num fr"]')

    for name, count in zip(names, counts):
        print(name.text, ':', count.text)

    if driver.page_source.find('shark-pager-next') != -1:
        # 自动点击下一页
        driver.find_element_by_xpath('//a[@class="shark-pager-next"]').click()
    else:
        break