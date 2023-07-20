import unittest
from email_validator import is_valid_email, is_valid_domain

class TestEmailValidator(unittest.TestCase):

    def test_valid_email(self):
        # Test valid email addresses
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user123@gmail.com"))
        self.assertTrue(is_valid_email("john_doe@hotmail.com"))

    def test_invalid_email(self):
        # Test invalid email addresses
        self.assertFalse(is_valid_email("invalid_email"))
        self.assertFalse(is_valid_email("missing_at.com"))
        self.assertFalse(is_valid_email("user123@missing_domain"))

    def test_valid_domain(self):
        # Test valid email domains
        self.assertTrue(is_valid_domain("test@example.com"))
        self.assertTrue(is_valid_domain("user123@gmail.com"))
        self.assertTrue(is_valid_domain("john_doe@hotmail.com"))

    def test_invalid_domain(self):
        # Test invalid email domains
        self.assertFalse(is_valid_domain("test@invalid_domain"))
        self.assertFalse(is_valid_domain("user123@non_existent_domain.com"))

if __name__ == "__main__":
    unittest.main()
