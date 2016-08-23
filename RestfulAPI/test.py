import commands


class Show(object):
    """docstring for Show"""
    def __init__(self):
        super(Show, self).__init__()

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["welcome to use it!"]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in Show.factory", global_conf, kwargs
        return Show()


class Hello(object):
    """docstring for Hello"""
    def __init__(self):
        super(Hello, self).__init__()

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Hello, nice to meet you"]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in Hello.factory", global_conf, kwargs
        return Hello()


class Goodbye(object):
    """docstring for Hello"""
    def __init__(self):
        super(Goodbye, self).__init__()

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Goodbye, may we meet again"]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in Goodbye.factory", global_conf, kwargs
        return Goodbye()


class Free(object):
    """docstring for Hello"""
    def __init__(self):
        super(Free, self).__init__()

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        result = commands.getstatusoutput('free')
        return [str(result[1])]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in Free.factory", global_conf, kwargs
        return Free()