class Contact:

	name = ''
	lastname = ''
	age = ''
	contacs_list = []

	def __init__(self, *att):

		if len(att) > 0:
			contact_data = list(att)

			self.name = contact_data[0]
			self.lastname = contact_data[1]
			self.age = contact_data[2]
		
			print 'attributes well setted' 


	def add(self, name, lastname, age):
		
		print 'attributes'
		print name
		print lastname
		print age
		contact_obj = {
			'name': name,
			'lastname': lastname,
			'age': age
		}

		print 'Printing contact dict'
		print contact_obj
		self.contacs_list.append(contact_obj)



	def show(self):

		if len(self.contacs_list) <=0 :
			print 'There is not contact to show'
		else:
			for contact in self.contacs_list:
				#print contact
				print 'Full name:{0} {1} and age: {2}'.format(contact['name'], contact['lastname'], contact['age'])