from data_loader import DataLoader

loader = DataLoader(r"C:\Studia\Zima2\DPP\Projekt\Data\facebook_combined.txt")
data = loader.load_csv()
transformed_data = loader.transform_data(data)
json_data = loader.convert_to_json(transformed_data)
