from wsgiref.simple_server import make_server

from SzDjango import SzObject

from route import Route

class Server(SzObject):
    def __init__(self):
        super().__init__()
        if not self.__server:
            self.__server = make_server('',port=80,self.__start)
    
    def __start(self):
        f" SzDjango web framework start.... "

    def run(self, parameter_list):
        self.__server.serve_forever()
        pass
