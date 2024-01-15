import random

class UserAgentMiddleware:

    user_agent_list = [
        # Chrome
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        # Firefox
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 "
        "Firefox/87.0",
        # Edge
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76",
        # Safari
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    ]
    
    def process_request(self, request, spider):
        options = request.meta['options']

        user_agent = random.choice(self.user_agent_list)
        options.add_argument(f'--user-agent={user_agent}')

        request.meta['settings'] = options