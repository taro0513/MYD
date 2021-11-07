class em:
    async_inspect_not_inclasss = "Only types can be raised (not instances)"
    async_invalid_thread_id = "invalid thread id"
    async_set_failed = "PyThreadState_SetAsyncExc failed"
    thread_not_active = "the thread is not active"
    thread_cant_determin = "could not determine the thread's id"
    warning_detail = "發生錯誤! 詳細資訊: %s"
    cancel_action = "取消上一步的動作!!"
    

class ctx:
    catcher_information = "名稱: %s\n介紹: %s\n分集:"
    connect_server = "嘗試連接至伺服器下載檔案: %s%s/720p.m3u8"
    connect_server_success = "連接成功! 耗時: %s"
    connect_server_failed = "連接失敗! 耗時: %s"
    connect_exceed = "重新連接超過3次! 尚未找到合適的伺服器，請稍後在試!"
    connect_best = "M3U8檔案位置: %s\n最佳伺服器位置: %s (連接時間: %s)"
    connect_best_spare = "M3U8檔案位置: %s\n最佳伺服器位置: %s (連接時間: %s)\n備用伺服器: %s (連接時間: %s)"
    connect_retry = "尚未找到合適得伺服器! 重新連接 - 第%s次!"
    connect_fast_best = "[FastMode] M3U8檔案位置: %s\n最佳伺服器位置: %s"
    connect_fast_best_spare = "[FastMode] M3U8檔案位置: %s\n最佳伺服器位置: %s\n備用伺服器: %s"

    download_list_generate = "開始生成下載清單! 排隊項目數: %s 項."
    download_list_add = "成功新增物件至隊列! 網址: %s 目標: %s"
    download_list_end = "清單建立完成!"

    select_slection = "[%s] %s"
    select_input = "請選擇要下載的集數: "

    download_check_ffmpeg = "確認必要檔案FFMPEG位置: %s"
    download_check_ffmpeg_success = "FFMPEG.exe 存在!"
    download_check_ffmpeg_failed = "FFMPEG.exe 不存在目標路徑 請去 '設定' 重新設定位置!"

    download_check_log_failed = "Log檔不存在 重新建立: %s"
    download_check_folder_failed = "目標資料夾不存在 重新建立: %s"

    download_excute_cmd = "執行系統指令 * %s *"
    download_excute_add = "排隊執行指令 網址: %s目標: %s"

    search_key = "搜尋目網址: %s"

    search_xfplay_skip = "目標包含黑名單(xfpaly) 因此無視此網址"
    search_vod_skip = "目標包含黑名單(vod) 因此無視此網址"

    search_result_name = "名稱: %s"
    search_result_description = "介紹: %s"
    search_result_picture = "圖片網址: %s"
    search_result_detail = "%s: %s"
    search_no_inforamtion = "未查找到任何資料! 請確認關鍵字是否正確: %s"

class hm:
    login_visitor ="以訪客身分登入!"
    login_accoutn ="歡迎! %s"

    login_no_enter_account = "請輸入Myself帳號!"
    login_no_enter_password = "請輸入您的密碼!"
    login_no_enter = "請輸入帳號以及密碼!"
    login_incorrect = "帳號或密碼錯誤!"

    login_not_open = "此功能尚未開放! 請使用訪客登入"

    search = "搜尋中... 目標: %s"
    search_result = "查詢結果: %s"
    search_no_result = "查無結果! 請確認輸入是否正確"

    log_add_item = "[Pyside2] 新增物件至選單"
    log_set_item = "[Pyside2] 設定物件: %s"

    select_count = "以選取目標數量: %s"

    setting_folder = "已設定 資料夾名稱: %s 對於: %s"
    setting_folder_no_input = "請輸入要新建的資料夾名稱!"

    download_list_generate = "建立下載清單中..."
    download_list_end = "清單建立完成! 可至 '下載' 查看下載清單"

    download_queue_enter = "%s 項目標進入排程"

    check_path_path = "位置: %s"

    change_path_download = "更換路徑(download) %s -> %s"
    change_path_ffmpeg = "更換路徑(ffmpeg) %s -> %s"

    open_file = "開啟目標檔案: %s"
    open_folder = "開啟目標資料夾: %s"