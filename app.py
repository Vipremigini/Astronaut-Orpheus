from flask import Flask, request
import requests

headers = { 'accept': 'application/json', 'Authorization': '6b0074dd01b83135bdbde3ae0ad48ee5b8b539bd' , 'Cookie': 'sessionid=6b0074dd01b83135bdbde3ae0ad48ee5b8b539bd'}

app = Flask(__name__)

@app.post("/api/try")
def trial():
  sendurl = request.form.get("response_url")
  nid = request.form.get("text")
  url = "https://db.satnogs.org/api/tle/?format=json&norad_cat_id=" + nid
  response = requests.post(url, headers=headers)
  rdata = response.json()
  
    
  return {"blocks": [    {
      "type": "section",
      "text": {
        "response_type": "in_channel",
        "type": "mrkdwn",
        "text": str(rdata)
      }
    }]}
