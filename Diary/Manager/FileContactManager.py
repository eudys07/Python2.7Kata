import json

class FileContactManager:

	FILE_NAME='contact.txt'


	def add(self, contact):
		print contact
		file = open(self.FILE_NAME, 'a+')
		file.write('\n')
		print 'python test'
		file.write(json.dumps(contact))
		file.close()


	def read_all(self):
		file = open(self.FILE_NAME, 'r+')
		contacts = file.read()
		file.close()
		return contacts


	def read(self, contact_id):
		file = open(self.FILE_NAME, 'r+')
		file.close()


	def delete(self, contact_id):
		file = open(self.FILE_NAME, 'w+')
		file.close()
