import urllib.request, json
from flask import Flask

#retrieve url object and store it.
urlobj = urllib.request.urlopen(
    'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

#read the contents of url page and store it.
byte_code = urlobj.read()

#Parse JSON into Python dictionary and store it.
py_dict = json.loads(byte_code.decode()) 

#declare a string.
string_to_display = '<img src="'+ py_dict['hdurl'] +'" alt="no image found " width="500" height="400"> <br>'

#append said string with all the values from py_dict.
for data_type, description in py_dict.items():
    string_to_display+= '<strong>' + data_type + '</strong>' + ': ' + description + '<br>'

#instanciate Flask object.
app = Flask('__name__')

#return the string to the page.
@app.route('/')
def index():
    return string_to_display

if __name__ == '__main__':
    app.run()
