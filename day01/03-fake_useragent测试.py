from fake_useragent import UserAgent
"""
    Python库(fake-useragent),可以随机生成各种UserAgent
"""
ua = UserAgent()

print(ua.chrome)
print(ua.firefox)
print(ua.ie)