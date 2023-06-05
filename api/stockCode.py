from . import api01
import pandas as pd
from flask import jsonify
import json

@api01.route("/stockCode")
def stockCode():
    code_dataFrame = pd.read_csv("api/codeSearch.csv", encoding='utf-8')
    code_dataFrame = code_dataFrame[['code','name']]
    #code_dataFrame
    #code_dataFrame.values
    all_list = code_dataFrame.values.tolist()
    python_list = [{item[0]:item[1]} for item in all_list]

    # Convert the Python list to a JSON string
    #json_data = json.dumps(python_list, ensure_ascii=False)

    return json.dumps(python_list, ensure_ascii=False)


@api01.route("/stockCode/<int:code>")
def stockName(code):
    code_dataFrame = pd.read_csv("api/codeSearch.csv")
    code_dataFrame = code_dataFrame[['code','name']]
    try:
        name = code_dataFrame.query('code == @code')['name'].values[0]

    except IndexError:
        return f"豬頭沒有{code}"
    

    return name