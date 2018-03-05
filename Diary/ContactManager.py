from Contact import Contact
from EditContact import EditContact
from ContactException import ContactException

class ContactManager:


	def __init__(self):
		self.contact = Contact()
		self.contact_edit = EditContact()


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
			if self.contact.contactsListHasValue() is not True :
				print 'No contact has been added yet. Would you like to add one?'
				print 'type [yes] to add otherwise press any key'
				answer = raw_input()
				if answer == 'yes':
					self.add_contact()
				else:
					self.show_menu()

			
			print 'Please type the contact Id That You Would like to edit:'
			self.contact_edit.contact_id = raw_input()
			print 'What Would you like edit: [name] - [lastname] - [age]'
			self.contact_edit.edit_attribute = raw_input()
			print 'Which the value that you want to add in your ', self.contact_edit.edit_attribute
			self.contact_edit.new_value = raw_input()

			print 'contact id in edit ', self.contact_edit.contact_id
			#self.contact_edit.contact_id = contact_edit_id

			print 'printing contact_edit before call edit in contact'
			print self.contact_edit

			self.contact.edit(self.contact_edit)
			print 
			print 
			self.show_menu()

		except Exception as e:
			raise ContactException(e)
		

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


