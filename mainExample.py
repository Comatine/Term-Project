# ver 1.0 (AI를 활용한 초기 구성)

# import flet as ft
# from Flet_Asset import Asset
# from Service import Crawler, Search, Sort
# from dotenv import load_dotenv

# load_dotenv()

# def main(page: ft.Page):
#     page.title = "⚔️Dekaron Crafting Item Table🛠️"
#     page.window_width = 800
#     page.window_height = 600
#     page.padding = 20
    
#     search_input = ft.TextField(label="검색어 입력", expand=True, border_radius=ft.BorderRadius.all(10), border_color=ft.Colors.GREY_600)
#     results_view = ft.ListView(expand=True, spacing=10)

#     # 상호작용

#     def on_search_click(e):
#         results_view.controls.clear()
#         keyword = search_input.value
        
#         raw_results = Search.process_search_request(keyword)
#         sorted_results = Sort.sort_items_by_id(raw_results)
        
#         if not sorted_results:
#             results_view.controls.append(ft.Text("결과가 없습니다.", color=ft.Colors.RED))
#         else:
#             for item_id, item_name in sorted_results:
#                 results_view.controls.append(Asset.build_item_card(item_id, item_name))
            
#         page.update()

#     search_btn = ft.ElevatedButton("검색", on_click=on_search_click)

#     page.add(
#         ft.Row([search_input, search_btn]),
#         ft.Divider(height=20, color="transparent"),
#         results_view
#     )

# Ver 2.0 (하드코딩 버전)

# if __name__ == "__main__":
#     ft.app(target=main)

# import flet as ft
# from Flet_Asset import Asset
# from Service import Crawler, Search, Sort
# from dotenv import load_dotenv

# load_dotenv()

# def main(page: ft.Page):

#     # ----------------------------------------
#     # Initalize
#     # ----------------------------------------

#     page.title = "⚔️Dekaron Crafting Item Table🛠️"
#     page.window_width = 800
#     page.window_height = 600
#     page.padding = 0

#     inital_page = Asset.initalization()

#     page.add(
#         inital_page
#     )
#     page.update()

#     # ----------------------------------------
#     # Basic Variables
#     # ----------------------------------------

#     search_input = Asset.Controls["SearchBar"].current
#     search_button = Asset.Controls["SearchButton"].current

#     results_view = Asset.Controls["Results"].current

#     # ----------------------------------------
#     # Event Functions
#     # ----------------------------------------

#     def on_search_click(e):
#         results_view.controls.clear()
#         keyword = search_input.value
        
#         raw_results = Search.process_search_request(keyword)
#         sorted_results = Sort.sort_items_by_id(raw_results)

#         if not sorted_results:
#             results_view.controls.append(ft.Text("결과가 없습니다.", color=ft.Colors.RED))
#         else:
#             for item_id, item_name in sorted_results:
#                 results_view.controls.append(Asset.build_item_card(item_id, item_name))
            
#         page.update()

#     # ----------------------------------------
#     # Connect Event Listener
#     # ----------------------------------------

#     search_button.on_click = on_search_click

# Ver 3.0 (AI + 하드코딩 환장의 조합)

# if __name__ == "__main__":
#     ft.app(target=main)

# import flet as ft
# from Flet_Asset import Asset
# from Service import Crawler, Search, Sort
# from dotenv import load_dotenv

# load_dotenv()

# def main(page: ft.Page):

#     # ----------------------------------------
#     # Initalize
#     # ----------------------------------------

#     page.title = "⚔️Dekaron Crafting Item Table🛠️"
#     page.window_width = 800
#     page.window_height = 600
#     page.padding = 0

#     inital_page = Asset.initalization()

#     page.add(
#         inital_page
#     )
#     page.update()

#     # ----------------------------------------
#     # Basic Variables
#     # ----------------------------------------

#     # 탭 부분

#     Tabs = {
#         "User" : Asset.Controls["UserTab"].current,
#         "Search" : Asset.Controls["SearchTab"].current,
#         "Detail" : Asset.Controls["DetailTab"].current,
#     }

#     # 사용자 부분

#     User = {
#         "IDBar" : Asset.Controls["IDBar"].current,
#         "PasswordBar" : Asset.Controls["PasswordBar"].current,
#         "LoginButton" : Asset.Controls["LoginButton"].current,
#         "RegisterButton" : Asset.Controls["RegisterButton"].current
#     }

