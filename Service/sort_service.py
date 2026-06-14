class Sort:
    def sort_items_by_id(item_list: list) -> list:
        if not item_list:
            return []
        return sorted(item_list, key=lambda x: x[0])

    def sort_items_by_name(item_list: list) -> list:
        if not item_list:
            return []
        return sorted(item_list, key=lambda x: x[1])

    def sort_items_descending(item_list: list, by_id: bool = True) -> list:
        if not item_list:
            return []
        index = 0 if by_id else 1
        return sorted(item_list, key=lambda x: x[index], reverse=True)
    
    def sort_item_base_info(item_info: list) -> str:
        base_info_section = next(section for section in item_info['sections'] if section['title'] == '기본 정보')
        attributes = base_info_section['attributes']

        formatted_parts = []

        for attr in attributes:
            key = attr['key']
            value = attr['value']
            
            if key == '요구레벨':
                key = '요구 레벨'
                value = f"{value}Lvl"
                
            formatted_parts.append(f"[ {key} ] {value}")

        result = " || ".join(formatted_parts)

        return result
    
    @staticmethod
    def extract_additional_options(item_info: dict) -> dict:
        """
        item_info 딕셔너리의 'sections' 구조를 순회하여
        '추가 옵션'의 attributes 리스트를 {키: 값} 딕셔너리 형태로 반환합니다.
        """
        # 방어적 코드: item_info가 딕셔너리가 아니거나 'sections' 키가 없으면 빈 딕셔너리 반환
        if not isinstance(item_info, dict) or "sections" not in item_info:
            return {}

        # sections 리스트를 순회하며 '추가 옵션' 섹션 탐색
        for section in item_info.get("sections", []):
            if section.get("title") == "추가 옵션":
                attributes = section.get("attributes", [])
                # [{'key': '힘', 'value': '140'}, ...] 형태의 리스트를
                # {'힘': '140', '민첩': '140', ...} 형태의 직관적인 딕셔너리로 변환하여 반환
                return {attr.get("key"): attr.get("value") for attr in attributes if "key" in attr and "value" in attr}
                
        return {}

    @staticmethod
    def format_drop_info(drop_data: list) -> dict:
        """[(Map, Monster), ...] 형태의 데이터를 맵 기준으로 묶어줍니다."""
        drop_dict = {}
        for loc_name, mon_name in drop_data:
            if loc_name not in drop_dict:
                drop_dict[loc_name] = []
            drop_dict[loc_name].append(mon_name)
        return drop_dict
    