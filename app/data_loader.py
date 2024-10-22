class Data:
    def __init__(self, path: str):
        self.path = path
        self.data = self.read_csv()
   
    def read_csv(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            final_data = [relationship.strip().split(" ") for relationship in file]
        return final_data
            
d1 = Data(r"C:\Studia\Zima2\DPP\Projekt\Data\facebook_combined.txt")
print(len(d1.data))