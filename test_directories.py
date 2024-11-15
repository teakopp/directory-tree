from directories import DirectoryManager
import unittest

class TestDirectories(unittest.TestCase):
	def setUp(self):
		self.dm = DirectoryManager()
	
	def test_create_directory(self):
		self.assertTrue(self.dm.create_directory("user"))
		self.assertTrue(self.dm.create_directory("user/howdy"))
		self.assertTrue(self.dm.create_directory("user/howdy/pardner"))
		self.assertFalse(self.dm.create_directory("user/hello/pardner"))

if __name__ == '__main__':
    unittest.main()