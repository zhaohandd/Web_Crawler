from tupian.settings import USER_AGENTS
from random import choice
from fake_useragent import UserAgent


class UserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        # print(choice(USER_AGENTS))
        # request.headers.setdefault(b'User-Agent', choice(USER_AGENTS))
        request.headers.setdefault(b'User-Agent', UserAgent().random)