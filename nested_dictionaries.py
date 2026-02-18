fynbo_families = {
    'Erica':{'Cape Floristic Region':670,'Worldwide':4500},
    'Protea':{'Cape Floristic Region':330,'Worldwide':1350},
    'Citrus':{'Cape Floristic Region':273,'Worldwide':1650},
     'Phylica':{'Cape Floristic Region':173,'Worldwide':900}
   
}

print(type(fynbo_families))

print(type(fynbo_families['Erica']))

# number of species from Cape Floristic Region in Protea

species_in_protea = fynbo_families['Protea']['Cape Floristic Region']

print("The number of species from Cape Floristic Region in Protea is {} species.".format(species_in_protea))


# protea species 
protea_species = fynbo_families['Protea']

print(protea_species)

# extract keys from a dictionary using keys() return key object

key_list = list(protea_species.keys())
print(key_list)

# extract values from a dictionary using values()

value_list = list(protea_species.values())
print(value_list)

# We can also extract the combined key-value pairs in tuples by using the items() method.

item_list = list(protea_species.items())
print(item_list)