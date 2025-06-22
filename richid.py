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

def get_all_rich_menus_and_aliases():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        # ✅ 取得所有 Rich Menu
        response = line_bot_api.get_rich_menu_list()
        richmenus = response.richmenus  # ✅ 注意這裡是 richmenus 而不是 rich_menus
        print(f"找到 {len(richmenus)} 個 Rich Menu")
        for rm in richmenus:
            print(f"RichMenu ID：{rm.rich_menu_id}")

        # ✅ 取得所有 alias
        alias_response = line_bot_api.get_rich_menu_alias_list()
        aliases = alias_response.aliases
        print(f"找到 {len(aliases)} 個 alias")
        for alias in aliases:
            print(f"Alias ID：{alias.rich_menu_alias_id} -> RichMenu ID：{alias.rich_menu_id}")

        print("✅ 已列出所有 Rich Menu 與 alias。")

if __name__ == "__main__":
    get_all_rich_menus_and_aliases()
