from unittest import TestCase
import dataGen


class TestDataGen(TestCase):

    def test_charGen(self):
        expected_result = 10
        result = len(dataGen.char_gen(10))
        self.assertEqual(result, expected_result)
    
    def test_charGen_whenLengthIsZero(self):
        expected_result = 0
        result = len(dataGen.char_gen(0))
        self.assertEqual(result, expected_result)

    def test_query_generator(self):
        data = [[123, '1927-03-19 11:43:53', 'char']]
        expected_result = '(123, \'1927-03-19 11:43:53\', \'char\');'
        result = dataGen.query_generator(data)
        self.assertEqual(expected_result, result)
