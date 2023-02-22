from flask import Flask, jsonify, request, render_template
import json

urllink=''

app = Flask(__name__)

@app.route('/savedata', methods=['GET', "POST"]) 
def nameroute():
    global urllink
    if(request.method=="POST"):
        request_data=request.data
        request_data=json.loads(request_data.decode('utf-8'))
        urllink=request_data['url']
    return ''
    # return render_template("videoPlayer.html", url=urllink)

@app.route('/hi')
def hello():
    return "hello"

@app.errorhandler(404)
def method_name(e):
    print("ok")
    return render_template("videoPlayer.html")

@app.route('/')
def method_name():
    # urllink='https://www06.gofcdn.com/videos/hls/eAqeehYm0njIloaTEiBVtg/1676807501/190856/ca09dc1ce88568467994ea8e756c4493/ep.8.1661269167.m3u8'
    print("link: "+urllink)
    return render_template("videoPlayer.html", url=urllink)

if __name__ =="__main__":
    app.run(debug=False, host='0.0.0.0')