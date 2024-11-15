from directories import DirectoryManager
import unittest

class TestDirectories(unittest.TestCase):
	def setUp(self):
		self.dm = DirectoryManager()
	
	def tearDown(self) -> None:
		return super().tearDown()
	
	def test_create_directory(self):
		self.dm = DirectoryManager()
		self.assertTrue(self.dm.create_directory("user"))
		self.assertTrue(self.dm.create_directory("user/howdy"))
		self.assertTrue(self.dm.create_directory("user/howdy/pardner"))
		self.assertFalse(self.dm.create_directory("user/hello/pardner"))

	def test_move_directory(self):
		self.dm = DirectoryManager()
		self.dm.create_directory("user")
		self.dm.create_directory("user/howdy")
		self.dm.create_directory("user/hello")
		self.dm.create_directory("user/hello/pardner")
		self.assertTrue(self.dm.move_directory("user/hello/pardner", "user/howdy"))
		self.assertFalse(self.dm.move_directory("user/hello/pardner", "user/howdy/partner"))
	
	def test_delete_directory(self):
		self.dm = DirectoryManager()
		self.dm.create_directory("user")
		self.dm.create_directory("user/howdy")
		self.dm.create_directory("user/hello")
		self.dm.create_directory("user/hello/pardner")
		self.assertTrue(self.dm.delete_directory("user/howdy"))
		self.assertFalse(self.dm.delete_directory("user/howdy"))

if __name__ == '__main__':
    unittest.main()