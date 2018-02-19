from Contact import Contact 


class Main:

	def __init__(self):
		self.contact = Contact()

	def add_contact(self):		
		self.ask_contact_info()
		self.contact.add(self.contact.name, self.contact.lastname, self.contact.age)
		print
		print
		print
		self.show_menu()

	def show_contact(self):
		self.contact.show()
		print
		print
		print
		self.show_menu()

	def ask_contact_info(self):
		
		print 'Please type your name: '
		name = raw_input()
		print 'Please type your lastname: '
		lastname = raw_input()
		print 'Please type your age: '
		age = raw_input()

		print 'Full name:{0} {1} and age: {2}'.format(name, lastname, age)
		self.contact = Contact(name, lastname, age)
		#self.contact = Contact(name, lastname, age)

		

	def show_menu(self):
		print 'please choose one option:' 
		print '1 - Add Contact' 
		print '2 - Show contacts' 
		choosed = raw_input()		

		if choosed == '1':
			self.add_contact()
		elif choosed == '2':
			self.show_contact()



if __name__== "__main__":
	 
	main = Main()	
	main.show_menu()
	

