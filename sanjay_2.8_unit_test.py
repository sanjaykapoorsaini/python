import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        csv_path = "data_file.csv"
        f_obj = open(csv_path, "rb")
        self.reader = csv.DictReader(f_obj, delimiter=',')
        self.sample_data = {'COMPANY A':'1', 'COMPANY B':'2', 'COMPANY C':'3', 'COMPANY N':'50'}
    
    def testTypeDictionary(self):
        # test each row of the csv file is a Dictionary
        for row in self.reader: 
            self.assertTrue(type(row) is dict)   

    def test_maxValue(self):
        # make sure the output value should be highest
        higest_share_price = max(map(int, self.sample_data.values()))
        self.assertTrue(higest_share_price == 50) 
   
    def test_keyWithHighestValue(self):
        # test to get the key of the Dictionary which have highest value
        list = []
        higest_share_price = max(map(int, self.sample_data.values()))
        [list.append(key) for key in self.sample_data if int(self.sample_data[key]) == higest_share_price]
        self.assertTrue(list[0] == 'COMPANY N')        
    

if __name__ == '__main__':
    unittest.main()
