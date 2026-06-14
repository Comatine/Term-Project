# ver 1.0 (AI를 활용한 초기 구성)

# import flet as ft
# from dotenv import load_dotenv
# import os

# class Asset:

#     def __init__(self):
#         pass

#     load_dotenv()
    
#     @staticmethod
#     def build_item_card(item_id: int, item_name: str):
#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         return ft.Card(
#             content=ft.Container(
#                 content=ft.Row([
#                     ft.Container(
#                         content=ft.Image(
#                             src=image_url,
#                             width=50,
#                             height=50,
#                             fit=ft.BoxFit.NONE,
#                             error_content=ft.Image(src="Assets/Placeholder.png", width=60, height=60),
#                         ),
#                         border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                         border_radius=ft.BorderRadius.all(10)
#                     ),
#                     ft.Column([
#                         ft.Text(
#                             item_name,
#                             weight=ft.FontWeight.BOLD,
#                             size=20
#                             )
#                     ])
#                 ]),
#                 padding=10,
#                 border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                 border_radius=ft.BorderRadius.all(10)
#             )
#         )

# Ver 2.0 (하드코딩 버전)

# import flet as ft
# from dotenv import load_dotenv
# import os

# class Asset:

#     load_dotenv()

#     Controls = {
#         "SearchBar" : ft.Ref[ft.TextField](),
#         "SearchButton" : ft.Ref[ft.ElevatedButton](),
#         "Results" : ft.Ref[ft.ListView]()
#     }

