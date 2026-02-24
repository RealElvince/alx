def analyse_carbon_impact(deforested_areas, planted_trees, carbon_emission_factor, carbon_offset_per_tree):
    """
    Calculate and categorise the overall carbon impact, considering deforestation, tree planting, and offset.

    Parameters:
    - deforested_areas (list): A list of deforested areas in hectares for each region.
    - planted_trees (list): A list of trees planted in each region.
    - carbon_emission_factor (float): Carbon emission factor in tons of CO2 per hectare.
    - carbon_offset_per_tree (float): Carbon offset per tree in tons of CO2.

    Returns:
    - str: 'Positive', 'Neutral', or 'Negative' based on the overall carbon impact.
    """
    total_carbon_emission = sum(area*carbon_emission_factor for area in deforested_areas)
    total_offset = sum(tree*carbon_offset_per_tree for tree in planted_trees)

    overal_impact = total_offset - total_carbon_emission

    if overal_impact > 0:
        return "Positive"
    elif overal_impact == 0:
        return "Neutral"
    else:
        return "Negative"
    
impact_result = analyse_carbon_impact([10, 15, 8, 12, 20],[100, 1000, 25, 35, 50],30,5)

print(impact_result)