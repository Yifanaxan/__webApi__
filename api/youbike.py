from . import api01

@api01.route("/youbike")
def youbike():
    return "<h1> Hello! Youbike </h1>"