#     # 검색창 부분

#     search_input = Asset.Controls["SearchBar"].current
#     search_button = Asset.Controls["SearchButton"].current

#     results_view = Asset.Controls["Results"].current

#     # ----------------------------------------
#     # Event Functions
#     # ----------------------------------------

#     def on_login_click(evnet):
#         page.update()

#     def on_register_click(evnet):
#         page.update()

#     def on_close_click(event):
#         Asset.close_detail()
#         page.update()

#     async def on_detail_click(event):
#         item_id = event.control.data["Item_Id"]
#         item_name = event.control.data["Item_Name"]
        
#         Asset.set_up_detail("아이템 정보")
#         page.update() 
        
#         # 동기 크롤러를 스레드 풀에서 실행하여 UI가 굳는 현상 방지
#         import asyncio
#         item_info = await asyncio.to_thread(Crawler.get_item_description, item_id)
        
#         close_btn = Asset.build_item_detail(item_id, item_name, item_info)
#         close_btn.on_click = on_close_click

#         page.update()  

#     def on_search_click(e):
#         results_view.controls.clear()
#         keyword = search_input.value
        
#         raw_results = Search.process_search_request(keyword)
#         sorted_results = Sort.sort_items_by_id(raw_results)

#         if not sorted_results:
#             results_view.controls.append(ft.Text("결과가 없습니다.", color=ft.Colors.RED))
#         else:
#             for item_id, item_name in sorted_results:
#                 detail_btn = Asset.build_item_card(item_id, item_name)
#                 detail_btn.content.content.controls[2].content.on_click = on_detail_click
#                 results_view.controls.append(detail_btn)
            
#         page.update()

#     # ----------------------------------------
#     # Connect Event Listener
#     # ----------------------------------------

#     search_button.on_click = on_search_click

#     User["LoginButton"].on_click = on_login_click
#     User["RegisterButton"].on_click = on_register_click


# if __name__ == "__main__":
#     ft.app(target=main)

# ver 4.0 (찜 등록 기능)

# import flet as ft
# from Flet_Asset import Asset
# from Service import Crawler, Search, Sort
# from DuckDB import User as UserRepo
# from dotenv import load_dotenv

# load_dotenv()

# def main(page: ft.Page):

#     # ----------------------------------------
#     # Initalize
#     # ----------------------------------------

#     page.title = "⚔️Dekaron Crafting Item Table🛠️"
#     page.window_width = 800
#     page.window_height = 600
#     page.padding = 0

#     inital_page = Asset.initalization()

#     page.add(
#         inital_page
#     )
#     page.update()

#     # ----------------------------------------
#     # Basic Variables
#     # ----------------------------------------

#     # 사용자 부분

#     User = {
#         "IDBar" : Asset.Controls["IDBar"].current,
#         "PasswordBar" : Asset.Controls["PasswordBar"].current,
#         "LoginButton" : Asset.Controls["LoginButton"].current,
#         "RegisterButton" : Asset.Controls["RegisterButton"].current,
#         "LogoutButton" : None
#     }

#     # 검색창 부분

#     search_input = Asset.Controls["SearchBar"].current
#     search_button = Asset.Controls["SearchButton"].current

#     results_view = Asset.Controls["Results"].current

#     # ----------------------------------------
#     # Event Functions
#     # ----------------------------------------

#     def on_login_click(event):

#         username = Asset.Controls["IDBar"].current.value
#         password = Asset.Controls["PasswordBar"].current.value
        
#         # User.py를 통한 검증
#         user_id, valid_username = UserRepo.login(username, password)
        
#         if user_id:
#             # 정보 할당
#             Asset.Info["User"] = valid_username
#             Asset.Info["Userid"] = user_id
            
#             # UserTab의 내용을 User_Info()로 교체
#             Asset.Controls["UserTab"].current.content = Asset.User_Info()
            
#             # 화면 갱신을 먼저 수행하여 LogoutButton 레퍼런스가 활성화되도록 보장
#             event.page.update()
            
#             # 이제 렌더링된 로그아웃 버튼에 이벤트 매핑
#             logout_btn = Asset.Controls["LogoutButton"].current
#             if logout_btn:
#                 logout_btn.on_click = on_logout_click
                
#         else:
#             pass

#         page.update()

