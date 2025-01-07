import unittest
from unittest.mock import mock_open, patch
from app.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    """
    Test suite for the DataLoader class.

    This class contains unit tests for the methods in the DataLoader class,
    including testing CSV loading, data transformation, and JSON conversion.
    """
    
    @patch("builtins.open", new_callable=mock_open, read_data="user friend\nuser1 friend1\nuser2 friend1") #mock dla funkcji open w DataLoader.load_csv
    def test_load_csv(self, mock_file):
        """
        Test the load_csv method of DataLoader.

        This test uses a mock for the `open` function to simulate reading a CSV file.
        It ensures that the `load_csv` method correctly parses the data into a list of dictionaries.

        Args:
            mock_file (unittest.mock.MagicMock): Mocked open function.

        Asserts:
            The output of `DataLoader.load_csv` matches the expected list of dictionaries.
        """
        loader = DataLoader("dummy_path.csv")
        data = loader.load_csv()
        expected_data = [{'user': 'user1', 'friend': 'friend1'}, {'user': 'user2', 'friend': 'friend1'}]
        self.assertEqual(data, expected_data) #result from mock == expected

    def test_transform_data(self):
        """
        Test the transform_data method of DataLoader.

        This test verifies that the `transform_data` method transforms input data into the expected
        node and edge format for further processing.

        Asserts:
            The output of `DataLoader.transform_data` matches the expected dictionary
            containing nodes and edges.
        """
        loader = DataLoader("dummy_path.csv")
        data = [{'user': 'user1', 'friend': 'friend1'}, {'user': 'user2', 'friend': 'friend1'}] 
        transformed_data = loader.transform_data(data)
        expected_data = {
        "nodes": [{"user": "user1"}, {"user": "user2"}],
        "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]
        }
        self.assertEqual(transformed_data, expected_data)

    def test_convert_to_json(self):
        """
       Test the convert_to_json method of DataLoader.

       This test verifies that the `convert_to_json` method correctly converts
       the data dictionary to a JSON string.

       Asserts:
           The output of `DataLoader.convert_to_json` matches the expected JSON string.
       """
        loader = DataLoader("dummy_path.csv")  
        data = {
            "nodes": [{"user": "user1"}, {"user": "user2"}],
            "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]
        } 
        
        json_data = loader.convert_to_json(data)
        
        expected_json = '{"nodes": [{"user": "user1"}, {"user": "user2"}], "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]}'

        self.assertEqual(json_data, expected_json)

if __name__ == '__main__':
    unittest.main()