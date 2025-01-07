# Data

The project uses the `facebook_combined.txt` dataset, which contains connections between friends.

## Structure of facebook_combined.txt

The dataset contains space-separated pairs of user IDs, where each line represents a connection between two users in the social network. The format is as follows:

0 1
0 2
0 3
0 4
...

Each line indicates that there is a bidirectional friendship between two users. For example:

0 1 means that User 0 is friends with User 1.

0 2 means that User 0 is friends with User 2.


## How the Dataset is Processed

The dataset is processed by the DataLoader module, which:

Reads the dataset file and loads the connections into memory.

Transforms the raw data into a structured format consisting of nodes and edges.

Builds a graph representation using the NetworkX library.

The transformed data includes:

Nodes: A list of unique users in the network.

Edges: A list of connections between users.

## Usage in the Project

The dataset is used in various parts of the project, including:

Finding the shortest path between two users using the shortest_path module.

Displaying a user's friends and visualizing their social connections using the show_friends module.

Calculating the reach of a social media post using the maximize_reach module.



## Dataset Size and Complexity

Number of Users (Nodes): 4,039

Number of Connections (Edges): 88,234

The dataset is relatively small but complex enough to demonstrate various graph algorithms and visualization techniques.

## Loading the Dataset

The dataset is loaded automatically by the main application using the `DataLoader` class:

```py
from app.data_loader import DataLoader

loader = DataLoader("data/facebook_combined.txt")
data = loader.load_csv()

transformed_data = loader.transform_data(data)

print(transformed_data)
```