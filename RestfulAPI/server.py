import os
from paste.deploy import loadapp
from oslo_config import cfg
from wsgiref.simple_server import make_server
import eventlet
from eventlet import wsgi


server_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.IntOpt('bind_port',
               default=9292,
               help='Port number to listen on.')
]
CONF = cfg.CONF
CONF.register_opts(server_opts)
CONF(default_config_files=['server_config.conf'])


def main():
    configfile = "server-api.ini"
    appname = "rootApp"
    
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
#     print CONF.bind_host, CONF.bind_port
    
    wsgi.server(eventlet.listen((CONF.bind_host, CONF.bind_port)), wsgi_app)
#     server = make_server(CONF.bind_host, CONF.bind_port, wsgi_app)
#     server.serve_forever()

if __name__ == '__main__':
    main()
