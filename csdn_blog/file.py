# import sys 
# reload(sys)
# sys.setdefaultencoding('utf-8')


class File(object):
    """docstring for File"""
    def __init__(self, ):
        super(File, self).__init__()

    def _generate_blog(self, blog_name, blog_url):
        blog = dict()
        blog['blog_name'] = blog_name
        blog['blog_url'] = blog_url
        return blog

    def opne_file(self, file_name, mode):
        file_object = open(file_name, mode)
        return file_object

    def close_file(self, file_object):
        file_object.close()

    def read_file(self, file_name):
        file_object = open(file_name)
        blog_list = []
        for line in file_object:
            line = line.split("------")
            blog = self._generate_blog(line[0], line[1])
            blog_list.append(blog)
        file_object.close()
        return blog_list

    def save_file(self, file_object, file_name, content):
        content.encode('utf-8')
        file_object.write(content)
