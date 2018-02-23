class ContactExceptions(DiaryBaseExceptions):
	
	def show_unfound():
		print 'Conctact does not exist.'

	def show_already_exist():
		print 'This contact already exist. Please try another one.'

	def show_empty():
		print 'The list is total empty.' 