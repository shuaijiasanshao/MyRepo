import wsgi
from image import ControllerImage
from test import ControllerTest


class API(wsgi.Router):

    def __init__(self,mapper):
        controller_test = ControllerTest()
        controller_image = ControllerImage()

        mapper.connect('/test',
                       controller=wsgi.Resource(controller_test),
                       action='test',
                       conditions={'method': ['GET']})
        
        mapper.connect('/image/1',
                       controller=wsgi.Resource(controller_image),
                       action='test',
                       conditions={'method': ['GET']})

        super(API, self).__init__(mapper)
    
