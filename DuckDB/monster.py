from .connection import get_connection

def get_monster_by_id(monster_id: int):
    conn = get_connection()
    query = "SELECT Monster_Id, Location_Id, Monster_Name FROM Monster WHERE Monster_Id = ?"
    result = conn.execute(query, [monster_id]).fetchall()
    conn.close()
    return result