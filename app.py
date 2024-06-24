from flask import Flask, request
import requests

headers = { 'accept': 'application/json'}

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
        "type": "mrkdwn",
        "text": str(rtext)
      }
    }]}
