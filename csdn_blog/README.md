## 环境
Ubuntu14.04<br>
Python2.7<br>
PyQuery<br>
PyMongo<br>

## 说明
一个自动爬取CSDN博客刷访问量的系统．<br>
系统首先自动爬取你的CSDN所有博客保存，然后一篇一篇的访问刷新，<br>
可以使用mongodb存博客信息，也可以将博客信息写在文件中．<br>
main.py是程序的入口．<br>
spiderCsdnBlog.py：用来爬取解析并存储博客的模块．<br>
autoUpdatePage.py：用来读取博客信息并访问的模块．<br>
file.py：文件操作．<br>
mongodb.py：mongodb数据库操作．<br>
