import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Doe", "John", "Computer Science", 3.5)

    def tearDown(self):
        del self.student
    
    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.major, "Computer Science")
    
    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.major, "Computer Science")
        self.assertEqual(self.student.gpa, 3.5)

    def test_student_str(self):
        expected_str = "Doe, John has major Computer Science with gpa: 3.5"
        self.assertEqual(str(self.student), expected_str)
    
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            Student("123", "John", "Computer Science", 3.5)
    
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            Student("Doe", "456", "Computer Science", 3.5)
    
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            Student("Doe", "John", "789", 3.5)
        
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            Student("Doe", "John", "Computer Science", "Four")
    
def main():
    unittest.main()

if __name__ == "__main__":
    main()
