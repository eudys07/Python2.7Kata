from Contact import Contact

class FileContactManager:

	file_name='contact.txt'


	def add(self, contact):
		file = open(file_name, 'a+')
		f.write('python rules')
		f.close()


	def read_all(self):
		file = open(file_name, 'r+')
		f.close()


	def read(self, contact_id):
		file = open(file_name, 'r+')
		f.close()


	def delete(self, contact_id):
		file = open(file_name, 'w+')
		f.close()
