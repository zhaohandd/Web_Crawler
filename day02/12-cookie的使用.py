from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = 'http://www.sxt.cn/index/user.html'
headers = {
    'User-agent': UserAgent().chrome,
    'Cookie': 'acw_tc=7b39758215363011943874835e1d3215bb94a146b06916441ade66e322bb46; UM_distinctid=165b2b21496193-0101c13d25471b-323b5b03-1fa400-165b2b21498c8; CNZZDATA1261969808=433646691-1536299364-%252F%252Fwww.sxt.cn%252F%7C1536299364; NTKF_T2D_CLIENTID=guest198E67AC-C852-3A32-8764-B2B2166CCDA7; 53gid2=10402417542006; 53gid0=10402417542006; 53gid1=10402417542006; 53revisit=1536301341404; PHPSESSID=7jouclm3cqejkthqfemokh0tv0; G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; nTalk_CACHE_DATA={uid:kf_10279_ISME9754_guest198E67AC-C852-3A,tid:1536302889563485}; nTalk_PAGE_MANAGE={|m|:[{|90230|:|029078|}],|t|:|14:48:27|}'
}

request = Request(url, headers=headers)
response = urlopen(request)

print(response.read().decode())