from os import rmdir
import threading
from typing import TypedDict      

class _thread(TypedDict):
    id:int
    name:str
    thread: threading.Thread

class RmThread(threading.Thread):

    _threads: list = []
    
    def __init__(self, name: str="ResourceMonitor", **kwargs) -> None:
        super().__init__(**kwargs)
        self.id: int = self.__get_next_id
        self.name: str = self.__get_unique_name(id=self.id, name=name)    
        RmThread._threads.append(_thread(id=self.id, name=self.name, thread=self))
        
    def __get_unique_name(self, id: int, name: str) -> str:
        for item in self._threads:
            if name in item.values():
                return f"{name}_{id}"
        return name

    @property
    def __get_next_id(self) -> int:
        if len(self._threads) < 1:
            return 0
        return self._threads[-1]['id'] + 1