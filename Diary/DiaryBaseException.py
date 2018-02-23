class DiaryBaseException(Exception):
	def __init__(self, *param_tuple, **param_dict):
		Exception.__init__(self,*param_tuple, **param_dict)
