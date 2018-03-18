import json

class FileContactManager:

	FILE_NAME='contact.txt'


	def add(self, contact):
		print contact
		contacts = self.read_all()
		print 'loading contact'
		print contacts
		file = open(self.FILE_NAME, 'a+')
		print 'python test'
		contact_to_write = file.write(json.dumps(contact))
		contacts.append(contact_to_write)
		file.close()


	def read_all(self):
		file = open(self.FILE_NAME, 'r+')
		print file
		contacts = json.loads(file.read())
		print contacts
		file.close()
		return contacts


	def read(self, contact_id):
		file = open(self.FILE_NAME, 'r+')
		file.close()


	def delete(self, contact_id):
		file = open(self.FILE_NAME, 'w+')
		file.close()


	def is_empty_file(self):
		import os
		os.stat(self.FILE_NAME).st_size == 0
