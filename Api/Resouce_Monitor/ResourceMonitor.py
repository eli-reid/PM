import sqlite3

from psutil import cpu_percent
from .RmThread import RmThread
from .Resources import Resources
from time import sleep
from datetime import datetime
import json

class ResourceMonitor:
    
    def __init__(self, DB_Name:str="ResourceMonitor.db") -> None:
        self.__db = DB_Name
        self.__thread = RmThread(target=self.log)
        self.resources = Resources()
        self.__Build_table()
        self.__kill: bool = False
    
    def log(self) -> None:
        while not self.__kill:
            db = sqlite3.connect(self.__db)
            q = f"""INSERT INTO {self.__thread.name}
                                    (TIME, DATA)
                                    VALUES (?,?);"""
            
            db.execute(q,[datetime.now(),str(self.resources.CPU.cpu_percent)])
            db.commit()
            db.close()
            sleep(self.__thread.id+1)

    def __Build_table(self) -> None:
        db = sqlite3.connect(self.__db)
        cursor = db.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.__thread.name}(
                        ID      INTEGER PRIMARY KEY AUTOINCREMENT,
                        TIME    DATETIME            NOT NULL,
                        DATA    JSON              NOT NULL
                        );""")
        db.close
    
    def start(self) -> None:
        self.__kill  = False
        self.__thread.start()
    
    def stop(self):
        self.__kill = True
    
    @property
    def getThreads(self):
        return RmThread._threads
        



       

