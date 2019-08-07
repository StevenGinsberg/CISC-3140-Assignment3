from flask import Flask
from flask import render_template
import urllib.request
import json
import webbrowser
import ssl
 
myKey= 'api_key=fsJlsdyc50kdcOWD7gpZMfZULF7nDkxAxuSbTqAf' 
url=   'https://api.nasa.gov/EPIC/api/natural/date/2017-07-04?'
# open webservice
epurlobj1= urllib.request.urlopen(url+myKey)
#Object is read
epread1=epurlobj1.read()
#Decoding json and converting to python
decode=json.loads(epread1.decode('utf-8'))
# Url of actual image
newurl=  'https://epic.gsfc.nasa.gov/archive/natural/2017/07/04/png/'+decode[8]['image']+'.png'
app= Flask(__name__,template_folder= r'../Flaskapp/templates')
@app.route('/')
def index():
 return  render_template('index.html',my_url=newurl,capt=decode[8]['caption'],
 vers=decode[8]['version'],date=decode[8]['date'])
 if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


 
