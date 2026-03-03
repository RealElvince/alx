class Ecosystem:
    def __init__(self,name,description,biodiversity_index):
        self.name = name
        self.description = description
        self.biodiversity_index = biodiversity_index


    def display_details(self):
        print(f"Ecosystem name: {self.name}")
        print(f"Ecosystem description:{self.description}")
        print(f"Ecosystem biodiversity index:{self.biodiversity_index}")


    def update_ecosystem(self,new_description):
        self.description = new_description


ecosystem = Ecosystem("Rainforest","A rainforestis a dense forest that receives heavy rainfall throughout the year and supports a wide variety of plants and animals.",0.80)

ecosystem.display_details()
ecosystem.update_ecosystem("A rainforest is a lush, tropical forest with high humidity and rich biodiversity, where tall trees form multiple layers of canopy.")

print("\n Updated ecosystem description:")
ecosystem.display_details()