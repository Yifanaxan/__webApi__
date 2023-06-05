#一定要有一個 __init__.py的檔案   代表api檔案夾的檔案


from flask import Blueprint, render_template


#api01 = Blueprint("api", __name__,url_prefix='/api')



api01 = Blueprint("api", __name__, url_prefix='/api')


from . import youbike, error, stockCode #一定要寫在api01 = Blueprint下面

@api01.route("/")
def api():
    return render_template("api.html")

