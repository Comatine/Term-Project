import flet as ft
from Flet_Asset import Asset
from Service import Crawler, Search, Sort
from dotenv import load_dotenv

load_dotenv()

def main(page: ft.Page):

    # ----------------------------------------
    # Initalize
    # ----------------------------------------

    page.title = "⚔️Dekaron Crafting Item Table🛠️"
    page.window_width = 800
    page.window_height = 600
    page.padding = 0

    inital_page = Asset.initalization()

    page.add(
        inital_page
    )
    page.update()

    # ----------------------------------------
    # Basic Variables
    # ----------------------------------------

    # 탭 부분

    Tabs = {
        "User" : Asset.Controls["UserTab"].current,
        "Search" : Asset.Controls["SearchTab"].current,
        "Detail" : Asset.Controls["DetailTab"].current,
    }

    # 사용자 부분

    User = {
        "IDBar" : Asset.Controls["IDBar"].current,
        "PasswordBar" : Asset.Controls["PasswordBar"].current,
        "LoginButton" : Asset.Controls["LoginButton"].current,
        "RegisterButton" : Asset.Controls["RegisterButton"].current
    }

    # 검색창 부분

    search_input = Asset.Controls["SearchBar"].current
    search_button = Asset.Controls["SearchButton"].current

    results_view = Asset.Controls["Results"].current

    # ----------------------------------------
    # Event Functions
    # ----------------------------------------

    def on_login_click(evnet):
        page.update()

    def on_register_click(evnet):
        page.update()

    def on_close_click(event):
        Asset.close_detail()
        page.update()

    async def on_detail_click(event):
        item_id = event.control.data["Item_Id"]
        item_name = event.control.data["Item_Name"]
        
        Asset.set_up_detail("아이템 정보")
        page.update() 
        
        # 동기 크롤러를 스레드 풀에서 실행하여 UI가 굳는 현상 방지
        import asyncio
        item_info = await asyncio.to_thread(Crawler.get_item_description, item_id)
        
        close_btn = Asset.build_item_detail(item_id, item_name, item_info)
        close_btn.on_click = on_close_click

        page.update()  

    def on_search_click(e):
        results_view.controls.clear()
        keyword = search_input.value
        
        raw_results = Search.process_search_request(keyword)
        sorted_results = Sort.sort_items_by_id(raw_results)

        if not sorted_results:
            results_view.controls.append(ft.Text("결과가 없습니다.", color=ft.Colors.RED))
        else:
            for item_id, item_name in sorted_results:
                detail_btn = Asset.build_item_card(item_id, item_name)
                detail_btn.content.content.controls[2].content.on_click = on_detail_click
                results_view.controls.append(detail_btn)
            
        page.update()

    # ----------------------------------------
    # Connect Event Listener
    # ----------------------------------------

    search_button.on_click = on_search_click

    User["LoginButton"].on_click = on_login_click
    User["RegisterButton"].on_click = on_register_click


if __name__ == "__main__":
    ft.app(target=main)