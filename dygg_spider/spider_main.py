# 总调度程序
from dygg_spider import url_manager, html_dowloader, html_parser, html_outputer
class SpiderMain(object)
    def __init__(self):
        # url管理器
        self.urls = url_manager.Url_Manager()
        # html下载器
        self.dowloader = html_downloader.Html_Downloader()
        # html解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 如果有url就取一个url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 下载url对应的页面
                html_cont = self.dowloader.download(new_url)
                # 进行页面解析,并得到新的url和数据
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                # 将新的url补充进url管理器
                self.urls.add_new_urls(new_urls)
                # 进行数据收集
                self.outputer.collect_data(new_data)

                if count == 1000
                    break
                count = coun + 1
            
            except:
                print('craw failed ')
        

        self.outputer.output_html()

if __name__=="__main__"
    root_url = "http://www.dyggzy.com/articleInfo_b06e5e4991a34d0bb159ac0020fd290e.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)