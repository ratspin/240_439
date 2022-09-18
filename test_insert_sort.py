
import unittest
def insertion_sort(d):
    data = d.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

class Sort_Test(unittest.TestCase):
    def test_float(self):
        data = [-1.23, 0.0000, 567, 46.12354, ]
        expected_output = [-1.23, 0.0000, 46.12354, 567]
        sort_list = insertion_sort(data)
        self.assertEqual(sort_list, expected_output,f'Should be {expected_output}')

    def test_Positive_Negative(self):
        data = [0,1,2,3,-1,-2,-3]
        expected_output = [-3,-2,-1,0,1,2,3]
        result = insertion_sort(data)
        self.assertEqual(result,expected_output)
    
    def test_give_1001_is_True(self):
        data = [-1000,1000,500,-500]
        expected_output = [-1000,-500,500,1000]
        result = insertion_sort(data)
        self.assertEqual(result,expected_output)