import unittest
import re

class TestRegex(unittest.TestCase):
    def test_name_regex(self):
        name_regex = r'[A-Za-z]+\s[A-Za-z]+'
        self.assertTrue(re.match(name_regex, "John Doe"))
        self.assertTrue(re.match(name_regex, "Jane Smith"))
        self.assertFalse(re.match(name_regex, "12345"))  
        
    def test_phone_regex(self):
        phone_regex = r'\d{3}-\d{3}-\d{4}'
        self.assertTrue(re.match(phone_regex, "555-555-5555"))
        self.assertFalse(re.match(phone_regex, "123-45-6789"))
        
    def test_identification_regex(self):
        identification_regex = r'[A-Z0-9]{8}'
        self.assertTrue(re.match(identification_regex, "ABC12345"))
        self.assertFalse(re.match(identification_regex, "abcdefg"))
        
if __name__ == '__main__':
    unittest.main()