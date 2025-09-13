from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getweather", methods=["POST"])
def weather():
    if request.method == "POST":
        location = request.form["city"]
    else:
        location = "Nairobi"

    api = "3e9a233c53e58a3aa29f1b1ee9922f74"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}&units=metric"
    
    source = urllib.request.urlopen(url)
    responseData = json.load(source)

    data = {
            "location": responseData["name"],
            "temperature": f"{responseData['main']['temp']} °C"
            }
    

    return render_template("index.html", data=data)

app.run(host="0.0.0.0", port=8080, debug=True)
