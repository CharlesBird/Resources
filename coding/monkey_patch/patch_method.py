def propagate(method1, method2):
	if method1:
		for attr in ('_returns',):
			if hasattr(method1, attr) and not hasattr(method2, attr):
				setattr(method2, attr, getattr(method1, attr))
	return method2



class BaseModel(object):

	@classmethod
	def _patch_method(cls, name, method):
		origin = getattr(cls, name)
		method.origin = origin
		wrapped = propagate(origin, method)
		wrapped.origin = origin
		setattr(cls, name, wrapped)

	def foo1(self, values=None):
		print('ff1')


class TestModel(BaseModel):


	def do_foo1(self, values=None):
		print('ff2')
		def inner_dofoo(self, values=None):
			res = inner_dofoo.origin(self, values)
			return res
		return inner_dofoo

	def _patch_methods(self):
		self._patch_method('foo1', self.do_foo1())


tm = TestModel()
tm._patch_methods()
tm.foo1()