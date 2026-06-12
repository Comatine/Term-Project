import pandas as pd
from .connection import get_connection

class Item:
    
    @staticmethod
    def get_item_by_name(keyword: str):
        conn = get_connection()
        query = "SELECT Item_Id, Item_Name FROM Item WHERE Item_Name LIKE ?"
        
        # 1. Pandas DataFrame으로 결과 반환
        df = conn.execute(query, ["%" + keyword + "%"]).df()
        conn.close()
        
        # 2. 딕셔너리로 변환 후 이전 코드와 동일한 튜플 리스트로 재구성
        dict_list = df.to_dict('records')
        return [(row['Item_Id'], row['Item_Name']) for row in dict_list]
    
    @staticmethod
    def get_obtain_paths(item_id: int) -> list:
        """아이템의 획득 경로(Obtain_Type) 목록을 조회합니다."""
        conn = get_connection()
        query = "SELECT Obtain_Type FROM Obtainable_Item WHERE Obtainable_Item_Id = ?"
        
        df = conn.execute(query, [item_id]).df()
        conn.close()
        
        dict_list = df.to_dict('records')
        return [row['Obtain_Type'] for row in dict_list]

    @staticmethod
    def get_drop_info(item_id: int) -> list:
        """아이템이 'Droppable'일 경우 드랍되는 맵과 몬스터 정보를 조회합니다."""
        conn = get_connection()
        query = """
            SELECT L.Location_Name, M.Monster_Name
            FROM Drop_Item D
            JOIN Monster M ON D.Monster_Id = M.Monster_Id AND D.Location_Id = M.Location_Id
            JOIN Location L ON D.Location_Id = L.Location_Id
            WHERE D.Obtainable_Item_Id = ?
        """
        df = conn.execute(query, [item_id]).df()
        conn.close()
        
        dict_list = df.to_dict('records')
        return [(row['Location_Name'], row['Monster_Name']) for row in dict_list]
    
    @staticmethod
    def get_craft_info(item_id: int) -> list:
        """아이템이 제작 아이템인지 확인하고, 속한 제작 시리즈(Craft_Name)와 단계, 제작 경로(Craft_Type)를 반환합니다."""
        conn = get_connection()
        query = "SELECT Craft_Name, Craft_Progress, Craft_Type FROM Craftable_Item WHERE Craftable_Item_Id = ?"
        
        df = conn.execute(query, [item_id]).df()
        conn.close()
        
        dict_list = df.to_dict('records')
        return [(row['Craft_Name'], row['Craft_Progress'], row['Craft_Type']) for row in dict_list]

    @staticmethod
    def get_craft_materials(craft_name: str, item_id: int) -> list:
        """특정 제작 아이템의 필요 재료 이름과 수량, 아이디를 조회합니다."""
        conn = get_connection()
        query = """
            SELECT I.Item_Name, CM.Material_Amount, CM.Material_Item_Id
            FROM Craft_Materials CM
            JOIN Item I ON CM.Material_Item_Id = I.Item_Id
            WHERE CM.Craft_Name = ? AND CM.Craftable_Item_Id = ?
        """
        df = conn.execute(query, [craft_name, item_id]).df()
        conn.close()
        
        dict_list = df.to_dict('records')
        return [(row['Item_Name'], row['Material_Amount'], row['Material_Item_Id']) for row in dict_list]

    @staticmethod
    def get_craft_series(craft_name: str) -> list:
        """제작 시리즈(Craft_Name)에 속한 모든 아이템을 단계(Progress) 오름차순으로 조회합니다."""
        conn = get_connection()
        query = """
            SELECT CI.Craft_Progress, I.Item_Id, I.Item_Name
            FROM Craftable_Item CI
            JOIN Item I ON CI.Craftable_Item_Id = I.Item_Id
            WHERE CI.Craft_Name = ?
            ORDER BY CI.Craft_Progress ASC
        """
        df = conn.execute(query, [craft_name]).df()
        conn.close()
        
        dict_list = df.to_dict('records')
        return [(row['Craft_Progress'], row['Item_Id'], row['Item_Name']) for row in dict_list]