#     def on_register_click(event):
#         username = Asset.Controls["IDBar"].current.value
#         password = Asset.Controls["PasswordBar"].current.value
        
#         if not username or not password:
#             return # 빈 값 방어
            
#         success = UserRepo.register(username, password)
        
#         if success:
#             # 성공 시 피드백
#             Asset.Controls["IDBar"].current.value = ""
#             Asset.Controls["PasswordBar"].current.value = ""
#         else:
#             # 이미 있는 아이디인 경우 피드백
#             pass
            
#         event.page.update()

#         page.update()
    
#     def on_logout_click(event):
#         Asset.Info["User"] = None
#         Asset.Info["Userid"] = None
        
#         # 다시 로그인 화면으로 탭 복구 (초기에 구현하신 로그인 빌드 메서드 사용)
#         Asset.Controls["UserTab"].current.content = Asset.Login_Tab()

#         # 이벤트 재할당 
#         Asset.Controls["LoginButton"].current.on_click = on_login_click
#         Asset.Controls["RegisterButton"].current.on_click = on_register_click

#         page.update()

#     def on_close_click(event):
#         Asset.close_detail()
#         page.update()

#     async def on_FP_click(event):
#         if Asset.Info["User"] is not None:
#             item_id = event.control.data["Item_Id"]
#             item_name = event.control.data["Item_Name"]
            
#             Asset.add_recent_item(item_id, item_name)
#             Asset.Controls["UserTab"].current.content = Asset.User_Info()
                

#             logout_btn = Asset.Controls["LogoutButton"].current
#             if logout_btn:
#                 logout_btn.on_click = on_logout_click
#             Asset.set_up_detail("찜 등록")
#             page.update()
            
#             # 찜 목록 팝업 UI를 구성하기 위해 크롤링/검색 서비스로부터 아이템 상세 정보를 먼저 가져옵니다.
#             import asyncio
#             item_info = await asyncio.to_thread(Crawler.get_item_description, item_id)
            
#             # Asset의 build_SelectFP_detail을 호출하고 반환된 close_btn의 이벤트를 바인딩합니다.
#             close_btn = Asset.build_SelectFP_detail(item_id, item_name, item_info)
#             close_btn.on_click = on_close_click
            
#             page.update()

#     async def on_detail_click(event):
#         item_id = event.control.data["Item_Id"]
#         item_name = event.control.data["Item_Name"]
        
#         if Asset.Info["User"]:
#             Asset.add_recent_item(item_id, item_name)
#             Asset.Controls["UserTab"].current.content = Asset.User_Info()

#         logout_btn = Asset.Controls["LogoutButton"].current
#         if logout_btn:
#             logout_btn.on_click = on_logout_click
        
#         Asset.set_up_detail("아이템 정보")
#         page.update()
        
#         # 동기 크롤러를 스레드 풀에서 실행하여 UI가 굳는 현상 방지
#         import asyncio
#         item_info = await asyncio.to_thread(Crawler.get_item_description, item_id)
        
#         close_btn = Asset.build_item_detail(item_id, item_name, item_info)
#         close_btn.on_click = on_close_click

#         page.update()  

#     def on_search_click(e):
#         results_view.controls.clear()
#         keyword = search_input.value
        
#         raw_results = Search.process_search_request(keyword)
#         sorted_results = Sort.sort_items_by_id(raw_results)

#         if not sorted_results:
#             results_view.controls.append(ft.Text("결과가 없습니다.", color=ft.Colors.RED))
#         else:
#             for item_id, item_name in sorted_results:
#                 detail_btn = Asset.build_item_card(item_id, item_name)
#                 detail_btn.content.content.controls[2].controls[0].content.on_click = on_detail_click
#                 if len(detail_btn.content.content.controls[2].controls) >= 2:
#                     detail_btn.content.content.controls[2].controls[1].content.on_click = on_FP_click
#                 results_view.controls.append(detail_btn)
            
#         page.update()

#     # ----------------------------------------
#     # Connect Event Listener
#     # ----------------------------------------

#     search_button.on_click = on_search_click

#     User["LoginButton"].on_click = on_login_click
#     User["RegisterButton"].on_click = on_register_click


# if __name__ == "__main__":
#     ft.app(target=main)

