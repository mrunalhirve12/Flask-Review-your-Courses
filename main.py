import flask
from auth import users
from flask.views import MethodView

class Main(MethodView):
	def get(self):
		"""
		for rendering the login page
		"""
		return flask.render_template('index.html')
	
	def post(self):
		"""
		autheticating user
		"""
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('index'))
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index'))	
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("Username does not exist or is Invalid")
		return flask.redirect(flask.url_for('index'))