#     @staticmethod
#     def initalization():
#         return ft.Row(
#             controls=[
#                 # 사용자 정보
#                 # 1. 배경
#                 ft.Container(
#                     expand=1,
#                     bgcolor=ft.Colors.BLACK_87,
#                     # 크기 맞춤
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=ft.Column(
#                             controls=[
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="아이디",
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             expand=True
#                                         )
#                                     ]
#                                 ),
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="패스워드",
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             password=True,
#                                             can_reveal_password=True,
#                                             expand=True
#                                         )
#                                     ]
#                                 ),
#                                 ft.Row(
#                                     controls=[
#                                         ft.Button(
#                                         content="로그인",
#                                         expand=True
#                                         ),
#                                         ft.Button(
#                                         content="회원가입",
#                                         expand=True
#                                         )
#                                     ]
#                                 )
#                             ]
#                         )
#                     )
#                 ),

#                 # 아이템 검색 창
#                 ft.Container(
#                     expand=2,
#                     bgcolor=ft.Colors.BLACK_12,
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=ft.Column(
#                             # 검색 바
#                             controls=[
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="검색어 입력",
#                                             expand=True,
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             ref=Asset.Controls["SearchBar"]
#                                         ),
#                                         ft.ElevatedButton("검색", ref=Asset.Controls["SearchButton"])
#                                     ]
#                                 ),
#                                 # 검색 결과
#                                 ft.Container(
#                                     expand=True,
#                                     content=ft.ListView(
#                                         expand=True,
#                                         spacing=10,
#                                         ref=Asset.Controls["Results"]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ),
#                 # 아이템 세부 정보 혹은 찜 목록 정보
#                 ft.Container(
#                     # 임시
#                     content=ft.Divider(
#                         height=0
#                     )
#                 )
#             ],
#             expand=True
#     )
    
#     @staticmethod
#     def build_item_card(item_id: int, item_name: str):
#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         return ft.Card(
#             content=ft.Container(
#                 content=ft.Row(
#                     controls=[
#                         ft.Container(
#                             content=ft.Image(
#                                 src=image_url,
#                                 width=50,
#                                 height=50,
#                                 fit=ft.BoxFit.NONE,
#                                 error_content=ft.Image(src="Assets/Placeholder.png", width=60, height=60),
#                             ),
#                             border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                             border_radius=ft.BorderRadius.all(10)
#                         ),
#                         ft.Column(
#                             controls=[
#                                 ft.Text(
#                                     item_name,
#                                     weight=ft.FontWeight.BOLD,
#                                     size=20
#                                 )
#                             ]
#                         ),
#                         ft.Container(
#                             content=ft.ElevatedButton(
#                                 content="세부 정보",
#                                 icon=ft.Icons.PLAY_ARROW,
#                                 icon_color=ft.Colors.GREY_600,
#                                 data={
#                                     "Item_Id" : item_id
#                                 }
#                             ),
#                             alignment=ft.Alignment.CENTER_RIGHT,
#                             expand=True
#                         )
#                     ],
#                     alignment=ft.MainAxisAlignment.START
#                 ),
#                 padding=10,
#                 border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                 border_radius=ft.BorderRadius.all(10)
#             )
#         )

# Ver 3.0 (AI + 하드코딩 환장의 조합)

# import flet as ft
# from dotenv import load_dotenv
# from Service import Sort, Search
# import os

# class Asset:

#     load_dotenv()

#     Info = {
#         "User" : None,
#     }

#     Controls = {
#         # 탭
#         "UserTab" : ft.Ref[ft.Container](),
#         "SearchTab" : ft.Ref[ft.Container](),
#         "DetailTab" : ft.Ref[ft.Container](),

#         # 사용자
#         "IDBar" : ft.Ref[ft.TextField](),
#         "PasswordBar" : ft.Ref[ft.TextField](),
#         "LoginButton" : ft.Ref[ft.Button](),
#         "RegisterButton" : ft.Ref[ft.Button](),

#         # 검색
#         "SearchBar" : ft.Ref[ft.TextField](),
#         "SearchButton" : ft.Ref[ft.ElevatedButton](),
#         "Results" : ft.Ref[ft.ListView]()
#     }
# # --------------------------------------------------
# #   Inner Method
# # --------------------------------------------------

#     def SetRatio(isopen : str):
#         SearchTab = Asset.Controls["SearchTab"].current
#         DetailTab = Asset.Controls["DetailTab"].current

#         if isopen == "open":
#             SearchTab.expand = 1
#             DetailTab.expand = 3
#         elif isopen == "close":
#             SearchTab.expand = 2
#             DetailTab.expand = 0
#             DetailTab.content = ft.Divider(height=0)

#     def build_Loading(val : str):
#         DetailTab = Asset.Controls["DetailTab"].current
#         DetailTab.expend = 0

#         DetailTab.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Text(
#                         value=f"{val}을(를) 로딩하고 있습니다",
#                         align=ft.Alignment.CENTER
#                     ),
#                     ft.Row(
#                         controls=[
#                             ft.ProgressRing(
#                                 width=50, height=50,
#                                 align=ft.Alignment.CENTER,
#                                 expand=True
#                             )
#                         ],
#                     )
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 expand=True
#             ),
#             padding=ft.Padding.all(20),
#             alignment=ft.Alignment.CENTER,
#             expand=3
#         )

# # --------------------------------------------------
# #   Static Method
# # --------------------------------------------------

#     @staticmethod
#     def initalization():
#         return ft.Row(
#             controls=[
#                 # 사용자 정보
#                 ft.Container(
#                     expand=1,
#                     bgcolor=ft.Colors.BLACK_87,
#                     ref=Asset.Controls["UserTab"],
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=ft.Column(
#                             controls=[
#                                 # 타이틀
#                                 ft.Row(
#                                     height=50,
#                                     controls=[
#                                         ft.Container(
#                                             content=ft.Text(
#                                                 value="⚔️Dekaron Crafting Item Table🛠️",
#                                                 size=20,
#                                                 weight=ft.FontWeight.BOLD,
#                                                 no_wrap=True,
#                                                 expand=True
#                                             ),
#                                             alignment=ft.Alignment.CENTER,
#                                             expand=True
#                                         )
#                                     ]
#                                 ),
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="아이디",
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             expand=True,
#                                             ref=Asset.Controls["IDBar"]
#                                         )
#                                     ]
#                                 ),
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="패스워드",
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             password=True,
#                                             can_reveal_password=True,
#                                             expand=True,
#                                             ref=Asset.Controls["PasswordBar"]
#                                         )
#                                     ]
#                                 ),
#                                 ft.Row(
#                                     controls=[
#                                         ft.Button(
#                                             content="로그인",
#                                             expand=True,
#                                             ref=Asset.Controls["LoginButton"]
#                                         ),
#                                         ft.Button(
#                                             content="회원가입",
#                                             expand=True,
#                                             ref=Asset.Controls["RegisterButton"]
#                                         )
#                                     ]
#                                 )
#                             ]
#                         )
#                     )
#                 ),

#                 # 아이템 검색 창
#                 ft.Container(
#                     expand=2,
#                     bgcolor=ft.Colors.BLACK_12,
#                     ref=Asset.Controls["SearchTab"],
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=ft.Column(
#                             # 검색 바
#                             controls=[
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="검색어 입력",
#                                             expand=True,
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             ref=Asset.Controls["SearchBar"]
#                                         ),
#                                         ft.ElevatedButton("검색", ref=Asset.Controls["SearchButton"])
#                                     ]
#                                 ),
#                                 # 검색 결과
#                                 ft.Container(
#                                     expand=True,
#                                     content=ft.ListView(
#                                         expand=True,
#                                         spacing=10,
#                                         ref=Asset.Controls["Results"]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ),
#                 # 아이템 세부 정보 혹은 찜 목록 정보
#                 ft.Container(
#                     ref=Asset.Controls["DetailTab"],
#                     expand = 0,
#                     # 임시
#                     content=ft.Divider(
#                         height=0
#                     )
#                 )
#             ],
#             expand=True
#     )
    
#     @staticmethod
#     def build_item_card(item_id: int, item_name: str):
#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         return ft.Card(
#             content=ft.Container(
#                 content=ft.Row(
#                     controls=[
#                         ft.Container(
#                             content=ft.Image(
#                                 src=image_url,
#                                 width=50,
#                                 height=50,
#                                 fit=ft.BoxFit.NONE,
#                                 error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50),
#                             ),
#                             border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                             border_radius=ft.BorderRadius.all(10)
#                         ),
#                         ft.Column(
#                             controls=[
#                                 ft.Text(
#                                     item_name,
#                                     weight=ft.FontWeight.BOLD,
#                                     size=20
#                                 )
#                             ]
#                         ),
#                         ft.Container(
#                             content=ft.ElevatedButton(
#                                 content="세부 정보",
#                                 icon=ft.Icons.PLAY_ARROW,
#                                 icon_color=ft.Colors.GREY_600,
#                                 data={
#                                     "Item_Id" : item_id,
#                                     "Item_Name" : item_name
#                                 }
#                             ),
#                             alignment=ft.Alignment.CENTER_RIGHT,
#                             expand=True
#                         )
#                     ],
#                     alignment=ft.MainAxisAlignment.START
#                 ),
#                 padding=10,
#                 border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                 border_radius=ft.BorderRadius.all(10)
#             )
#         )
    
#     @staticmethod
#     def set_up_detail(Type : str = None):
#         Asset.SetRatio("open")
#         Asset.build_Loading(Type)

#     @staticmethod
#     def close_detail():
#         Asset.SetRatio("close")
    
#     @staticmethod
#     def build_item_detail(item_id: int, item_name: str, item_info):
#         # 1. 화면 탭 및 기본 데이터 설정
#         DetailTab = Asset.Controls["DetailTab"].current

#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         base_info_text = Sort.sort_item_base_info(item_info)

#         close_btn = ft.Button(
#             content="X",
#             height=50, width=50,
#             align=ft.Alignment.CENTER_RIGHT
#         )

#         ColumnLi = DetailTab.content.content
#         ColumnLi.controls.clear()
#         ColumnLi.alignment = None
        
#         # 2. 기본 정보 및 이미지 블록 배치
#         list_controls = [
#             ft.Row(
#                 controls=[
#                     ft.Container(
#                         content=ft.Image(
#                             src=image_url,
#                             width=100, height=100,
#                             fit=ft.BoxFit.NONE, # 구버전의 경우 ft.BoxFit.NONE 사용
#                             error_content=ft.Image(src="Assets/Placeholder.png", width=100, height=100),
#                         ),
#                         border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                         border_radius=ft.BorderRadius.all(10)
#                     ),
#                     ft.Column(
#                         controls=[
#                             ft.Text(value=item_name, weight=ft.FontWeight.BOLD, size=25, align=ft.Alignment.TOP_LEFT),
#                             ft.Text(value=base_info_text, size=15, align=ft.Alignment.TOP_LEFT)
#                         ],
#                         alignment=ft.MainAxisAlignment.START,
#                         height=100
#                     ),
#                     ft.Container(content=close_btn, expand=True)
#                 ],
#                 expand=True,
#                 alignment=ft.MainAxisAlignment.START
#             )
#         ]

#         # 3. '추가 옵션' 세부 정보 추출 및 배치
#         additional_options = Sort.extract_additional_options(item_info)
#         if additional_options:
#             opt_controls = [ft.Text("추가 옵션", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.BLUE_300)]
#             for key, val in additional_options.items():
#                 opt_controls.append(ft.Row([ft.Text(f"• {key} :", weight=ft.FontWeight.W_500, size=14), ft.Text(f"{val}", size=14)]))
            
#             list_controls.append(
#                 ft.Container(content=ft.Column(controls=opt_controls), margin=ft.Margin.only(top=15, bottom=5))
#             )

#         # 4. 획득 경로 및 드랍 정보 표기 (Service 계층 간접 호출)
#         obtain_paths = Search.get_item_obtain_paths(item_id)
        
#         if obtain_paths:
#             path_str = ", ".join(obtain_paths)
#             list_controls.append(
#                 ft.Container(
#                     content=ft.Column([
#                         ft.Text("획득 경로", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.GREEN_300),
#                         ft.Text(path_str, size=14)
#                     ]),
#                     margin=ft.Margin.only(top=10, bottom=5)
#                 )
#             )

#             # 경로에 'Droppable'이 포함되어 있으면 드랍 맵/몬스터 표시
#             if "Droppable" in obtain_paths:
#                 drop_data = Search.get_item_drop_info(item_id)
#                 if drop_data:
#                     formatted_drops = Sort.format_drop_info(drop_data)
#                     drop_controls = [ft.Text("📍 드랍 정보 (맵별 몬스터)", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.ORANGE_300)]
                    
#                     for loc, monsters in formatted_drops.items():
#                         monsters_str = ", ".join(monsters)
#                         drop_controls.append(ft.Text(f"[{loc}] : {monsters_str}", size=14))
                        
#                     list_controls.append(
#                         ft.Container(content=ft.Column(controls=drop_controls), margin=ft.Margin.only(left=10, top=5))
#                     )

#         # 5. 제작 정보(필요 재료, 제작 경로) 및 전체 제작 트리 시각화
#         craft_info_list = Search.get_craft_info(item_id)
#         if craft_info_list:
#             # 반환받는 튜플을 3개(craft_name, craft_progress, craft_type)로 언패킹
#             for craft_name, craft_progress, craft_type in craft_info_list:
#                 craft_controls = [
#                     ft.Text(f"🛠️ 제작 정보 ({craft_name})", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.PURPLE_300),
#                     # 제작 경로 추가
#                     ft.Text(f"📍 제작 장소/경로 : {craft_type}", weight=ft.FontWeight.W_500, size=14, color=ft.Colors.TEAL_300)
#                 ]
                
#                 # 5-1. 해당 아이템의 필요 제작 재료
#                 materials = Search.get_craft_materials(craft_name, item_id)
#                 if materials:
#                     craft_controls.append(ft.Container(height=5)) # 약간의 간격 띄우기
#                     craft_controls.append(ft.Text("필요 재료:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
#                     for mat_name, mat_amount, mat_id in materials:
#                         craft_controls.append(ft.Text(f" • {mat_name} x {mat_amount}", size=14))
                
#                 # 5-2. 전체 제작 트리 시각화 (가로 스크롤 Row 컨테이너)
#                 series_items = Search.get_craft_series(craft_name)
#                 if series_items:
#                     craft_controls.append(ft.Container(height=10)) # 간격 띄우기
#                     craft_controls.append(ft.Text("제작 트리:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
                    
#                     tree_controls = []
#                     for i, (prog, t_item_id, t_item_name) in enumerate(series_items):
#                         # 아이템 사이 화살표 아이콘
#                         if i > 0:
#                             tree_controls.append(
#                                 ft.Container(content=ft.Icon(ft.Icons.ARROW_RIGHT, size=20, color=ft.Colors.GREY_400), alignment=ft.Alignment.CENTER)
#                             )
                        
#                         t_image_url = image_url_template.replace("Item_Id", str(t_item_id))
                        
#                         # 현재 선택된 아이템의 테두리는 시각적으로 강조
#                         is_current = (t_item_id == item_id)
#                         border_color = ft.Colors.PURPLE_400 if is_current else ft.Colors.GREY_600
#                         border_width = 2 if is_current else 1
                        
#                         tree_controls.append(
#                             ft.Column([
#                                 ft.Container(
#                                     content=ft.Image(src=t_image_url, width=50, height=50, fit=ft.BoxFit.NONE, error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50)),
#                                     border=ft.Border.all(width=border_width, color=border_color),
#                                     border_radius=ft.BorderRadius.all(5)
#                                 ),
#                                 ft.Text(f"{prog}단계", size=12, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE if is_current else ft.Colors.GREY_400)
#                             ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
#                         )
                    
#                     # 아이템 트리가 길어질 것을 대비해 가로 스크롤 설정 적용
#                     craft_controls.append(
#                         ft.Row(controls=tree_controls, scroll=ft.ScrollMode.ADAPTIVE, vertical_alignment=ft.CrossAxisAlignment.CENTER)
#                     )
                
#                 list_controls.append(
#                     ft.Container(content=ft.Column(controls=craft_controls), margin=ft.Margin.only(top=15, bottom=5))
#                 )

#         # 6. 최종 ListView 조립 및 삽입
#         ColumnLi.controls.append(
#             ft.ListView(
#                 controls=list_controls,
#                 spacing=10,
#                 expand=True
#             )
#         )
        
#         return close_btn

# Ver 4.0 (찜 등록 기능)

# import flet as ft
# from dotenv import load_dotenv
# from Service import Sort, Search
# from DuckDB import Item, User
# import os

# class Asset:

#     load_dotenv()

#     Info = {
#         "User" : None,
#         "Userid" : None
#     }

#     Controls = {
#         # 탭
#         "UserTab" : ft.Ref[ft.Container](),
#         "SearchTab" : ft.Ref[ft.Container](),
#         "DetailTab" : ft.Ref[ft.Container](),

#         # 사용자
#         "IDBar" : ft.Ref[ft.TextField](),
#         "PasswordBar" : ft.Ref[ft.TextField](),
#         "LoginButton" : ft.Ref[ft.Button](),
#         "RegisterButton" : ft.Ref[ft.Button](),
#         "LogoutButton" : ft.Ref[ft.Button](),
#         "RecentItemView" : ft.Ref[ft.ListView](),
#         "FPList" : ft.Ref[ft.ListView](),

#         # 검색
#         "SearchBar" : ft.Ref[ft.TextField](),
#         "SearchButton" : ft.Ref[ft.ElevatedButton](),
#         "Results" : ft.Ref[ft.ListView]()
#     }

#     RecentItems = []

#     # 로그인 창 재할당
#     @staticmethod
#     def Login_Tab():
#         return ft.Column(
#                 controls=[
#                     # 타이틀
#                     ft.Row(
#                         height=50,
#                         controls=[
#                             ft.Container(
#                                 content=ft.Text(
#                                     value="⚔️Dekaron Crafting Item Table🛠️",
#                                     size=20,
#                                     weight=ft.FontWeight.BOLD,
#                                     no_wrap=True,
#                                     expand=True
#                                 ),
#                                 alignment=ft.Alignment.CENTER,
#                                 expand=True
#                             )
#                         ]
#                     ),
#                     ft.Row(
#                         controls=[
#                             ft.TextField(
#                                 label="아이디",
#                                 border_radius=ft.BorderRadius.all(10),
#                                 border_color=ft.Colors.GREY_600,
#                                 expand=True,
#                                 ref=Asset.Controls["IDBar"]
#                             )
#                         ]
#                     ),
#                     ft.Row(
#                         controls=[
#                             ft.TextField(
#                                 label="패스워드",
#                                 border_radius=ft.BorderRadius.all(10),
#                                 border_color=ft.Colors.GREY_600,
#                                 password=True,
#                                 can_reveal_password=True,
#                                 expand=True,
#                                 ref=Asset.Controls["PasswordBar"]
#                             )
#                         ]
#                     ),
#                     ft.Row(
#                         controls=[
#                             ft.Button(
#                                 content="로그인",
#                                 expand=True,
#                                 ref=Asset.Controls["LoginButton"]
#                             ),
#                             ft.Button(
#                                 content="회원가입",
#                                 expand=True,
#                                 ref=Asset.Controls["RegisterButton"]
#                             )
#                         ]
#                     )
#             ]
#         )

#     @classmethod
#     def User_Info(cls):
#         username = cls.Info["User"]
#         userid = cls.Info["Userid"]

#         # 1. 최근 탐색 목록 컨트롤 생성
#         recent_controls = []
#         if not cls.RecentItems:
#             recent_controls.append(ft.Text("최근 탐색한 아이템이 없습니다.", color=ft.Colors.GREY_500))
#         else:
#             for item in cls.RecentItems:
#                 recent_controls.append(
#                     ft.ElevatedButton(
#                         item['name'],
#                         icon=ft.Icons.HISTORY,
#                         # on_click=lambda e, i=item['id']: [아이템 상세 보기 로직 연결]
#                     )
#                 )

#         # 2. 찜 목록(Favorite Pin) 컨트롤 생성
#         fp_controls = []
#         favorite_pins = User.get_favorite_pins(userid)
#         if not favorite_pins:
#             fp_controls.append(ft.Text("찜한 목록이 없습니다.", color=ft.Colors.GREY_500))
#         else:
#             for pin in favorite_pins:
#                 # Pin_Name이 없을 경우 Pin_Id로 대체 표시
#                 display_name = pin['Pin_Name'] if pin['Pin_Name'] else f"저장된 항목 #{pin['Pin_Id']}"
#                 fp_controls.append(
#                     ft.ElevatedButton(
#                         display_name,
#                         icon=ft.Icons.STAR,
#                         icon_color=ft.Colors.YELLOW_500,
#                         # on_click=lambda e, p_id=pin['Pin_Id']: [찜 항목 불러오기 로직 연결]
#                     )
#                 )

#         return ft.Column(
#             controls=[
#                 # 타이틀
#                 ft.Row(
#                     height=50,
#                     controls=[
#                         ft.Container(
#                             content=ft.Text(
#                                 value="⚔️Dekaron Crafting Item Table🛠️",
#                                 size=20,
#                                 weight=ft.FontWeight.BOLD,
#                                 no_wrap=True,
#                                 expand=True
#                             ),
#                             alignment=ft.Alignment.CENTER,
#                             expand=True
#                         )
#                     ]
#                 ),
#                 # 유저 이름
#                 ft.Row(
#                     controls=[
#                         ft.Text(
#                             value=f"{username} (Id : {userid})",
#                             size=20,
#                             weight=ft.FontWeight.BOLD,
#                             no_wrap=True,
#                             expand=True
#                         )
#                     ]
#                 ),
#                 # 로그아웃 버튼
#                 ft.Row(
#                     controls=[
#                         ft.Button(
#                             content=ft.Text("로그아웃"),
#                             expand=True,
#                             ref=cls.Controls["LogoutButton"]
#                         ),
#                     ]
#                 ),
#                 # 리스트 뷰 영역
#                 ft.Row(
#                     expand=True,
#                     controls=[
#                         ft.Column(
#                             expand=True,
#                             controls=[
#                                 ft.Text("🕒 최근 탐색 아이템", weight=ft.FontWeight.BOLD),
#                                 ft.ListView(
#                                     expand=1,
#                                     ref=cls.Controls["RecentItemView"],
#                                     height=200,
#                                     controls=recent_controls,
#                                 ),
#                                 ft.Divider(),
#                                 ft.Text("⭐ 찜 목록", weight=ft.FontWeight.BOLD),
#                                 ft.ListView(
#                                     expand=1,
#                                     ref=cls.Controls["FPList"],
#                                     height=200,
#                                     controls=fp_controls,
#                                 )
#                             ]
#                         )
#                     ]
#                 )
#             ]
#         )
# # --------------------------------------------------
# #   Inner Method
# # --------------------------------------------------


#     def SetRatio(isopen : str):
#         SearchTab = Asset.Controls["SearchTab"].current
#         DetailTab = Asset.Controls["DetailTab"].current

#         if isopen == "open":
#             SearchTab.expand = 1
#             DetailTab.expand = 3
#         elif isopen == "close":
#             SearchTab.expand = 2
#             DetailTab.expand = 0
#             DetailTab.content = ft.Divider(height=0)

#     def build_Loading(val : str):
#         DetailTab = Asset.Controls["DetailTab"].current
#         DetailTab.expend = 0

#         DetailTab.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Text(
#                         value=f"{val}을(를) 로딩하고 있습니다",
#                         align=ft.Alignment.CENTER
#                     ),
#                     ft.Row(
#                         controls=[
#                             ft.ProgressRing(
#                                 width=50, height=50,
#                                 align=ft.Alignment.CENTER,
#                                 expand=True
#                             )
#                         ],
#                     )
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 expand=True
#             ),
#             padding=ft.Padding.all(20),
#             alignment=ft.Alignment.CENTER,
#             expand=3
#         )

#     @classmethod
#     def add_recent_item(cls, item_id, item_name):
#         """아이템을 검색/열람할 때 호출하여 최근 목록을 갱신합니다."""
#         # 이미 목록에 있다면 제거 (중복 방지)
#         cls.RecentItems = [item for item in cls.RecentItems if item['id'] != item_id]
#         # 맨 앞에 새 아이템 추가
#         cls.RecentItems.insert(0, {'id': item_id, 'name': item_name})
        
#         # 목록이 너무 길어지는 것을 방지 (예: 최대 20개 유지)
#         if len(cls.RecentItems) > 20:
#             cls.RecentItems.pop()

            

# # --------------------------------------------------
# #   Static Method
# # --------------------------------------------------

#     @staticmethod
#     def initalization():
#         return ft.Row(
#             controls=[
#                 # 사용자 정보
#                 ft.Container(
#                     expand=1,
#                     bgcolor=ft.Colors.BLACK_87,
#                     ref=Asset.Controls["UserTab"],
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=Asset.Login_Tab()
#                     )
#                 ),

#                 # 아이템 검색 창
#                 ft.Container(
#                     expand=2,
#                     bgcolor=ft.Colors.BLACK_12,
#                     ref=Asset.Controls["SearchTab"],
#                     content=ft.Container(
#                         padding=ft.Padding.all(20),
#                         content=ft.Column(
#                             # 검색 바
#                             controls=[
#                                 ft.Row(
#                                     controls=[
#                                         ft.TextField(
#                                             label="검색어 입력",
#                                             expand=True,
#                                             border_radius=ft.BorderRadius.all(10),
#                                             border_color=ft.Colors.GREY_600,
#                                             ref=Asset.Controls["SearchBar"]
#                                         ),
#                                         ft.ElevatedButton("검색", ref=Asset.Controls["SearchButton"])
#                                     ]
#                                 ),
#                                 # 검색 결과
#                                 ft.Container(
#                                     expand=True,
#                                     content=ft.ListView(
#                                         expand=True,
#                                         spacing=10,
#                                         ref=Asset.Controls["Results"]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ),
#                 # 아이템 세부 정보 혹은 찜 목록 정보
#                 ft.Container(
#                     ref=Asset.Controls["DetailTab"],
#                     expand = 0,
#                     # 임시
#                     content=ft.Divider(
#                         height=0
#                     )
#                 )
#             ],
#             expand=True
#     )
    
#     @staticmethod
#     def build_item_card(item_id: int, item_name: str):
#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         card = ft.Card(
#             content=ft.Container(
#                 content=ft.Row(
#                     controls=[
#                         ft.Container(
#                             content=ft.Image(
#                                 src=image_url,
#                                 width=50,
#                                 height=50,
#                                 fit=ft.BoxFit.NONE,
#                                 error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50),
#                             ),
#                             border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                             border_radius=ft.BorderRadius.all(10)
#                         ),
#                         ft.Column(
#                             controls=[
#                                 ft.Text(
#                                     item_name,
#                                     weight=ft.FontWeight.BOLD,
#                                     size=20
#                                 )
#                             ]
#                         ),
#                         ft.Row(
#                             controls=[
#                                 ft. Container(
#                                     content=ft.ElevatedButton(
#                                         content="세부 정보",
#                                         icon=ft.Icons.PLAY_ARROW,
#                                         icon_color=ft.Colors.GREY_600,
#                                         data={
#                                             "Item_Id" : item_id,
#                                             "Item_Name" : item_name
#                                         }
#                                     ),
#                                     alignment=ft.Alignment.CENTER_RIGHT,
#                                     width=140
#                                 )
#                             ],
#                             alignment=ft.MainAxisAlignment.END,
#                             expand=True
#                         )
#                     ],
#                     alignment=ft.MainAxisAlignment.START
#                 ),
#                 padding=10,
#                 border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                 border_radius=ft.BorderRadius.all(10)
#             )
#         )

#         if Item.is_craftable_item(item_id) :
#             card.content.content.controls[2].controls.append(
#                 ft.Container(
#                     content=ft.ElevatedButton(
#                         content="",
#                         icon=ft.Icons.STAR,
#                         icon_color=ft.Colors.GREY_600,
#                         data={
#                             "Item_Id" : item_id,
#                             "Item_Name" : item_name
#                         }
#                     ),
#                     alignment=ft.Alignment.CENTER_RIGHT,
#                     width=60
#                 )
#             )



#         return card
    
    
#     @staticmethod
#     def set_up_detail(Type : str = None):
#         Asset.SetRatio("open")
#         Asset.build_Loading(Type)

#     @staticmethod
#     def close_detail():
#         Asset.SetRatio("close")
    
#     @staticmethod
#     def build_item_detail(item_id: int, item_name: str, item_info):
#         # 1. 화면 탭 및 기본 데이터 설정
#         DetailTab = Asset.Controls["DetailTab"].current

#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         base_info_text = Sort.sort_item_base_info(item_info)

#         close_btn = ft.Button(
#             content="X",
#             height=50, width=50,
#             align=ft.Alignment.CENTER_RIGHT
#         )

#         ColumnLi = DetailTab.content.content
#         ColumnLi.controls.clear()
#         ColumnLi.alignment = None
        
#         # 2. 기본 정보 및 이미지 블록 배치
#         list_controls = [
#             ft.Row(
#                 controls=[
#                     ft.Container(
#                         content=ft.Image(
#                             src=image_url,
#                             width=100, height=100,
#                             fit=ft.BoxFit.NONE,  
#                             error_content=ft.Image(src="Assets/Placeholder.png", width=100, height=100),
#                         ),
#                         border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                         border_radius=ft.BorderRadius.all(10)
#                     ),
#                     ft.Column(
#                         controls=[
#                             ft.Text(value=item_name, weight=ft.FontWeight.BOLD, size=25, align=ft.Alignment.TOP_LEFT),
#                             ft.Text(value=base_info_text, size=15, align=ft.Alignment.TOP_LEFT)
#                         ],
#                         alignment=ft.MainAxisAlignment.START,
#                         height=100
#                     ),
#                     ft.Container(content=close_btn, expand=True)
#                 ],
#                 expand=True,
#                 alignment=ft.MainAxisAlignment.START
#             )
#         ]

#         # 3. '추가 옵션' 세부 정보 추출 및 배치
#         additional_options = Sort.extract_additional_options(item_info)
#         if additional_options:
#             opt_controls = [ft.Text("추가 옵션", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.BLUE_300)]
#             for key, val in additional_options.items():
#                 opt_controls.append(ft.Row([ft.Text(f"• {key} :", weight=ft.FontWeight.W_500, size=14), ft.Text(f"{val}", size=14)]))
            
#             list_controls.append(
#                 ft.Container(content=ft.Column(controls=opt_controls), margin=ft.Margin.only(top=15, bottom=5))
#             )

#         # 4. 획득 경로 및 드랍 정보 표기 (Service 계층 간접 호출)
#         obtain_paths = Search.get_item_obtain_paths(item_id)
        
#         if obtain_paths:
#             path_str = ", ".join(obtain_paths)
#             list_controls.append(
#                 ft.Container(
#                     content=ft.Column([
#                         ft.Text("획득 경로", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.GREEN_300),
#                         ft.Text(path_str, size=14)
#                     ]),
#                     margin=ft.Margin.only(top=10, bottom=5)
#                 )
#             )

#             # 경로에 'Droppable'이 포함되어 있으면 드랍 맵/몬스터 표시
#             if "Droppable" in obtain_paths:
#                 drop_data = Search.get_item_drop_info(item_id)
#                 if drop_data:
#                     formatted_drops = Sort.format_drop_info(drop_data)
#                     drop_controls = [ft.Text("📍 드랍 정보 (맵별 몬스터)", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.ORANGE_300)]
                    
#                     for loc, monsters in formatted_drops.items():
#                         monsters_str = ", ".join(monsters)
#                         drop_controls.append(ft.Text(f"[{loc}] : {monsters_str}", size=14))
                        
#                     list_controls.append(
#                         ft.Container(content=ft.Column(controls=drop_controls), margin=ft.Margin.only(left=10, top=5))
#                     )

#         # 5. 제작 정보(필요 재료, 제작 경로) 및 전체 제작 트리 시각화
#         craft_info_list = Search.get_craft_info(item_id)
#         if craft_info_list:
#             # 반환받는 튜플을 3개(craft_name, craft_progress, craft_type)로 언패킹
#             for craft_name, craft_progress, craft_type in craft_info_list:
#                 craft_controls = [
#                     ft.Text(f"🛠️ 제작 정보 ({craft_name})", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.PURPLE_300),
#                     # 제작 경로 추가
#                     ft.Text(f"📍 제작 장소/경로 : {craft_type}", weight=ft.FontWeight.W_500, size=14, color=ft.Colors.TEAL_300)
#                 ]
                
#                 # 5-1. 해당 아이템의 필요 제작 재료
#                 materials = Search.get_craft_materials(craft_name, item_id)
#                 if materials:
#                     craft_controls.append(ft.Container(height=5)) # 약간의 간격 띄우기
#                     craft_controls.append(ft.Text("필요 재료:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
#                     for mat_name, mat_amount, mat_id in materials:
#                         craft_controls.append(ft.Text(f" • {mat_name} x {mat_amount}", size=14))
                
#                 # 5-2. 전체 제작 트리 시각화 (가로 스크롤 Row 컨테이너)
#                 series_items = Search.get_craft_series(craft_name)
#                 if series_items:
#                     craft_controls.append(ft.Container(height=10)) # 간격 띄우기
#                     craft_controls.append(ft.Text("제작 트리:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
                    
#                     tree_controls = []
#                     for i, (prog, t_item_id, t_item_name) in enumerate(series_items):
#                         # 아이템 사이 화살표 아이콘
#                         if i > 0:
#                             tree_controls.append(
#                                 ft.Container(content=ft.Icon(ft.Icons.ARROW_RIGHT, size=20, color=ft.Colors.GREY_400), alignment=ft.Alignment.CENTER)
#                             )
                        
#                         t_image_url = image_url_template.replace("Item_Id", str(t_item_id))
                        
#                         # 현재 선택된 아이템의 테두리는 시각적으로 강조
#                         is_current = (t_item_id == item_id)
#                         border_color = ft.Colors.PURPLE_400 if is_current else ft.Colors.GREY_600
#                         border_width = 2 if is_current else 1
                        
#                         tree_controls.append(
#                             ft.Column([
#                                 ft.Container(
#                                     content=ft.Image(src=t_image_url, width=50, height=50, fit=ft.BoxFit.NONE, error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50)),
#                                     border=ft.Border.all(width=border_width, color=border_color),
#                                     border_radius=ft.BorderRadius.all(5)
#                                 ),
#                                 ft.Text(f"{prog}단계", size=12, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE if is_current else ft.Colors.GREY_400)
#                             ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
#                         )
                    
#                     # 아이템 트리가 길어질 것을 대비해 가로 스크롤 설정 적용
#                     craft_controls.append(
#                         ft.Row(controls=tree_controls, scroll=ft.ScrollMode.ADAPTIVE, vertical_alignment=ft.CrossAxisAlignment.CENTER)
#                     )
                
#                 list_controls.append(
#                     ft.Container(content=ft.Column(controls=craft_controls), margin=ft.Margin.only(top=15, bottom=5))
#                 )

#         # 6. 최종 ListView 조립 및 삽입
#         ColumnLi.controls.append(
#             ft.ListView(
#                 controls=list_controls,
#                 spacing=10,
#                 expand=True
#             )
#         )
        
#         return close_btn
    
#     @staticmethod
#     def build_FPInfo_detail():
#         return
    
#     @staticmethod
#     def build_SelectFP_detail(item_id: int, item_name: str, item_info):

#         # 1. 화면 탭 및 기본 데이터 설정
#         DetailTab = Asset.Controls["DetailTab"].current

#         image_url_template = os.getenv("ITEM_IMAGE_URL")
#         image_url = image_url_template.replace("Item_Id", str(item_id))

#         base_info_text = Sort.sort_item_base_info(item_info)

#         close_btn = ft.Button(
#             content="X",
#             height=50, width=50,
#             align=ft.Alignment.CENTER_RIGHT
#         )

#         ColumnLi = DetailTab.content.content
#         ColumnLi.controls.clear()
#         ColumnLi.alignment = None
        
#         # 2. 기본 정보 및 이미지 블록 배치
#         list_controls = [
#             ft.Row(
#                 controls=[
#                     ft.Container(
#                         content=ft.Image(
#                             src=image_url,
#                             width=100, height=100,
#                             fit=ft.BoxFit.NONE,  
#                             error_content=ft.Image(src="Assets/Placeholder.png", width=100, height=100),
#                         ),
#                         border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
#                         border_radius=ft.BorderRadius.all(10)
#                     ),
#                     ft.Column(
#                         controls=[
#                             ft.Text(value=item_name, weight=ft.FontWeight.BOLD, size=25, align=ft.Alignment.TOP_LEFT),
#                             ft.Text(value=base_info_text, size=15, align=ft.Alignment.TOP_LEFT)
#                         ],
#                         alignment=ft.MainAxisAlignment.START,
#                         height=100
#                     ),
#                     ft.Container(content=close_btn, expand=True)
#                 ],
#                 expand=True,
#                 alignment=ft.MainAxisAlignment.START
#             )
#         ]

#         # --- 찜 목록 UI 구성 시작 ---
#         user_id = Asset.Info.get("Userid")
        
#         favorite_pins = User.get_favorite_pins(user_id) if user_id else []

#         # 1) 기존 찜 목록 선택 드롭다운
#         pin_dropdown = ft.Dropdown(
#             label="기존 찜 목록 선택",
#             options=[ft.dropdown.Option(key=str(pin["Pin_Id"]), text=pin["Pin_Name"]) for pin in favorite_pins],
#             expand=1
#         )

#         # 2) 새 찜 목록 이름 입력창
#         new_pin_input = ft.TextField(
#             label="새 찜 목록 이름 (선택 시 무시됨)", 
#             expand=1
#         )
        
#         # 3) 찜 Log 텍스트
#         pin_log = ft.Text(value="", size=14, weight=ft.FontWeight.BOLD)

#         # 4) 찜 추가 버튼 클릭 이벤트 핸들러
#         def on_add_to_pin_click(e):
#             pin_id = pin_dropdown.value
#             new_pin_name = new_pin_input.value
            
#             # 입력값 검증
#             if not pin_id and not new_pin_name:
#                 pin_log.value = "기존 찜 목록을 선택하거나 새 이름을 입력해주세요."
#                 pin_log.color = ft.Colors.RED_400
#                 e.control.page.update()
#                 return
            
#             # 새 찜 목록 생성 분기 (이름 입력이 우선)
#             if not pin_id and new_pin_name:
#                 # User 모듈에서 새 찜 목록을 생성하고 새로 발급된 Pin_Id를 반환한다고 가정
#                 pin_id = User.create_favorite_pin(user_id, new_pin_name)
#                 pin_name_to_show = new_pin_name
#             else:
#                 # 기존 찜 목록 이름 추출
#                 pin_name_to_show = next((p.text for p in pin_dropdown.options if p.key == pin_id), "알 수 없는 찜 목록")
            
#             # 중복 검사 로직 (User 모듈의 메서드 가정)
#             # 스키마 상 Pin_Data는 Craftable_Item을 참조하므로, 추가적인 파라미터가 필요할 수 있습니다.
#             is_exist = User.check_item_in_pin(pin_id, user_id, item_id)
            
#             if is_exist:
#                 pin_log.value = "이미 찜 목록에 추가된 아이템입니다."
#                 pin_log.color = ft.Colors.RED_400
#             else:
#                 User.add_item_to_pin(pin_id, user_id, item_id)
#                 pin_log.value = f"{pin_name_to_show}에 추가 되었습니다."
#                 pin_log.color = ft.Colors.GREEN_400
#                 Asset.Controls["UserTab"].current.content = Asset.User_Info()
            
#             e.control.page.update()

#         add_btn = ft.ElevatedButton("찜 추가", on_click=on_add_to_pin_click, height=50)

#         # UI 레이아웃을 list_controls 리스트에 추가
#         list_controls.append(
#             ft.Container(
#                 content=ft.Column(
#                     controls=[
#                         ft.Row([pin_dropdown, new_pin_input]),
#                         ft.Row([add_btn, pin_log], alignment=ft.MainAxisAlignment.START)
#                     ],
#                     spacing=10
#                 ),
#                 margin=ft.Margin.only(top=20)
#             )
#         )
#         # --- 찜 목록 UI 구성 끝 ---

        

#         # 6. 최종 ListView 조립 및 삽입
#         ColumnLi.controls.append(
#             ft.ListView(
#                 controls=list_controls,
#                 spacing=10,
#                 expand=True
#             )
#         )
        
#         return close_btn

import flet as ft
from dotenv import load_dotenv
from Service import Sort, Search
from DuckDB import Item, User
import os

class Asset:

    load_dotenv()

    Info = {
        "User" : None,
        "Userid" : None
    }

    Controls = {
        # 탭
        "UserTab" : ft.Ref[ft.Container](),
        "SearchTab" : ft.Ref[ft.Container](),
        "DetailTab" : ft.Ref[ft.Container](),

        # 사용자
        "IDBar" : ft.Ref[ft.TextField](),
        "PasswordBar" : ft.Ref[ft.TextField](),
        "LoginButton" : ft.Ref[ft.Button](),
        "RegisterButton" : ft.Ref[ft.Button](),
        "LogoutButton" : ft.Ref[ft.Button](),
        "RecentItemView" : ft.Ref[ft.ListView](),
        "FPList" : ft.Ref[ft.ListView](),

        # 검색
        "SearchBar" : ft.Ref[ft.TextField](),
        "SearchButton" : ft.Ref[ft.ElevatedButton](),
        "Results" : ft.Ref[ft.ListView]()
    }

    RecentItems = []

    # 로그인 창 재할당
    @staticmethod
    def Login_Tab():
        return ft.Column(
                controls=[
                    # 타이틀
                    ft.Row(
                        height=50,
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    value="⚔️Dekaron Crafting Item Table🛠️",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    no_wrap=True,
                                    expand=True
                                ),
                                alignment=ft.Alignment.CENTER,
                                expand=True
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.TextField(
                                label="아이디",
                                border_radius=ft.BorderRadius.all(10),
                                border_color=ft.Colors.GREY_600,
                                expand=True,
                                ref=Asset.Controls["IDBar"]
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.TextField(
                                label="패스워드",
                                border_radius=ft.BorderRadius.all(10),
                                border_color=ft.Colors.GREY_600,
                                password=True,
                                can_reveal_password=True,
                                expand=True,
                                ref=Asset.Controls["PasswordBar"]
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(
                                content="로그인",
                                expand=True,
                                ref=Asset.Controls["LoginButton"]
                            ),
                            ft.Button(
                                content="회원가입",
                                expand=True,
                                ref=Asset.Controls["RegisterButton"]
                            )
                        ]
                    )
            ]
        )

    @classmethod
    def User_Info(cls):
        username = cls.Info["User"]
        userid = cls.Info["Userid"]

        # 1. 최근 탐색 목록 컨트롤 생성
        recent_controls = []
        if not cls.RecentItems:
            recent_controls.append(ft.Text("최근 탐색한 아이템이 없습니다.", color=ft.Colors.GREY_500))
        else:
            for item in cls.RecentItems:
                recent_controls.append(
                    ft.ElevatedButton(
                        item['name'],
                        icon=ft.Icons.HISTORY,
                        # on_click=lambda e, i=item['id']: [아이템 상세 보기 로직 연결]
                    )
                )

        # 2. 찜 목록(Favorite Pin) 컨트롤 생성
        fp_controls = []
        favorite_pins = User.get_favorite_pins(userid)
        if not favorite_pins:
            fp_controls.append(ft.Text("찜한 목록이 없습니다.", color=ft.Colors.GREY_500))
        else:
            for pin in favorite_pins:
                # Pin_Name이 없을 경우 Pin_Id로 대체 표시
                display_name = pin['Pin_Name'] if pin['Pin_Name'] else f"저장된 항목 #{pin['Pin_Id']}"
                fp_controls.append(
                    ft.ElevatedButton(
                        display_name,
                        icon=ft.Icons.STAR,
                        icon_color=ft.Colors.YELLOW_500,
                        # on_click=lambda e, p_id=pin['Pin_Id']: [찜 항목 불러오기 로직 연결]
                    )
                )

        return ft.Column(
            controls=[
                # 타이틀
                ft.Row(
                    height=50,
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                value="⚔️Dekaron Crafting Item Table🛠️",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                no_wrap=True,
                                expand=True
                            ),
                            alignment=ft.Alignment.CENTER,
                            expand=True
                        )
                    ]
                ),
                # 유저 이름
                ft.Row(
                    controls=[
                        ft.Text(
                            value=f"{username} (Id : {userid})",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            no_wrap=True,
                            expand=True
                        )
                    ]
                ),
                # 로그아웃 버튼
                ft.Row(
                    controls=[
                        ft.Button(
                            content=ft.Text("로그아웃"),
                            expand=True,
                            ref=cls.Controls["LogoutButton"]
                        ),
                    ]
                ),
                # 리스트 뷰 영역
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Column(
                            expand=True,
                            controls=[
                                ft.Text("🕒 최근 탐색 아이템", weight=ft.FontWeight.BOLD),
                                ft.ListView(
                                    expand=1,
                                    ref=cls.Controls["RecentItemView"],
                                    height=200,
                                    controls=recent_controls,
                                ),
                                ft.Divider(),
                                ft.Text("⭐ 찜 목록", weight=ft.FontWeight.BOLD),
                                ft.ListView(
                                    expand=1,
                                    ref=cls.Controls["FPList"],
                                    height=200,
                                    controls=fp_controls,
                                )
                            ]
                        )
                    ]
                )
            ]
        )
