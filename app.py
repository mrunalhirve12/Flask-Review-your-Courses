
import flask, flask.views 
import auth
from main import Main
from cs import cs
from addcsreviews import addcsreviews 

app = flask.Flask(__name__)
app.secret_key = auth.secret_key

"""
add routes on navigation to the page
"""
app.add_url_rule('/', view_func=Main.as_view('index'), methods =["GET", "POST"])

app.add_url_rule('/cs', view_func=cs.as_view('cs'), methods = ['GET', 'POST'])

app.add_url_rule('/addcsreviews', view_func=addcsreviews.as_view('addcsreviews'), methods = ['GET', 'POST'])

app.debug=True

"""
Initializing main method to run on given host and port no
"""
if __name__ == '__main__':
	
	app.run (host= '0.0.0.0', port=8888, debug=True)

