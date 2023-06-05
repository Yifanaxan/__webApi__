from . import api01

@api01.route("/error")
def error():
    return "處理錯誤"