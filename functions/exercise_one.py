deforested_land = [10,15,8,12,20]

carbon_emission_factor = 40

total_deforested_land = sum(deforested_land)

total_carbon_emission = total_deforested_land*carbon_emission_factor
print(total_deforested_land)
print(total_carbon_emission)


# Exercise 2

def acres_to_hectares(acres):
    """
    conversion: acres to hectares
    paramters : acres 

    constant : 0.404686
    return acres * constant
    
    
    """
    conversion_rate = 0.404686
    hectares = acres*conversion_rate

    return hectares

acres_to_hectares(50)


# Exercise 3

average_deforested_land = sum(deforested_land)/len(deforested_land)
print(average_deforested_land)



