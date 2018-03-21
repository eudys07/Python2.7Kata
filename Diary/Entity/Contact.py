from EditContact import EditContact
from Manager.FileContactManager import FileContactManager as file_contact

class Contact:

	contact_id = None
	name = None
	lastname = None
	age = None
	contacts = []
	file_contact =  file_contact()


	def __init__(self, *att):
		if len(att) > 0:
			contact_list = list(att)

			self.contact_id = contact_list[0]
			self.name = contact_list[1]
			self.lastname = contact_list[2]
			self.age = contact_list[3]
		

	def add(self):
		contact = {
			'contact_id': self.contact_id,
			'name': self.name,
			'lastname': self.lastname,
			'age': self.age
		}
		self.file_contact.add(contact)
		self.contacts.append(contact)


	def show(self):
		if self.contacts_list_has_value() :
			self.file_contact.read_all()
			for contact in self.contacts:
				print 'The Contact Id {0} named {1} {2} and age {3} '.format(contact['contact_id'], contact['name'], contact['lastname'], contact['age'])
		else:
			print 'There is not contact to show'
			

	def edit(self, edit_contact):

		for contact in self.contacts:
			if contact['contact_id'] == edit_contact.contact_id :
				contact[edit_contact.edit_attribute] = edit_contact.new_value


	def delete(self, contact_id):
		for index, contact in enumerate(self.contacts):
			if contact['contact_id'] == contact_id:
				del self.contacts[index]
		

	def get_contact_by_id(self, contact_id):
		
		for contact in self.contacts:
			if contact['contact_id'] == contact_id:
				return contact


	def get_contact_size(self):
		return len(self.contacts)


	def contacts_list_has_value(self):
		return self.file_contact.is_empty_file()
