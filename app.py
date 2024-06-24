from flask import Flask, request
import requests
import string

app = Flask(__name__)

@app.post("/api/try")
def trial():
  sendurl = request.form.get("response_url")
  nid = request.form.get("text")
  if nid == "":
    return {"blocks": [    {
      "type": "section",
      "text": {
        "type": "plain_text",
        "text": "Please enter a NORAD ID"
      }
    }]}
  elif not nid.isdigit():
    return {"blocks": [    {
      "type": "section",
      "text": {
        "type": "plain_text",
        "text": "Please enter a valid number"
      }
    }]}
  

  url = "https://db.satnogs.org/api/tle/?format=json&norad_cat_id=" + nid
  iurl = "https://db-dev.satnogs.org/api/satellites/?norad_cat_id=" + nid
  response = requests.get(url)	
  rdata = response.json()
  ires = requests.get(iurl)
  idata = ires.json()
  

  if rdata == []:
    return {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Data Not Found"
			}
		}
	]
}
  
    
  return {
	"blocks": [
		{
			"type": "image",
			"title": {
				"type": str(rdata[0]['tle0'])
				"text": "I love tacos",
				"emoji": true
			},
			"image_url": idata[0]["image"],
			"alt_text": str(rdata[0]['tle0'])
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Name: " + str(rdata[0]['tle0'])
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "NORAD ID: " + str(rdata[0]['norad_cat_id'])
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE 1: " + str(rdata[0]['tle1'])
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE 2: " + str(rdata[0]['tle2'])
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE Source: " + str(rdata[0]['tle_source'])
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Satellite_ID: " + str(rdata[0]['sat_id'])
			}
		}
	]
}
