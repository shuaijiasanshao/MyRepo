class ControllerImage(object):

    def __init__(self):
        print "ControllerImage!!!!"

    def test(self,req):
        print "req",req
        return {
            'name': "image",
            'properties': "image"
        }