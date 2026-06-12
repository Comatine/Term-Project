from DuckDB import Item

class Search:
    
    @staticmethod
    def process_search_request(keyword: str):
        if not keyword.strip():
            return []
        return Item.get_item_by_name(keyword.strip())
    
    @staticmethod
    def get_item_obtain_paths(item_id: int) -> list:
        """Asset.py의 요청을 받아 아이템 획득 경로를 반환합니다."""
        return Item.get_obtain_paths(item_id)
    
    @staticmethod
    def get_item_drop_info(item_id: int) -> list:
        """Asset.py의 요청을 받아 아이템 드랍 정보를 반환합니다."""
        return Item.get_drop_info(item_id)
    
    @staticmethod
    def get_craft_info(item_id: int) -> list:
        return Item.get_craft_info(item_id)

    @staticmethod
    def get_craft_materials(craft_name: str, item_id: int) -> list:
        return Item.get_craft_materials(craft_name, item_id)

    @staticmethod
    def get_craft_series(craft_name: str) -> list:
        return Item.get_craft_series(craft_name)