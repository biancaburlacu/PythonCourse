import unittest
import pytest
from password_checker import (has_special_char, has_numbers, has_length, is_password_valid)


class PasswordCheckerTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_has_special_char_true(self):
        texts = ["a*", "abc^&% 9bac#$", "5361&^$%", "!@#$^&*"]
        for text in texts:
            self.assertEqual(True, has_special_char(text))

    @pytest.mark.task(taskno=2)
    def test_has_special_char_false(self):
        texts = ["a", "abc 9bac", "5361", " ", ""]
        for text in texts:
            self.assertEqual(False, has_special_char(text))

    @pytest.mark.task(taskno=3)
    def test_has_numbers_true(self):
        texts = ["a*123", "abc^&% 9bac#$", "5361&^$%", "1"]
        for text in texts:
            self.assertEqual(True, has_numbers(text))

    @pytest.mark.task(taskno=4)
    def test_has_numbers_false(self):
        texts = ["a*", "abc^&% bac#$", "", " "]
        for text in texts:
            self.assertEqual(False, has_numbers(text))

    @pytest.mark.task(taskno=5)
    def test_has_length_true(self):
        texts = ["1627488", "abc^&% bac#$", "abcderfghti", " hgasjakj6189809"]
        for text in texts:
            self.assertEqual(True, has_length(text))

    @pytest.mark.task(taskno=6)
    def test_has_length_false(self):
        texts = ["1628", "abc &%", "", " "]
        for text in texts:
            self.assertEqual(False, has_length(text))

    @pytest.mark.task(taskno=7)
    def test_is_password_valid_true(self):
        texts = ["1627488abc*", "abc^&% b1ac#$", "abc$#*8ti", " hgasjakj618*$09"]
        for text in texts:
            self.assertEqual(True, is_password_valid(text))

    @pytest.mark.task(taskno=8)
    def test_is_password_valid_false(self):
        texts = ["1628", "ab &%", "", " "]
        for text in texts:
            self.assertEqual(False, is_password_valid(text))

