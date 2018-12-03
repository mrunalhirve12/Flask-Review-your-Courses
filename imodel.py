from abc import ABCMeta, abstractmethod

class IModel():
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def fetchall(self):
		pass

