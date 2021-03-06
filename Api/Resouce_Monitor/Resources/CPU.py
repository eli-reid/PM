from typing import Iterable
import psutil
import platform

class CPU:

    @property
    def type(self) -> str: 
        return platform.processor()
    
    @property
    def p_cores(self) -> int:
        return psutil.cpu_count(logical=False)

    @property
    def t_cores(self): 
        return psutil.cpu_count(logical=True)
    
    @property 
    def max_freq(self):
        return psutil.cpu_freq().max
    
    @property
    def min_freq(self):
        return psutil.cpu_freq().min

    @property
    def current_freq(self): 
        return psutil.cpu_freq().current
    
    @property
    def percent(self) -> float:
        return psutil.cpu_percent()

    @property
    def temps(self):
        return psutil.sensors_temperatures() \
            if hasattr(psutil, 'sensors_temperatures') else {}

    @property
    def stats(self):
        return psutil.cpu_stats() 

    def __dict__(self):
        all: dict={}
        for item in self.__dir__():
            if not item.startswith('__'):
                all[item]=self.__getattribute__(item)
        return all


 