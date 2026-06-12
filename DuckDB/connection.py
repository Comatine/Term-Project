import duckdb
import os
from dotenv import load_dotenv
from .interface import DBInterface

load_dotenv()

class DuckDBConnection(DBInterface):
    def connect(self):
        db_path = os.getenv("DUCKDB_PATH", "Data/ItemTable.db")
        return duckdb.connect(db_path)
        
    def close(self):
        pass 

def get_connection():
    return DuckDBConnection().connect()