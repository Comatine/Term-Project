from abc import ABC, abstractmethod

class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
        
    @abstractmethod
    def close(self):
        pass