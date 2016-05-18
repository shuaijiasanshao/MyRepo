from spiderCsdnBlog import GetCsdnBlog
from autoUpdatePage import AutoUpdaPage


def main():
    entry_url = 'your CSDN blog URL'
    prefix_url = 'http://blog.csdn.net'
    spider = GetCsdnBlog(entry_url, prefix_url)
    auto_update = AutoUpdaPage()
    spider.get_my_blog()
    auto_update.auto_update_page()

if __name__ == '__main__':
    main()
