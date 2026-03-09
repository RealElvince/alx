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


# Inheritance
class Forest(Ecosystem):
    def __init__(self,name,description,biodiversity_index,carbon_sequestration_rate):
        super().__init__(name,description,biodiversity_index)
        self.tree_species = []
        self.carbon_sequestration_rate = carbon_sequestration_rate


    def add_tree_species(self,species):
        self.tree_species.append(species)

    def display_tree_species(self):
        print(f"The tree species in the forest are:{', '.join(self.tree_species)}")




forest = Forest("Tropical Forest", "Dense tropical forest with diverse wildlife", 0.75, 1000.0)

# Display forest details
print("Display forest details:")
forest.display_details()


# add tree species
forest.add_tree_species("Oak")
forest.add_tree_species("Mahogany")
forest.add_tree_species("Teak")

# Display trees species in the forest
print("\n Tree species in the forest:")
forest.display_tree_species()


# Polymorphism
class Wildlife():
    

    def habitat(self):
        pass


class Mammal(Wildlife):
    def habitat(self):
        return "Mammals live in a wide range of habitats including forests, deserts, oceans, and grasslands where they can find shelter, food, and suitable conditions for survival."

class Bird(Wildlife):
    def habitat(self):
      return "Birds: Birds live in habitats such as forests, wetlands, grasslands, and coastal areas where they can find food, water, and safe places to build nests."
    

mammal = Mammal()

bird = Bird()

# Mammal habitats
print("Mammals live in:")
print(mammal.habitat())

# Birds habitat
print("Birds live in: ")
print(bird.habitat())


# Absraction

from abc import ABC

class ConservationEfforts(ABC):
    def implement_effort(self):
        pass


class Reforestation(ConservationEfforts):
    def implement_effort(self):
        return "Reforestation implementation: Reforestation is implemented by planting trees in deforested areas, protecting young trees, and involving communities in forest restoration programs.."
    


class WildlifeConversation(ConservationEfforts):
    def implement_effort(self):
        return "Wildlife conservation implementation: Wildlife conservation is implemented by protecting habitats, enforcing laws against poaching, and creating protected areas such as national parks and reserves."
    


reforestation = Reforestation()

wildlifeconservation = WildlifeConversation()


# Reforestation implementation
print(reforestation.implement_effort())

# Wildlife conservation implementation
print(wildlifeconservation.implement_effort())

