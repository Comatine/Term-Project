from DuckDB import Item, User

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
    
    @staticmethod
    def get_pinned_items(pin_id: int, user_id: int) -> list:
        """찜 목록의 아이템들을 반환합니다."""
        return User.get_pinned_items(pin_id, user_id)

    @staticmethod
    def get_pin_materials_summary(pin_id: int, user_id: int) -> list:
        """찜 목록 아이템 제작에 필요한 재료 총합을 반환합니다."""
        return User.get_pin_materials_summary(pin_id, user_id)