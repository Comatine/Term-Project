from .connection import get_connection

def register_user(user_name: str, user_password: str):
    conn = get_connection()
    query = "INSERT INTO Dekaron_User (User_Name, User_Password) VALUES (?, ?)"
    conn.execute(query, [user_name, user_password])
    conn.close()

def login_user(user_name: str, user_password: str):
    conn = get_connection()
    query = "SELECT User_Id FROM Dekaron_User WHERE User_Name = ? AND User_Password = ?"
    result = conn.execute(query, [user_name, user_password]).fetchone()
    conn.close()
    return result