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
  response = requests.get(url)
  rdata = response.json()

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
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Name: " + rdata[0]['tle0']
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "NORAD ID: " + rdata[0]['norad_cat_id']
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE 1: " + rdata[0]['tle1']
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE 2: " + rdata[0]['tle2']
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "TLE Source: " + rdata[0]['tle_source']
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Satellite_ID: " + rdata[0]['sat_id']
			}
		}
	]
}
