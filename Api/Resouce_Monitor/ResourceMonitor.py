
import sqlite3
from .RmThread import RmThread
from .Resources import Resources
from time import sleep
from datetime import datetime, timedelta

class ResourceMonitor:
    """ Resource Monitor - creates new thread for logging system reources!
        log_file: if is None database stores in memory 
        log_size in MB 

    """
    def __init__(self, log_file: str=None, log_size: int=50,) -> None:
        self.__log_file: str = ":memory:" if log_file is None else log_file
        self.__log_size: int = log_size * 1000000 # convert bytes to MB
        self.__thread: RmThread = RmThread(target=self.__log)
        self.__resources: Resources = Resources()
        self.__dbcon = sqlite3.connect(self.__log_file, check_same_thread=False)
        self.__kill: bool = False
        self.__Build_table()

    def __log(self) -> None:
        __LOG_SQL_INSERT_STR: str = f"INSERT INTO {self.__thread.name} (TIME, CPU_U, MEM_U) VALUES (?,?,?);"
        __LOG_SQL_DELETE_STR: str = f"DELETE FROM {self.__thread.name} WHERE TIME < ?"

        while not self.__kill: 
            try:
                size = self.__dbcon.execute('PRAGMA page_size;').fetchone()[0] * self.__dbcon.execute('PRAGMA page_count').fetchone()[0]
                if  size > self.__log_size : 
                    t: int = datetime.now().timestamp() - timedelta(days=10).seconds
                    self.__dbcon.execute(__LOG_SQL_DELETE_STR, [t])
                    self.__dbcon.commit()
                self.__dbcon.execute(__LOG_SQL_INSERT_STR, [datetime.now().timestamp(), self.__resources.CPU.percent, self.__resources.memory.percent])
                self.__dbcon.commit()
                sleep(.001)
            except Exception as e:
                pass

    def __Build_table(self) -> None:
        self.__dbcon.execute(f"CREATE TABLE IF NOT EXISTS {self.__thread.name}(\
                        TIME   INTEGER PRIMARY KEY,\
                        CPU_U   INTEGER,\
                        MEM_U   INTEGER\
                        )WITHOUT ROWID;")
       
    def start(self) -> None:
        self.__kill  = False
        self.__thread.start()
    
    def stop(self) -> None:
        self.__kill = True

    @property
    def getThreads(self) -> list:
        return self.__thread.threads