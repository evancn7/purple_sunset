#!/usr/bin/env python3
from check_ppsn import *
import unittest


class TestPPSN(unittest.TestCase):
    def test_normal(self):
        testcase = '8348378Q'
        expected = '{} is valid'.format(testcase)
        self.assertEqual(check_ppsn(testcase), expected)

    def test_digits_too_many(self):
        testcase = '83483888Q'
        expected = '{} is not a valid PPSN'.format(testcase)
        self.assertEqual(check_ppsn(testcase), expected)

    def test_digits_too_few(self):
        testcase = '834838Q'
        expected = '{} is not a valid PPSN'.format(testcase)
        self.assertEqual(check_ppsn(testcase), expected)

    def test_letter_none(self):
        testcase = '834838'
        expected = '{} is not a valid PPSN'.format(testcase)
        self.assertEqual(check_ppsn(testcase), expected)

    def test_incorrect_checksum(self):
        testcase = '8348388A'
        expected = '{} is not a valid PPSN'.format(testcase)
        self.assertEqual(check_ppsn(testcase), expected)


unittest.main()
