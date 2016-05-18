# coding:utf-8
import time
import urllib2
from mongodb import Mongodb
from file import File


class AutoUpdaPage(object):
    """docstring for AutoUpdaPage"""
    def __init__(self):
        super(AutoUpdaPage, self).__init__()
        host = 'localhost'
        port = 27017
        db_name = 'mydb'
        collection_blog = 'my_blog'
        collection_proxy = 'free_proxy'
        self.mongodb_blog = Mongodb(host, port, db_name, collection_blog)
        self.mongodb_proxy = Mongodb(host, port, db_name, collection_proxy)

    def _get_data_form_db(self, db):
        data_list = []
        blog_obj = db.query_data()
        for blog in blog_obj:
            data_list.append(blog)
        return data_list

    def _get_blog_from_file(self, file_name='blog_info'):
        file = File()
        blog = file.read_file(file_name)
        return blog

    def auto_update_page(self):
        # blog_list = self._get_blog_from_file(file_name='blog_info')
        # blog_list = self._get_data_form_db(self.mongodb_blog)

        head_req = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64'}
        j = 0
        max_count = 8000
        while True:
            for blog in blog_list:
                try:
                    req = urllib2.Request(blog['blog_url'], headers=head_req)
                    urllib2.urlopen(req)
                    j += 1
                    print('%d %s %s' % (j, blog['blog_name'], blog['blog_url']))
                    if j >= max_count:
                        break
                    # import random
                    # sleep_time = random.randint(3, 6)
                    # print("sleep-------", sleep_time, "s")
                    time.sleep(5)
                except urllib2.HTTPError, e:
                    print('urllib2.HTTPError', e.code)
                    time.sleep(5)
                except urllib2.URLError, e:
                    print('urllib2.URLError', e.reason)
                    time.sleep(5)
                    time.sleep(0.1)
            if j >= max_count:
                break


def main():
    updatepage = AutoUpdaPage()
    updatepage.auto_update_page()

if __name__ == '__main__':
    main()