import flet as ft
from Flet_Asset import Asset
from Service import Crawler, Search, Sort
from DuckDB import User as UserRepo
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

    # 사용자 부분

    User = {
        "IDBar" : Asset.Controls["IDBar"].current,
        "PasswordBar" : Asset.Controls["PasswordBar"].current,
        "LoginButton" : Asset.Controls["LoginButton"].current,
        "RegisterButton" : Asset.Controls["RegisterButton"].current,
        "LogoutButton" : None
    }

    # 검색창 부분

    search_input = Asset.Controls["SearchBar"].current
    search_button = Asset.Controls["SearchButton"].current

    results_view = Asset.Controls["Results"].current

    # ----------------------------------------
    # Event Functions
    # ----------------------------------------

    def on_login_click(event):

        username = Asset.Controls["IDBar"].current.value
        password = Asset.Controls["PasswordBar"].current.value
        
        # User.py를 통한 검증
        user_id, valid_username = UserRepo.login(username, password)
        
        if user_id:
            # 정보 할당
            Asset.Info["User"] = valid_username
            Asset.Info["Userid"] = user_id
            
            # UserTab의 내용을 User_Info()로 교체
            Asset.Controls["UserTab"].current.content = Asset.User_Info()
            
            # 화면 갱신을 먼저 수행하여 LogoutButton 레퍼런스가 활성화되도록 보장
            event.page.update()
            
            # 이제 렌더링된 로그아웃 버튼에 이벤트 매핑
            logout_btn = Asset.Controls["LogoutButton"].current
            if logout_btn:
                logout_btn.on_click = on_logout_click
                
        else:
            pass

        page.update()

    def on_register_click(event):
        username = Asset.Controls["IDBar"].current.value
        password = Asset.Controls["PasswordBar"].current.value
        
        if not username or not password:
            return # 빈 값 방어
            
        success = UserRepo.register(username, password)
        
        if success:
            # 성공 시 피드백
            Asset.Controls["IDBar"].current.value = ""
            Asset.Controls["PasswordBar"].current.value = ""
        else:
            # 이미 있는 아이디인 경우 피드백
            pass
            
        event.page.update()

        page.update()
    
    def on_logout_click(event):
        Asset.Info["User"] = None
        Asset.Info["Userid"] = None
        
        # 다시 로그인 화면으로 탭 복구 (초기에 구현하신 로그인 빌드 메서드 사용)
        Asset.Controls["UserTab"].current.content = Asset.Login_Tab()

        # 이벤트 재할당 
        Asset.Controls["LoginButton"].current.on_click = on_login_click
        Asset.Controls["RegisterButton"].current.on_click = on_register_click

        page.update()

    def on_close_click(event):
        Asset.close_detail()
        page.update()

    async def on_FP_click(event):
        if Asset.Info["User"] is not None:
            item_id = event.control.data["Item_Id"]
            item_name = event.control.data["Item_Name"]
            
            Asset.add_recent_item(item_id, item_name)
            Asset.Controls["UserTab"].current.content = Asset.User_Info()
                

            logout_btn = Asset.Controls["LogoutButton"].current
            if logout_btn:
                logout_btn.on_click = on_logout_click
            Asset.set_up_detail("찜 등록")
            page.update()
            
            # 찜 목록 팝업 UI를 구성하기 위해 크롤링/검색 서비스로부터 아이템 상세 정보를 먼저 가져옵니다.
            import asyncio
            item_info = await asyncio.to_thread(Crawler.get_item_description, item_id)
            
            # Asset의 build_SelectFP_detail을 호출하고 반환된 close_btn의 이벤트를 바인딩합니다.
            close_btn = Asset.build_SelectFP_detail(item_id, item_name, item_info)
            close_btn.on_click = on_close_click
            
            page.update()

    async def on_detail_click(event):
        item_id = event.control.data["Item_Id"]
        item_name = event.control.data["Item_Name"]
        
        if Asset.Info["User"]:
            Asset.add_recent_item(item_id, item_name)
            Asset.Controls["UserTab"].current.content = Asset.User_Info()

        logout_btn = Asset.Controls["LogoutButton"].current
        if logout_btn:
            logout_btn.on_click = on_logout_click
        
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
                detail_btn.content.content.controls[2].controls[0].content.on_click = on_detail_click
                if len(detail_btn.content.content.controls[2].controls) >= 2:
                    detail_btn.content.content.controls[2].controls[1].content.on_click = on_FP_click
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