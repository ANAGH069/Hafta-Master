import pandas as pd
import openpyxl

gdp_df = pd.read_excel(
    "C:/Users/hp/Downloads/galytx assign.xlsx",
    sheet_name="GDP_WorldBank",
    header=4
)


gdp_df = gdp_df.drop(columns=["Indicator Name", "Indicator Code"])

#print(gdp_df.head())

pwb_df = pd.read_excel(
    "C:/Users/hp/Downloads/galytx assign.xlsx",
    sheet_name="Population_WorldBank",
    header=4
)

pwb_df = pwb_df.drop(columns=["Indicator Name", "Indicator Code"])

#print(pwb_df.head())

import pandas as pd


gdp_long = gdp_df.melt(
    id_vars=["Country Code", "Country Name"],  # columns to keep as is
    var_name="Year",                          # new column for the year
    value_name="GDP"                          # new column for GDP values
)


gdp_long["Year"] = gdp_long["Year"].astype(int)

print(gdp_long.columns)

#print(pwb_df.columns)


pwb_long = pwb_df.melt(
    id_vars=["Country Code", "Country Name"],  # columns to keep as is
    var_name="Year",                          # new column for the year
    value_name="POPULATION"                          # new column for GDP values
)


pwb_long["Year"] = pwb_long["Year"].astype(int)

print(pwb_long.columns)

pwb_long.to_excel("C:/Users/hp/Downloads/assignment.xlsx", sheet_name="Population_WorldBank", index=False)
gdp_long.to_excel("C:/Users/hp/Downloads/assignment.xlsx", sheet_name="GDP", index=False)
import pandas as pd


merged_df = pd.merge(
    gdp_long,
    pwb_long,
    on=["Country Code", "Country Name", "Year"],
    how="inner"
)


merged_df["GDP per Capita"] = merged_df["GDP"] / merged_df["POPULATION"]


merged_df = merged_df[merged_df["Year"] >= (merged_df["Year"].max() - 19)]

merged_df = merged_df.sort_values(by=["Country Name", "Year"], ascending=[True, True])



merged_df.to_excel("C:/Users/hp/Downloads/assignment.xlsx", sheet_name="GDP_Per_Capita", index=False)

print(merged_df.head())

import matplotlib.pyplot as plt



countries = ["China", "Germany", "India", "United States"]


latest_year = merged_df["Year"].max()


start_year = latest_year - 19


trend_data = merged_df[
    (merged_df["Country Name"].isin(countries)) &
    (merged_df["Year"] >= start_year)
]


plt.figure(figsize=(12, 6))
for country in countries:
    country_data = trend_data[trend_data["Country Name"] == country]
    plt.plot(country_data["Year"], country_data["GDP per Capita"], marker='o', label=country)

plt.xlabel("Year")
plt.ylabel("GDP per Capita")
plt.title(f"GDP per Capita Trend (Last 20 Years) - {', '.join(countries)}")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