# --------------------------------------------------
#   Inner Method
# --------------------------------------------------


    def SetRatio(isopen : str):
        SearchTab = Asset.Controls["SearchTab"].current
        DetailTab = Asset.Controls["DetailTab"].current

        if isopen == "open":
            SearchTab.expand = 1
            DetailTab.expand = 3
        elif isopen == "close":
            SearchTab.expand = 2
            DetailTab.expand = 0
            DetailTab.content = ft.Divider(height=0)

    def build_Loading(val : str):
        DetailTab = Asset.Controls["DetailTab"].current
        DetailTab.expend = 0

        DetailTab.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=f"{val}을(를) 로딩하고 있습니다",
                        align=ft.Alignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            ft.ProgressRing(
                                width=50, height=50,
                                align=ft.Alignment.CENTER,
                                expand=True
                            )
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            ),
            padding=ft.Padding.all(20),
            alignment=ft.Alignment.CENTER,
            expand=3
        )

    @classmethod
    def add_recent_item(cls, item_id, item_name):
        """아이템을 검색/열람할 때 호출하여 최근 목록을 갱신합니다."""
        # 이미 목록에 있다면 제거 (중복 방지)
        cls.RecentItems = [item for item in cls.RecentItems if item['id'] != item_id]
        # 맨 앞에 새 아이템 추가
        cls.RecentItems.insert(0, {'id': item_id, 'name': item_name})
        
        # 목록이 너무 길어지는 것을 방지 (예: 최대 20개 유지)
        if len(cls.RecentItems) > 20:
            cls.RecentItems.pop()

            

