from flask import Flask
from flask import request
from flask import render_template
import json
app=Flask(__name__,static_folder="",static_url_path="")
@app.route("/")
def index():
    #获取要求字串信息
    getargs=request.args.get(key="m",default="file1-1")
    #从moivelist.json文件中取出视频链接
    with open("static/moivelist.json",mode="r",encoding="utf-8") as file:
        moivelist=json.load(file)
    moives1=moivelist["page1"]["shuxue1"]
    moives2=moivelist["page1"]["shuxue2"]
    moives3=moivelist["page1"]["shuxue3"]
    moives4=moivelist["page1"]["shuxue4"]
    moives5=moivelist["page1"]["shuxue5"]
    moives6=moivelist["page1"]["shuxue6"]
    moives7=moivelist["page1"]["shuxue7"]
    moives8=moivelist["page1"]["shuxue8"]
    moives9=moivelist["page1"]["shuxue9"]
    moives10=moivelist["page1"]["shuxue10"]
    moives11=moivelist["page1"]["shuxue11"]
    moives12=moivelist["page1"]["shuxue12"]
    urls=moivelist["page1"]["url"][getargs]
    return render_template("index.html",myurl=urls,moives1=moives1,moives2=moives2,moives3=moives3,moives4=moives4,moives5=moives5,moives6=moives6,moives7=moives7,moives8=moives8,moives9=moives9,moives10=moives10,moives11=moives11,moives12=moives12)
@app.route("/index1")
def index1():
    getargs=request.args.get(key="m",default="file1-1")
    with open("static/moivelist.json",mode="r",encoding="utf-8") as file:
        moivelist=json.load(file)
    moives1=moivelist["page2"]["yuwen1"]
    moives2=moivelist["page2"]["yuwen2"]
    moives3=moivelist["page2"]["yuwen3"]
    moives4=moivelist["page2"]["yuwen4"]
    moives5=moivelist["page2"]["yuwen5"]
    moives6=moivelist["page2"]["yuwen6"]
    moives7=moivelist["page2"]["yuwen7"]
    moives8=moivelist["page2"]["yuwen8"]
    moives9=moivelist["page2"]["yuwen9"]
    moives10=moivelist["page2"]["yuwen10"]
    moives11=moivelist["page2"]["yuwen11"]
    moives12=moivelist["page2"]["yuwen12"]
    urls=moivelist["page2"]["url"][getargs]
    return  render_template("index1.html",myurl=urls,moives1=moives1,moives2=moives2,moives3=moives3,moives4=moives4,moives5=moives5,moives6=moives6,moives7=moives7,moives8=moives8,moives9=moives9,moives11=moives11,moives12=moives12)
@app.route("/index2")
def index2():
    getargs=request.args.get(key="m",default="file5-1")
    with open("static/moivelist.json",mode="r",encoding="utf-8") as file:
        moivelist=json.load(file)
    moives5=moivelist["page3"]["yingyu5"]
    moives6=moivelist["page3"]["yingyu6"]
    moives7=moivelist["page3"]["yingyu7"]
    moives8=moivelist["page3"]["yingyu8"]
    moives9=moivelist["page3"]["yingyu9"]
    moives10=moivelist["page3"]["yingyu10"]
    moives11=moivelist["page3"]["yingyu11"]
    moives12=moivelist["page3"]["yingyu12"]
    urls=moivelist["page3"]["url"][getargs]
    return render_template("index2.html",myurl=urls,moives5=moives5,moives6=moives6,moives7=moives7,moives8=moives8,moives9=moives9,moives10=moives10,moives11=moives11,moives12=moives12)
if  __name__=="__main__":
  app.run(debug=True,host="0.0.0.0",port=8000)