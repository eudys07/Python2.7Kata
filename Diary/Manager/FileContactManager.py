#from Entity.Contact import Contact

class FileContactManager:

	FILE_NAME='contact.txt'


	def add(self, contact):
		print contact
		file = open(self.FILE_NAME, 'a+')

		file.write('\n')
		file.write('python test')
		file.write('\n')
		file.write('python test')
		file.close()


	def read_all(self):
		file = open(self.FILE_NAME, 'r+')
		file.close()


	def read(self, contact_id):
		file = open(self.FILE_NAME, 'r+')
		file.close()


	def delete(self, contact_id):
		file = open(self.FILE_NAME, 'w+')
		file.close()