# --------------------------------------------------
#   Static Method
# --------------------------------------------------

    @staticmethod
    def initalization():
        return ft.Row(
            controls=[
                # 사용자 정보
                ft.Container(
                    expand=1,
                    bgcolor=ft.Colors.BLACK_87,
                    ref=Asset.Controls["UserTab"],
                    content=ft.Container(
                        padding=ft.Padding.all(20),
                        content=Asset.Login_Tab()
                    )
                ),

                # 아이템 검색 창
                ft.Container(
                    expand=2,
                    bgcolor=ft.Colors.BLACK_12,
                    ref=Asset.Controls["SearchTab"],
                    content=ft.Container(
                        padding=ft.Padding.all(20),
                        content=ft.Column(
                            # 검색 바
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.TextField(
                                            label="검색어 입력",
                                            expand=True,
                                            border_radius=ft.BorderRadius.all(10),
                                            border_color=ft.Colors.GREY_600,
                                            ref=Asset.Controls["SearchBar"]
                                        ),
                                        ft.ElevatedButton("검색", ref=Asset.Controls["SearchButton"])
                                    ]
                                ),
                                # 검색 결과
                                ft.Container(
                                    expand=True,
                                    content=ft.ListView(
                                        expand=True,
                                        spacing=10,
                                        ref=Asset.Controls["Results"]
                                    )
                                )
                            ]
                        )
                    )
                ),
                # 아이템 세부 정보 혹은 찜 목록 정보
                ft.Container(
                    ref=Asset.Controls["DetailTab"],
                    expand = 0,
                    # 임시
                    content=ft.Divider(
                        height=0
                    )
                )
            ],
            expand=True
    )
    
    @staticmethod
    def build_item_card(item_id: int, item_name: str):
        image_url_template = os.getenv("ITEM_IMAGE_URL")
        image_url = image_url_template.replace("Item_Id", str(item_id))

        card = ft.Card(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src=image_url,
                                width=50,
                                height=50,
                                fit=ft.BoxFit.NONE,
                                error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50),
                            ),
                            border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
                            border_radius=ft.BorderRadius.all(10)
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    item_name,
                                    weight=ft.FontWeight.BOLD,
                                    size=20
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft. Container(
                                    content=ft.ElevatedButton(
                                        content="세부 정보",
                                        icon=ft.Icons.PLAY_ARROW,
                                        icon_color=ft.Colors.GREY_600,
                                        data={
                                            "Item_Id" : item_id,
                                            "Item_Name" : item_name
                                        }
                                    ),
                                    alignment=ft.Alignment.CENTER_RIGHT,
                                    width=140
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            expand=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                padding=10,
                border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
                border_radius=ft.BorderRadius.all(10)
            )
        )

        if Item.is_craftable_item(item_id) :
            card.content.content.controls[2].controls.append(
                ft.Container(
                    content=ft.ElevatedButton(
                        content="",
                        icon=ft.Icons.STAR,
                        icon_color=ft.Colors.GREY_600,
                        data={
                            "Item_Id" : item_id,
                            "Item_Name" : item_name
                        }
                    ),
                    alignment=ft.Alignment.CENTER_RIGHT,
                    width=60
                )
            )



        return card
    
    
    @staticmethod
    def set_up_detail(Type : str = None):
        Asset.SetRatio("open")
        Asset.build_Loading(Type)

    @staticmethod
    def close_detail():
        Asset.SetRatio("close")
    
    @staticmethod
    def build_item_detail(item_id: int, item_name: str, item_info):
        # 1. 화면 탭 및 기본 데이터 설정
        DetailTab = Asset.Controls["DetailTab"].current

        image_url_template = os.getenv("ITEM_IMAGE_URL")
        image_url = image_url_template.replace("Item_Id", str(item_id))

        base_info_text = Sort.sort_item_base_info(item_info)

        close_btn = ft.Button(
            content="X",
            height=50, width=50,
            align=ft.Alignment.CENTER_RIGHT
        )

        ColumnLi = DetailTab.content.content
        ColumnLi.controls.clear()
        ColumnLi.alignment = None
        
        # 2. 기본 정보 및 이미지 블록 배치
        list_controls = [
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=image_url,
                            width=100, height=100,
                            fit=ft.BoxFit.NONE,  
                            error_content=ft.Image(src="Assets/Placeholder.png", width=100, height=100),
                        ),
                        border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
                        border_radius=ft.BorderRadius.all(10)
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(value=item_name, weight=ft.FontWeight.BOLD, size=25, align=ft.Alignment.TOP_LEFT),
                            ft.Text(value=base_info_text, size=15, align=ft.Alignment.TOP_LEFT)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        height=100
                    ),
                    ft.Container(content=close_btn, expand=True)
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START
            )
        ]

        # 3. '추가 옵션' 세부 정보 추출 및 배치
        additional_options = Sort.extract_additional_options(item_info)
        if additional_options:
            opt_controls = [ft.Text("추가 옵션", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.BLUE_300)]
            for key, val in additional_options.items():
                opt_controls.append(ft.Row([ft.Text(f"• {key} :", weight=ft.FontWeight.W_500, size=14), ft.Text(f"{val}", size=14)]))
            
            list_controls.append(
                ft.Container(content=ft.Column(controls=opt_controls), margin=ft.Margin.only(top=15, bottom=5))
            )

        # 4. 획득 경로 및 드랍 정보 표기 (Service 계층 간접 호출)
        obtain_paths = Search.get_item_obtain_paths(item_id)
        
        if obtain_paths:
            path_str = ", ".join(obtain_paths)
            list_controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text("획득 경로", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.GREEN_300),
                        ft.Text(path_str, size=14)
                    ]),
                    margin=ft.Margin.only(top=10, bottom=5)
                )
            )

            # 경로에 'Droppable'이 포함되어 있으면 드랍 맵/몬스터 표시
            if "Droppable" in obtain_paths:
                drop_data = Search.get_item_drop_info(item_id)
                if drop_data:
                    formatted_drops = Sort.format_drop_info(drop_data)
                    drop_controls = [ft.Text("📍 드랍 정보 (맵별 몬스터)", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.ORANGE_300)]
                    
                    for loc, monsters in formatted_drops.items():
                        monsters_str = ", ".join(monsters)
                        drop_controls.append(ft.Text(f"[{loc}] : {monsters_str}", size=14))
                        
                    list_controls.append(
                        ft.Container(content=ft.Column(controls=drop_controls), margin=ft.Margin.only(left=10, top=5))
                    )

        # 5. 제작 정보(필요 재료, 제작 경로) 및 전체 제작 트리 시각화
        craft_info_list = Search.get_craft_info(item_id)
        if craft_info_list:
            # 반환받는 튜플을 3개(craft_name, craft_progress, craft_type)로 언패킹
            for craft_name, craft_progress, craft_type in craft_info_list:
                craft_controls = [
                    ft.Text(f"🛠️ 제작 정보 ({craft_name})", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.PURPLE_300),
                    # 제작 경로 추가
                    ft.Text(f"📍 제작 장소/경로 : {craft_type}", weight=ft.FontWeight.W_500, size=14, color=ft.Colors.TEAL_300)
                ]
                
                # 5-1. 해당 아이템의 필요 제작 재료
                materials = Search.get_craft_materials(craft_name, item_id)
                if materials:
                    craft_controls.append(ft.Container(height=5)) # 약간의 간격 띄우기
                    craft_controls.append(ft.Text("필요 재료:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
                    for mat_name, mat_amount, mat_id in materials:
                        craft_controls.append(ft.Text(f" • {mat_name} x {mat_amount}", size=14))
                
                # 5-2. 전체 제작 트리 시각화 (가로 스크롤 Row 컨테이너)
                series_items = Search.get_craft_series(craft_name)
                if series_items:
                    craft_controls.append(ft.Container(height=10)) # 간격 띄우기
                    craft_controls.append(ft.Text("제작 트리:", weight=ft.FontWeight.BOLD, size=14, color=ft.Colors.YELLOW_300))
                    
                    tree_controls = []
                    for i, (prog, t_item_id, t_item_name) in enumerate(series_items):
                        # 아이템 사이 화살표 아이콘
                        if i > 0:
                            tree_controls.append(
                                ft.Container(content=ft.Icon(ft.Icons.ARROW_RIGHT, size=20, color=ft.Colors.GREY_400), alignment=ft.Alignment.CENTER)
                            )
                        
                        t_image_url = image_url_template.replace("Item_Id", str(t_item_id))
                        
                        # 현재 선택된 아이템의 테두리는 시각적으로 강조
                        is_current = (t_item_id == item_id)
                        border_color = ft.Colors.PURPLE_400 if is_current else ft.Colors.GREY_600
                        border_width = 2 if is_current else 1
                        
                        tree_controls.append(
                            ft.Column([
                                ft.Container(
                                    content=ft.Image(src=t_image_url, width=50, height=50, fit=ft.BoxFit.NONE, error_content=ft.Image(src="Assets/Placeholder.png", width=50, height=50)),
                                    border=ft.Border.all(width=border_width, color=border_color),
                                    border_radius=ft.BorderRadius.all(5)
                                ),
                                ft.Text(f"{prog}단계", size=12, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE if is_current else ft.Colors.GREY_400)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
                        )
                    
                    # 아이템 트리가 길어질 것을 대비해 가로 스크롤 설정 적용
                    craft_controls.append(
                        ft.Row(controls=tree_controls, scroll=ft.ScrollMode.ADAPTIVE, vertical_alignment=ft.CrossAxisAlignment.CENTER)
                    )
                
                list_controls.append(
                    ft.Container(content=ft.Column(controls=craft_controls), margin=ft.Margin.only(top=15, bottom=5))
                )

        # 6. 최종 ListView 조립 및 삽입
        ColumnLi.controls.append(
            ft.ListView(
                controls=list_controls,
                spacing=10,
                expand=True
            )
        )
        
        return close_btn
    
    @staticmethod
    def build_FPInfo_detail():
        return
    
    @staticmethod
    def build_SelectFP_detail(item_id: int, item_name: str, item_info):

        # 1. 화면 탭 및 기본 데이터 설정
        DetailTab = Asset.Controls["DetailTab"].current

        image_url_template = os.getenv("ITEM_IMAGE_URL")
        image_url = image_url_template.replace("Item_Id", str(item_id))

        base_info_text = Sort.sort_item_base_info(item_info)

        close_btn = ft.Button(
            content="X",
            height=50, width=50,
            align=ft.Alignment.CENTER_RIGHT
        )

        ColumnLi = DetailTab.content.content
        ColumnLi.controls.clear()
        ColumnLi.alignment = None
        
        # 2. 기본 정보 및 이미지 블록 배치
        list_controls = [
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=image_url,
                            width=100, height=100,
                            fit=ft.BoxFit.NONE,  
                            error_content=ft.Image(src="Assets/Placeholder.png", width=100, height=100),
                        ),
                        border=ft.Border.all(width=1, color=ft.Colors.GREY_600),
                        border_radius=ft.BorderRadius.all(10)
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(value=item_name, weight=ft.FontWeight.BOLD, size=25, align=ft.Alignment.TOP_LEFT),
                            ft.Text(value=base_info_text, size=15, align=ft.Alignment.TOP_LEFT)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        height=100
                    ),
                    ft.Container(content=close_btn, expand=True)
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START
            )
        ]

        # --- 찜 목록 UI 구성 시작 ---
        user_id = Asset.Info.get("Userid")
        
        favorite_pins = User.get_favorite_pins(user_id) if user_id else []

        # 1) 기존 찜 목록 선택 드롭다운
        pin_dropdown = ft.Dropdown(
            label="기존 찜 목록 선택",
            options=[ft.dropdown.Option(key=str(pin["Pin_Id"]), text=pin["Pin_Name"]) for pin in favorite_pins],
            expand=1
        )

        # 2) 새 찜 목록 이름 입력창
        new_pin_input = ft.TextField(
            label="새 찜 목록 이름 (선택 시 무시됨)", 
            expand=1
        )
        
        # 3) 찜 Log 텍스트
        pin_log = ft.Text(value="", size=14, weight=ft.FontWeight.BOLD)

        # 4) 찜 추가 버튼 클릭 이벤트 핸들러
        def on_add_to_pin_click(e):
            pin_id = pin_dropdown.value
            new_pin_name = new_pin_input.value
            
            # 입력값 검증
            if not pin_id and not new_pin_name:
                pin_log.value = "기존 찜 목록을 선택하거나 새 이름을 입력해주세요."
                pin_log.color = ft.Colors.RED_400
                e.control.page.update()
                return
            
            # 새 찜 목록 생성 분기 (이름 입력이 우선)
            if not pin_id and new_pin_name:
                # User 모듈에서 새 찜 목록을 생성하고 새로 발급된 Pin_Id를 반환한다고 가정
                pin_id = User.create_favorite_pin(user_id, new_pin_name)
                pin_name_to_show = new_pin_name
            else:
                # 기존 찜 목록 이름 추출
                pin_name_to_show = next((p.text for p in pin_dropdown.options if p.key == pin_id), "알 수 없는 찜 목록")
            
            # 중복 검사 로직 (User 모듈의 메서드 가정)
            # 스키마 상 Pin_Data는 Craftable_Item을 참조하므로, 추가적인 파라미터가 필요할 수 있습니다.
            is_exist = User.check_item_in_pin(pin_id, user_id, item_id)
            
            if is_exist:
                pin_log.value = "이미 찜 목록에 추가된 아이템입니다."
                pin_log.color = ft.Colors.RED_400
            else:
                User.add_item_to_pin(pin_id, user_id, item_id)
                pin_log.value = f"{pin_name_to_show}에 추가 되었습니다."
                pin_log.color = ft.Colors.GREEN_400
                Asset.Controls["UserTab"].current.content = Asset.User_Info()
            
            e.control.page.update()

        add_btn = ft.ElevatedButton("찜 추가", on_click=on_add_to_pin_click, height=50)

        # UI 레이아웃을 list_controls 리스트에 추가
        list_controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row([pin_dropdown, new_pin_input]),
                        ft.Row([add_btn, pin_log], alignment=ft.MainAxisAlignment.START)
                    ],
                    spacing=10
                ),
                margin=ft.Margin.only(top=20)
            )
        )
        # --- 찜 목록 UI 구성 끝 ---

        

        # 6. 최종 ListView 조립 및 삽입
        ColumnLi.controls.append(
            ft.ListView(
                controls=list_controls,
                spacing=10,
                expand=True
            )
        )
        
        return close_btn