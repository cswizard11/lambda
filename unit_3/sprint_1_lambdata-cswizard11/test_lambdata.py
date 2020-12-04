import lambdata
import unittest


class LambdataTest(unittest.TestCase):
    '''test the BetterDataFrame class from Lambdata'''

    def setUp(self):
        '''make the data frame to use for testing'''
        self.test_df = lambdata.BetterDataFrame({'a' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]})

    def test_null_count(self):
        '''test that null_count returns the correct number of null values'''
        self.assertEqual(self.test_df.null_count(), 0)

    def test_train_test_split(self):
        '''test that the train_test_split returns lists of the correct length'''
        self.assertEqual(len(self.test_df.train_test_split(0.8)[0]), 8)
        self.assertEqual(len(self.test_df.train_test_split(0.8)[1]), 2)

if __name__ == '__main__':
    unittest.main()
