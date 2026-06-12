from .connection import get_connection

def get_location_by_id(location_id: int):
    conn = get_connection()
    query = "SELECT Location_Id, Location_Type, Location_Name, Location_Level FROM Location WHERE Location_Id = ?"
    result = conn.execute(query, [location_id]).fetchall()
    conn.close()
    return result