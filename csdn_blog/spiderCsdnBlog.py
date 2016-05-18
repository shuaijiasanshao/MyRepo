# _*_ coding:utf-8 _*_
from pyquery import PyQuery as pq
import urllib2
from mongodb import Mongodb
from file import File


# csdn不让直接解析，会403,所以伪造了http请求头
class GetCsdnBlog(object):
    """docstring for get_csdn_blog_info"""
    def __init__(self, entry_url, prefix_url):
        super(GetCsdnBlog, self).__init__()
        self.url = entry_url
        self.prefix_url = prefix_url

    def _generate_dict(self, blog_name, blog_url):
        blog = {"blog_name": blog_name, "blog_url": blog_url}
        return blog

    def save_data_2_db(self, blog_list):
        host = 'localhost'
        port = 27017
        db_name = 'mydb'
        collection_name = 'my_blog'
        db = Mongodb(host, port, db_name, collection_name)
        db.delete_data()
        for blog in blog_list:
            db.insert_data(blog)

    def save_data_2_file(self, blog_list, file_name='blog_info',):
        file = File()
        file_write_file = file.opne_file(file_name, "w")
        for blog in blog_list:
            content = blog['blog_name'] + '------' + blog['blog_url'] + '\n'
            file.save_file(file_write_file, file_name, content)
        file_write_file.close()

    def _get_next_page(self, response):
        doc = pq(response)
        page_list = doc('.pagelist').find('a')
        flag = 0
        for item in page_list:
            if item.text == '下一页':
                url = self.prefix_url + item.get('href')
                flag = 1
        if flag == 0:
            url = None
        return url

    def _get_blog_detail(self, response):
        doc = pq(response)
        info = doc('.link_title')
        blog_list = []
        for i in info.items('a'):
            blog = self._generate_dict(i.text(), self.prefix_url + i('a').attr('href'))
            blog_list.append(blog)
        return blog_list

    def _send_request(self, url):
        head_req = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64'}
        req = urllib2.Request(url, headers=head_req)
        return urllib2.urlopen(req).read().decode('utf-8')

    def get_my_blog(self):
        blog_list = []
        while self.url:
            response = self._send_request(self.url)
            self.url = self._get_next_page(response)
            blog_list += self._get_blog_detail(response)
        self.save_data_2_db(blog_list)
        self.save_data_2_file(blog_list)
