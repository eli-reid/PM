import json
from flask.helpers import get_template_attribute
from flask_socketio import emit
from . import CPU
from . import Memory
from . import Disk
from . import Network
from . import Processes
from datetime import time

class Resources:
    
    def __init__(self) -> None:
        self.__CPU = CPU()
        self.__memory = Memory()
        self.__disk = Disk()
        self.__network = Network()
        self.__processes = Processes()

    @property
    def CPU(self) -> CPU:
        return self.__CPU
    
    @property
    def memory(self) -> Memory:
        return self.__memory
    
    @property
    def disk(self):
        return self.__disk
    
    @property
    def network(self) -> Network:
        return self.__network
    
    @property
    def processes(self) -> Processes:
        return self.__processes


    @property
    def get_all(self) -> dict:
        t = self.CPU.__dict__()
        return t
        return {
            'cpu' : self.CPU.get_all
        }
    



