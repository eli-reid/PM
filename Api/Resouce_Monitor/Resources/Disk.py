import psutil
import platform
from os import path

class Disk:

    @property
    def io(self):
        return psutil.disk_io_counters()
   
    @property
    def partitions(self):
        data: list[dict] = []
        for item in psutil.disk_partitions():
                data.append(
                {
                "device" : item.device,
                "mount" : item.mountpoint,
                "filesystem" : item.fstype,
                "maxfile": item.maxfile,
                "maxpath" : item.maxpath,
                "opt" : item.opts
                } )
          
        return data


    @property
    def usage(self):
        return psutil.disk_usage(path="c:\\")
    
    def get(self):
        all: dict={}
        for item in psutil.__all__:
            if not item.startswith('__'):
                try:
                    value = psutil.__dict__[item]
                    if value:
                        all[item]=type(value)
                except Exception as e:
                    e=e
                    pass
        return all
