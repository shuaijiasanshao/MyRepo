class ControllerTest(object):

    def __init__(self):
        print "ControllerTest!!!!"

    def test(self,req):
        print "req",req
        return {
            'name': "test",
            'properties': "test"
        }
