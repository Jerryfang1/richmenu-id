import os
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi
)

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
if not channel_access_token:
    raise Exception("請設定環境變數 LINE_CHANNEL_ACCESS_TOKEN")

configuration = Configuration(access_token=channel_access_token)

def delete_all_rich_menus_and_aliases():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        # 刪除所有 Rich Menu
        richmenus = line_bot_api.get_rich_menu_list().richmenus
        print(f"找到 {len(richmenus)} 個 Rich Menu")
        for rm in richmenus:
            print(f"刪除：{rm.rich_menu_id}")
            line_bot_api.delete_rich_menu(rm.rich_menu_id)

        # 刪除所有 alias
        aliases = line_bot_api.get_rich_menu_alias_list().aliases
        print(f"找到 {len(aliases)} 個 alias")
        for alias in aliases:
            print(f"刪除 alias：{alias.rich_menu_alias_id}")
            line_bot_api.delete_rich_menu_alias(alias.rich_menu_alias_id)

        print("所有 Rich Menu 與 alias 已成功刪除。")

delete_all_rich_menus_and_aliases()
