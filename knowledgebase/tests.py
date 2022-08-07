from django.test import TestCase

# Create your tests here.

def get_square(n):
	if n>100:
		raise ValueError('This one is too much')
	return n**2

class TestMeBete(TestCase):
	def test_function(self):
		function_se_op = get_square(5)
		expected = 25
		self.assertEqual(function_se_op, expected)

	def test_raise_exceptionnn(self):
		with self.assertRaises(ValueError) as exception_context:
		    get_square(134)
		self.assertEqual(
		    str(exception_context.exception),
		    "This one is too much"
		)
