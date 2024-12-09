from data_loader import DataLoader

file_path = "../data/facebook_combined.txt"

loader = DataLoader(file_path)

try:
    data = loader.load_csv()
    print("Data successfully loaded!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    raise

try:
    transformed_data = loader.transform_data(data)
    print("Data transformation completed successfully!")
except Exception as e:
    print(f"Error during data transformation: {e}")
    raise

try:
    json_data = loader.convert_to_json(transformed_data)
    print("Data successfully converted to JSON!")
except Exception as e:
    print(f"Error during JSON conversion: {e}")
    raise
