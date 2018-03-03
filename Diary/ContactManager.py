from Contact import Contact
from EditContact import EditContact
from ContactException import ContactException

class ContactManager:


	def __init__(self):
		self.contact = Contact()


	def show_contacts(self):
		self.contact.show()
		print
		self.show_menu()


	def add_contact(self):
		self.ask_contact_info()
		self.contact.add()
		print
		self.show_menu()


	def edit_contact(self):
		
		try :
			edit_contact = EditContact()
			print 'Please type the contact Id That You Would like to edit:'
			contact_id = raw_input()
			print 'What Would you like edit: [name] - [lastname] - [age]'
			edit_attribute = raw_input()
			print 'Which the value that you want to add in your ', edit_attribute
			edit_new_value = raw_input()

			edit_contact.contact_id = contact_id
			edit_contact.edit_attribute = edit_attribute
			edit_contact.new_value = edit_new_value

			print 'printing edit_contact before call edit in contact'
			print edit_contact

			self.contact.edit(edit_contact)
			self.contact.show()

		except Exception as e:
			raise ContactException 
		

	def delete_contact(self):
		print 'Please type the contact Id That You Would like to delete:'
		contact_id = raw_input()
		if contact_id.isdigit() :
			self.contact.delete(contact_id);
		else:
			print 'Please try to type a number instead'


	def ask_contact_info(self):		
		print 'Please type your ID: '
		contact_id = raw_input()
		print 'Please type your name: '
		name = raw_input()
		print 'Please type your lastname: '
		lastname = raw_input()
		print 'Please type your age: '
		age = raw_input()

		print 'Full name:{0} {1} and age: {2}'.format(contact_id, name, lastname, age)
		self.contact = Contact(contact_id, name, lastname, age)		


	def show_menu(self):
		print "----------------------------------------------"
		print "--------------MAIN MENU-----------------------"
		print "-----------1-Show Contacts--------------------"
		print "-----------2-Add Contact----------------------"
		print "-----------3-Edit Contact---------------------"
		print "-----------4-Delete Contact-------------------"
		print "-----------5-Salir del sistema----------------"
		print "----------------------------------------------"
		print ">>Please choose your options"
		print "----------------------------------------------"
		user_choosed = raw_input()		

		if user_choosed == '1':
			self.show_contacts()
		elif user_choosed == '2':
			self.add_contact()
		elif user_choosed == '3':
			self.edit_contact()
		elif user_choosed == '4':
			self.delete_contact()


