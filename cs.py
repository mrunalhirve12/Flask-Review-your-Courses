import flask
import model


class cs(flask.views.MethodView):
	
	def get(self):
		"""
		fetches data fro model to display 
		"""
		data = model.list()
		return flask.render_template('cs.html', reviews=data)
