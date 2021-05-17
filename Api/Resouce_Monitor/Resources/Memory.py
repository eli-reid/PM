import psutil
import platform

class Memory:

    @property
    def percent(self) -> float:
       return psutil.virtual_memory().percent

    @property
    def total(self):
        return psutil.virtual_memory().total

    @property
    def used(self):
        psutil.swap_memory().percent
        return  psutil.virtual_memory().used


        
    