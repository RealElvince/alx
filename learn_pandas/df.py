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