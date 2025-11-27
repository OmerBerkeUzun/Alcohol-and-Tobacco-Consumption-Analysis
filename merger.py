import pandas as pd

#Import and filter features of world_data_2023.csv
world_data = pd.read_csv("./Raw Data/world_data_2023.csv")
world_data = world_data.drop(columns=["Abbreviation","Agricultural Land( %)","Land Area(Km2)","Armed Forces size", "Calling Code", "Capital/Major City", "Co2-Emissions", "Currency-Code", "Fertility Rate", "Forested Area (%)", "Gasoline Price", "Infant mortality", "Largest city", "Maternal mortality ratio", "Minimum wage", "Official language", "Out of pocket health expenditure", "Physicians per thousand", "Population", "Population: Labor force participation (%)", "Tax revenue (%)", "Latitude", "Longitude"])

#Import and filter features of alcohol_use_data.csv
alcohol_use_data = pd.read_csv("./Raw Data/alcohol_use_data.csv")
alcohol_use_data = alcohol_use_data[["Location","Value"]]
alcohol_use_data = alcohol_use_data.rename(columns={"Location": "Country", "Value": "Alcohol Total Per Capita Consumption"})

#Import and filter features of tobacco_use_data.csv
tobacco_use_data = pd.read_csv("./Raw Data/tobacco_use_data.csv")
tobacco_use_data = tobacco_use_data[tobacco_use_data["Dim1ValueCode"] == "SEX_BTSX"]
tobacco_use_data = tobacco_use_data[["Location","Value"]]
tobacco_use_data = tobacco_use_data.rename(columns={"Location": "Country", "Value": "Tobacco Use Estimate"})
tobacco_use_data = tobacco_use_data.reset_index(drop=True)

#Import and filter features of tobacco_regulation_data.csv
tobacco_reg_data = pd.read_csv("./Raw Data/tobacco_regulation_data.csv")
tobacco_reg_data = tobacco_reg_data[["Location","Value"]]
tobacco_reg_data = tobacco_reg_data.rename(columns={"Location": "Country", "Value": "Tobacco Regulation"})

#Import and filter features of alcohol_regulation_data.csv
alcohol_reg_data = pd.read_csv("./Raw Data/alcohol_regulation_data.csv")
alcohol_reg_data = alcohol_reg_data[["Location","Value"]]
alcohol_reg_data = alcohol_reg_data.rename(columns={"Location": "Country", "Value": "Alcohol Regulation"})

#Merge the data frames on to a single data frame with inner join
merged_df =(world_data
            .merge(alcohol_use_data, on="Country", how="inner")
            .merge(tobacco_use_data, on="Country", how="inner")
            .merge(tobacco_reg_data, on="Country", how="inner")
            .merge(alcohol_reg_data, on="Country", how="inner")
)

#Clean merged data of null and unwanted values
merged_df = merged_df.dropna()
merged_df = merged_df[merged_df["Alcohol Regulation"] != "No data"]
merged_df["Alcohol Regulation"] = merged_df["Alcohol Regulation"].replace("Subnational", "Yes")
merged_df["Alcohol Regulation"] = merged_df["Alcohol Regulation"].replace("Total ban", "Yes")

merged_df.to_csv("./Processed Data/merged_data.csv", index=False)