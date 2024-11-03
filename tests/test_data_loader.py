import unittest
from unittest.mock import mock_open, patch
from app.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="user friend\nuser1 friend1\nuser2 friend1") #mock dla funkcji open w DataLoader.load_csv
    def test_load_csv(self, mock_file):
        loader = DataLoader("dummy_path.csv")  #load_csv nie jest statyczne więc muszę stworzyć obiekt
        data = loader.load_csv()
        expected_data = [{'user': 'user1', 'friend': 'friend1'}, {'user': 'user2', 'friend': 'friend1'}]
        self.assertEqual(data, expected_data) #result z mocka == expected

    def test_transform_data(self): 
        loader = DataLoader("dummy_path.csv")#transform_data nie jest statyczne więc muszę stworzyć obiekt
        data = [{'user': 'user1', 'friend': 'friend1'}, {'user': 'user2', 'friend': 'friend1'}] #bez mocka, nie ma interackji z zewnętrznymi zależnośćiami API/plik itd
        transformed_data = loader.transform_data(data)
        expected_data = {
        "nodes": [{"user": "user1"}, {"user": "user2"}],
        "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]
        }
        self.assertEqual(transformed_data, expected_data)

    def test_convert_to_json(self): 
        loader = DataLoader("dummy_path.csv")  #convert_to_json nie jest statyczne więc muszę stworzyć obiekt
        data = {
            "nodes": [{"user": "user1"}, {"user": "user2"}],
            "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]
        } 
        
        json_data = loader.convert_to_json(data)  #funkcja
        
        #oczekiwany rezultat 
        expected_json = '{"nodes": [{"user": "user1"}, {"user": "user2"}], "edges": [{"user": "user1", "friend": "friend1"}, {"user": "user2", "friend": "friend1"}]}'

        self.assertEqual(json_data, expected_json) #test

if __name__ == '__main__':
    unittest.main()