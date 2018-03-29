from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # 项目标题：<h1 class="firth-tit">德阳高新区万福棚户区改造项目（一期）监理招标</h1>
        title_node = soup.find('h1', class_="firth-tit")
        res_data['title'] = title_node.get_text()
        # 项目编号：<span id="ctl00_ContentPlaceHolder1_lbNoticeNum">DYGC（2018）0074</span>
        projnumber_node = soup.find('span',class_="ctl00_ContentPlaceHolder1_lbNoticeNum")
        res_data['projnumber'] = projnumber_node.get_text()
        
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data