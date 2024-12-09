import json
import csv


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        # Wczytaj dane bez nagłówków
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            return [{"user": row[0], "friend": row[1]} for row in reader]

    def convert_to_json(self, data):
        return json.dumps(data)

    def transform_data(self, data):
        nodes = []
        edges = []

        # Unikalne węzły i krawędzie
        unique_users = set()
        for entry in data:
            unique_users.add(entry["user"])
            unique_users.add(entry["friend"])
            edges.append({"user": entry["user"], "friend": entry["friend"]})

        for user in unique_users:
            nodes.append({"user": user})

        return {
            "nodes": nodes,
            "edges": edges
        }
