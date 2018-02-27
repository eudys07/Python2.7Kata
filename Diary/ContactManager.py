from Contact import Contact
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
			print 'Please type the contact Id That You Would like to edit:'
			contact_id = raw_input()
			
			for idx, contact in self.contacts:
				if contact_id == contact.contact_id:
					print 'What Would you like edit: [name] - [lastname] - [age]'
					edit_choose = raw_input()
					print 'Which the value that you want to add in your ', edit_choose
					edit_choose_value = raw_input()
					contact[edit_choose] = edit_choose_value
					self.contacts[idx] = contact

			
			#if contact_id.isdigit() :
			#	self.contact.edit(contact_id);
			#else:
			#	print 'Please try to type a number instead'

		except ContactException as ex:
			raise ContactException
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


