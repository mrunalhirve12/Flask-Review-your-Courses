import flask
import model
from flask import request



class addcsreviews(flask.views.MethodView):
	def get(self):
		"""
		Displays the form. 
		"""
		return flask.render_template('addcsreviews.html')


	def post(self):
		"""
		posts the reviews 
		"""
		cn = request.form['cn']
		ins = request.form['ins']
		rat = request.form['rat']
		re = request.form ['re']
		ty = request.form ['ty']
		model.insert(cn, ins, rat, re, ty)
		return "Record Inserted Successfully!!"
	
