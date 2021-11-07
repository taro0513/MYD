class dp:
    jffmpeg = "FFMPEG"
    jdownload = "Download"
    jdownloadlog = "DownloadLog"
    jMyselflog = "MyselfLog"
    jAnimeFolder = "AnimeFolder"

    server_connecttimeout = 10
    server_readtimeout = 10
    connect_exceed = 3

    m3u8_url = "%s%s/720p.m3u8"
    vpx_url = "https://v.myself-bbs.com/vpx/%s"

    download_name = "%s.mp4"

    download_cmd = "%s -i %s -c copy %s"

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    level =30