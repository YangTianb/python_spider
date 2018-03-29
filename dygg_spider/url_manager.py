class UrlManager(object):

    def __init__(sef):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加一个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    # 是否有新的
    def has_new_url(self):
        return len(self.new_urls) != 0
    # 获取一个新的
    def get_new_url():
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    