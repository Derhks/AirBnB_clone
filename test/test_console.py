#!/usr/bin/python3
"""Unittest Console Module"""

from console import HBNBCommand
import unittest
import pep8


class Test_Console(unittest.TestCase):

    def test_help_quit(self):
        """Test quit command"""
        msg = "Quit command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_pep8(self):
        """Test pep8"""
        pep8st = pep8.StyleGuide(quiet=True)
        res = pep8st.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
