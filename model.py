from imodel import IModel
from google.appengine.ext import ndb

builtin_list = list

#[Start Model]
class review(ndb.Model):
	coursename = ndb.StringProperty()
	instructor = ndb.StringProperty()
	ratings = ndb.StringProperty()
	reviews = ndb.StringProperty()
	termyear = ndb.StringProperty()
#[End model]

#[Start od data_store]
def from_datastore(entity):
	if not entity:
		return None
	if isinstance(entity, builtin_list):
		entity = entity.pop()
	data = {}
	data['coursename']= entity.coursename
	data['instructor']= entity.instructor 
	data['ratings']= entity.ratings
	data['reviews'] = entity.reviews
	data['termyear'] = entity.termyear
	return data
#[end_of_datastore]

#[Start_list]
def list(limit= 100):
	query = review.query()
	entities = query.fetch(limit)
	entities = builtin_list(map(from_datastore, entities))
	return entities 

#[end_list]

def insert(cn, ins, rat, re, ty):
	data = review()
	data.coursename = cn
	data.instructor = ins
	data.ratings = rat
	data.reviews = re
	data.termyear = ty
	data.put()
	

		
		
