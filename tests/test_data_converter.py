import unittest
from data_converter import read_data

class TestDataConverter(unittest.TestCase):
    
    def test_read_data_empty_file(self):
        data_frame = read_data('data/empty_file.csv', 'csv')
        self.assertTrue(data_frame.empty)

    def test_read_data_single_row_csv(self):
        data_frame = read_data('data/single_row.csv', 'csv')
        self.assertTrue(data_frame.empty)
        
    def test_read_data_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError) as context:
            read_data('data/non_existent_file.csv', 'csv')
        self.assertIn("Input file not found: data/non_existent_file.csv", str(context.exception))

    def test_read_data_invalid_format(self):
        with self.assertRaises(ValueError) as context:
            read_data('data/input.csv', 'invalid_format')
        self.assertIn("Unsupported input format: invalid_format", str(context.exception))

    def test_read_data_valid_csv(self):
        data_frame = read_data('data/input.csv', 'csv')
        self.assertIsNotNone(data_frame)
        # Add more assertions if needed

    def test_read_data_valid_json(self):
        data_frame = read_data('data/input.json', 'json')
        self.assertIsNotNone(data_frame)
        # Add more assertions if needed

    def test_read_data_valid_xml(self):
        data_frame = read_data('data/input.xml', 'xml')
        self.assertIsNotNone(data_frame)
        # Add more assertions if needed

    def test_write_data_csv(self):
        # Add your write_data tests here
        pass

    def test_write_data_json(self):
        # Add your write_data tests here
        pass

    def test_write_data_xml(self):
        # Add your write_data tests here
        pass

if __name__ == '__main__':
    unittest.main()
