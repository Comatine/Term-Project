from .connection import get_connection

class User:
    def login(username, password):
        """DB에서 유저 정보를 확인하고 (User_Id, User_Name)을 반환합니다."""
        conn = get_connection()
        query = "SELECT User_Id, User_Name FROM Dekaron_User WHERE User_Name = ? AND User_Password = ?"
        # pandas를 거쳐 딕셔너리로 변환
        result = conn.execute(query, [username, password]).df().to_dict('records')
        conn.close()
        
        if result:
            return result[0]['User_Id'], result[0]['User_Name']
        return None, None

    @staticmethod
    def register(username, password):
        """회원가입을 진행합니다. 이미 존재하는 아이디면 False를 반환합니다."""
        conn = get_connection()
        check_query = "SELECT User_Id FROM Dekaron_User WHERE User_Name = ?"
        exists = conn.execute(check_query, [username]).df().to_dict('records')
        
        if exists:
            conn.close()
            return False
            
        insert_query = "INSERT INTO Dekaron_User (User_Name, User_Password) VALUES (?, ?)"
        conn.execute(insert_query, [username, password])
        conn.close()
        return True

    @staticmethod
    def get_favorite_pins(user_id):
        """유저의 찜 목록을 이름(Pin_Name) 오름차순으로 가져옵니다."""
        conn = get_connection()
        query = "SELECT Pin_Id, Pin_Name FROM Favorite_Pin WHERE User_Id = ? ORDER BY Pin_Name ASC"
        result = conn.execute(query, [user_id]).df().to_dict('records')
        conn.close()
        return result
    
    @staticmethod
    def create_favorite_pin(user_id: int, pin_name: str) -> int:
        """새로운 찜 목록을 생성하고 생성된 Pin_Id를 반환합니다."""
        conn = get_connection()
        
        # INSERT 문에서 RETURNING을 사용하여 새로 발급된 Pin_Id를 바로 가져옵니다.
        query = "INSERT INTO Favorite_Pin (User_Id, Pin_Name) VALUES (?, ?) RETURNING Pin_Id"
        
        # Pandas 변환 규칙 준수
        result = conn.execute(query, [user_id, pin_name]).df().to_dict('records')
        conn.close()
        
        # 새로 생성된 Pin_Id 반환 (실패 시 None)
        return result[0]['Pin_Id'] if result else None

    @staticmethod
    def check_item_in_pin(pin_id: int, user_id: int, item_id: int) -> bool:
        """해당 아이템이 특정 찜 목록에 이미 존재하는지 중복 검사합니다."""
        conn = get_connection()
        
        query = """
            SELECT 1 
            FROM Pin_Data 
            WHERE Pin_Id = ? AND User_Id = ? AND Craftable_Item_Id = ?
        """
        
        # Pandas 변환 규칙 준수
        result = conn.execute(query, [pin_id, user_id, item_id]).df().to_dict('records')
        conn.close()
        
        # 조회된 데이터가 있으면 True 반환
        return len(result) > 0

    @staticmethod
    def add_item_to_pin(pin_id: int, user_id: int, item_id: int):
        """찜 목록에 아이템을 추가합니다."""
        conn = get_connection()
        
        # Pin_Data 테이블은 Craft_Name이 필수이므로, 
        # Craftable_Item 테이블에서 Craft_Name을 찾아 함께 INSERT 하는 서브쿼리 방식을 사용합니다.
        query = """
            INSERT INTO Pin_Data (Pin_Id, User_Id, Craft_Name, Craftable_Item_Id)
            SELECT ?, ?, Craft_Name, Craftable_Item_Id
            FROM Craftable_Item
            WHERE Craftable_Item_Id = ?
        """
        
        conn.execute(query, [pin_id, user_id, item_id])
        conn.close()

        # DuckDB/user.py 추가 코드 (User 클래스 내부)

    @staticmethod
    def get_pinned_items(pin_id: int, user_id: int) -> list:
        """찜 목록에 담긴 목표 제작 아이템들의 이름과 ID를 조회합니다."""
        conn = get_connection()
        query = """
            SELECT I.Item_Name, I.Item_Id
            FROM Pin_Data PD
            JOIN Item I ON PD.Craftable_Item_Id = I.Item_Id
            WHERE PD.Pin_Id = ? AND PD.User_Id = ?
        """
        df = conn.execute(query, [pin_id, user_id]).df()
        conn.close()
        
        result_dicts = df.to_dict('records')
        return [(row['Item_Name'], row['Item_Id']) for row in result_dicts] if result_dicts else []

    @staticmethod
    def get_pin_materials_summary(pin_id: int, user_id: int) -> list:
        """찜 목록에 담긴 아이템들을 제작하기 위한 모든 재료의 총합을 계산합니다."""
        conn = get_connection()
        query = """
            SELECT I.Item_Name, I.Item_Id, SUM(CM.Material_Amount) as Total_Amount
            FROM Pin_Data PD
            JOIN Craft_Materials CM ON PD.Craft_Name = CM.Craft_Name AND PD.Craftable_Item_Id = CM.Craftable_Item_Id
            JOIN Item I ON CM.Material_Item_Id = I.Item_Id
            WHERE PD.Pin_Id = ? AND PD.User_Id = ?
            GROUP BY I.Item_Name, I.Item_Id
            ORDER BY Total_Amount DESC
        """
        df = conn.execute(query, [pin_id, user_id]).df()
        conn.close()
        
        result_dicts = df.to_dict('records')
        return [(row['Item_Name'], row['Item_Id'], row['Total_Amount']) for row in result_dicts] if result_dicts else []