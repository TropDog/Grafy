import json
import csv

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=' ')
            return [row for row in reader]
    
    def convert_to_json(self, data):
        return json.dumps(data)
    
    def transform_data(self, data):
        nodes = []
        edges = []

        #unikalne wystapienia (edges)
        unique_users = set()
        for entry in data:
            unique_users.add(entry["user"])
            edges.append({"user": entry["user"], "friend": entry["friend"]})

        #unikalne wystapienia (nodes)
        for user in unique_users:
            nodes.append({"user": user})

        return {
            "nodes": nodes,
            "edges": edges
        }