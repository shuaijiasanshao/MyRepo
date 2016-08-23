##仿openstack Restful风格实现<br>

##环境<br>
Ubuntu14.04<br>
Python2.7<br>
PasteDeploy<br>
oslo.config<br>
wsgi<br>
evenlet<br>
....<br>

##说明
server.py 读取配置，启动app<br>
server_api.ini 发现和配置WSGI<br>
server_config.conf 服务器配置文件<br>
test.py 包含app的文件<br>
v1/router.py 路由，定义连接和app的映射<br>
v1/wsgi.py   负责请求的分发<br>
v1/image.py  app<br>
v1/test.py   app<br>

