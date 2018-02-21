class Contact:

	contact_id = ''
	name = ''
	lastname = ''
	age = ''
	contacts = []


	def __init__(self, *att):
		if len(att) > 0:
			contact_list = list(att)

			self.contact_id = contact_list[0]
			self.name = contact_list[1]
			self.lastname = contact_list[2]
			self.age = contact_list[3]
		
			print 'attributes well setted' 


	def add(self):		
		print 'attributes'
		print self.contact_id
		print self.name
		print self.lastname
		print self.age
		contact = {
			'contact_id': self.contact_id,
			'name': self.name,
			'lastname': self.lastname,
			'age': self.age
		}

		print 'Printing contact dict'
		print contact
		self.contacts.append(contact)



	def show(self):
		if len(self.contacts) <=0 :
			print 'There is not contact to show'
		else:
			for contact in self.contacts:
				#print contact
				print 'Full name:{0} {1} and age: {2}'.format(contact['name'], contact['lastname'], contact['age'])


	def edit(self, contact_id):
		contact = self.contact_id['contact_id']
		print 
		print contact_id
		print 
		print contact


	def delete(self, contact_id):
		contact = self.contact_id['contact_id']
		print 
		print contact_id
		print 
		print contact