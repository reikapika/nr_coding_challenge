#!/usr/bin/env python3 

import unittest
from get_three_word_sequences import get_three_word_sequences, main, validate_params

class TestGetThreeWordSequences(unittest.TestCase):
    def test_validate_params_with_empty_parameter(self):
        input_val = ['']
        expected = {'':1}
        self.assertEqual(validate_params(input_val), expected)

    def test_get_three_word_sequences_with_empty_string(self):
        input_val = ''
        expected = []
        self.assertEqual(get_three_word_sequences(input_val), expected)

    def test_main_with_none_arguements(self):
        input_val = None
        self.assertRaises(SystemExit)




unittest.main()