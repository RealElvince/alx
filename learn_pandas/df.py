import pandas as pd
import numpy as np

df = {
    "Crop":['Wheat', 'Corn', 'Rice', 'Soybean'],
    "Year_per_Acre":[3, 4.5, 5, 2.8],
    "Country":['USA', 'China', 'India', 'Brazil']

}

crop_df = pd.DataFrame(data=df)
print(crop_df)

print(crop_df.iloc[1:3])


tree_array = np.array([[30, 25], [60, 30], [25, 20]])

columns = ["Max_Height_m","Growth_Rate_cm_per_year"]

index = ["Maple", "Pine","Birch"]


tree_df = pd.DataFrame(data=tree_array,columns=columns,index=index)

print(tree_df)