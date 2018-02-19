class Contact:

	def __init__(self):
		self.name
		self.lastname
		self.age
		self.contacs_list = []
		print 'attributes well setted' 


	def add(self, name, lastname, age):
		contacts = {
			'name': name,
			'lastname': lastname,
			'age': age
		}
		self.contacs_list.append(contacts)



	def show(self):
		for contact in self.contacts:
			print 'Full name:{0} {1} and age: {2}' format(contact.name, contact.lastname, contact.age)