# Import statements necessary
from flask import Flask
import requests
import json

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def another_function():
	return 'Hello World!'

@app.route('/user/<yourname>')
def hello_name(yourname):
	return '<h1>Hello {}</h1>'.format(yourname)



# new route: /itunes/<artist>
@app.route('/itunes/<newthing>') # As long as the route and param name are the same, it's fine!
def get_itunes_data(newthing):
	# Get specifics of how to write this from knowledge about REST APIs in Python -- see textbook -- and iTunes API documentation
	baseurl = "https://itunes.apple.com/search"
	params_diction = {}
	params_diction["term"] = newthing
	resp = requests.get(baseurl,params=params_diction)
	text = resp.text
	python_obj = json.loads(text)
	album_titles = []
	for item in python_obj["results"]:
		album_titles.append("<em>" + item["collectionName"] + "</em>") # This turns out where you find the album name in the nested data
	all_titles = "<br>".join(album_titles) # join by the <br> tag, which means 'line break' in html
	# return str(album_titles)
	return all_titles
	#return a string -- must return a string to render on the page

if __name__ == '__main__':
	app.run() # Runs the flask server when you run this with python first_flas_app_solution.py runserver
