"""
Module for loading and transforming social network data.

This module provides a `DataLoader` class with the following functionalities:
1. Load data from a file containing user connections.
2. Convert data to JSON format.
3. Transform data into nodes and edges for use in graph algorithms.
"""

import json
import csv

class DataLoader:
    """
    A class to load and process social network data from a file.

    Attributes:
        file_path (str): Path to the file containing the data.
    """

    def __init__(self, file_path):
        """
        Initializes the DataLoader with the file path.

        :param file_path: Path to the file containing the social network data.
        """
        self.file_path = file_path

    def load_csv(self):
        """
        Loads data from a CSV file where each row represents a connection between two users.

        :return: List of dictionaries with keys "user" and "friend".
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=' ')
            return [{"user": row[0], "friend": row[1]} for row in reader]

    def convert_to_json(self, data):
        """
        Converts a list of dictionaries into a JSON string.

        :param data: List of dictionaries containing the data to convert.
        :return: JSON string representing the data.
        """
        return json.dumps(data)

    def transform_data(self, data):
        """
        Transforms raw data into nodes and edges suitable for graph processing.

        :param data: List of dictionaries with keys "user" and "friend".
        :return: Dictionary with two keys:
                 - "nodes": List of unique users.
                 - "edges": List of connections as dictionaries with keys "user" and "friend".
        """
        nodes = []
        edges = []

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
