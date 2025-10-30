# Alcohol and Tobacco Consumption Analysis
### Sabancı University 2025-26 Fall Term DSA 210 Term Project
---

## Motivation
Alcohol and tobacco consumption is a prevalent issue in various countries throughout the world. This project aims to analyze and understand the socioeconomic factors such as GDP, education level and population statistics contributing to the usage of these substances and whether the government’s efforts to control them are effective. By comparing different countries’ features, the analysis will hopefully help us understand how we can reduce these substances consumption rates.

The project will thus focus on these questions:
1. **How do socioeconomic factors correlate with the usage of alcohol and tobacco?**
2.	**Does government control help reduce these substance’s consumption in a meaningful way?**
3.	**Can we predict the consumption rate of these substances and find factors that reduce them?**


## Data Sources
1. [Global Country Information Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023)

* Dataset to get the socioeconomic factors of each country.
* **Features Used:**
    * Country: Name of the country.
    * Density (P/Km2): Population density measured in persons per square kilometer.
    * Birth Rate: Number of births per 1,000 population per year.
    * CPI: Consumer Price Index, a measure of inflation and purchasing power.
    * CPI Change (%): Percentage change in the Consumer Price Index compared to the previous year.
    * GDP: Gross Domestic Product, the total value of goods and services produced in the country.
    * Gross Primary Education Enrollment (%): Gross enrollment ratio for primary education.
    * Gross Tertiary Education Enrollment (%): Gross enrollment ratio for tertiary education.
    * Life Expectancy: Average number of years a newborn is expected to live.
    * Total Tax Rate: Overall tax burden as a percentage of commercial profits.
    * Unemployment Rate: Percentage of the labor force that is unemployed.
    * Urban Population: Percentage of the population living in urban areas.
    
2. [Tobacco: current tobacco use, tobacco smoking and cigarette smoking, age-standardized](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/gho-tobacco-control-monitor-current-tobaccouse-tobaccosmoking-cigarrettesmoking-agestd-tobagestdcurr)

* Dataset to get the tobacco usage of each country.
* **Features Used:**
    * Country: Name of the country.
    * Estimate of current tobacco use prevalence (%) (age-standardized rate): Estimated usage rate of tobacco.

3. [Alcohol, total per capita (15+) consumption (in litres of pure alcohol) (SDG Indicator 3.5.2)](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/total-(recorded-unrecorded)-alcohol-per-capita-(15-)-consumption)

* Dataset to get the alcohol usage of each country.
* **Features Used:**
    * Country: Name of the country.
    * Alcohol, total per capita (15+) consumption (in litres of pure alcohol) (SDG Indicator 3.5.2), three-year average: Average consumption of alcohol per capita.

4. [Alcohol policy: adopted written national policy on alcohol](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/adopted-written-national-policy-on-alcohol)

* Dataset to get the alcohol policies of each country.
* **Features Used:**
    * Country: Name of the country.
    * Adopted written national policy on alcohol: Does the country have a written policy to control alcohol usage.

5. [Tobacco control: Monitor: national tobacco control programmes](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/gho-tobacco-control-monitor-national-tobacco-control-programmes)

* Dataset to get the tobacco policies of each country.
* **Features Used:**
    * Country: Name of the country.
    * Government objectives on tobacco control exist: Does the government try to control the tobacco usage.

## Data Collection
Plans on how to collect the data.
1. **Global Country Information Dataset 2023**
* Downloaded the dataset through Kaggle.
* Filtered the features to retain `Country`, `Density (P/Km2)`, `Birth Rate`, `CPI`, `CPI Change (%)`, `GDP Gross Primary Education Enrollment (%)`, `Gross Tertiary Education Enrollment (%)`, `Life Expectancy`, `Total Tax Rate`, `Unemployment Rate`, `Urban Population`.
    
2. **Tobacco: current tobacco use, tobacco smoking and cigarette smoking, age-standardized**
* Filtered the dataset rows to the year 2022 and the features to `Country (Renamed from Location)`, `Estimate of current tobacco use prevalence (%) (age-standardized rate)`.
* Downloaded the dataset through the WHO website.

3. **Alcohol, total per capita (15+) consumption (in litres of pure alcohol) (SDG Indicator 3.5.2)**
* Filtered the dataset rows to the year 2022 and the features to `Country (Renamed from Location)`, `Alcohol, total per capita (15+) consumption (in litres of pure alcohol) (SDG Indicator 3.5.2), three-year average`.
* Downloaded the dataset through the WHO website.

4. **Alcohol policy: adopted written national policy on alcohol**
* Filtered the dataset rows to the latest year and the features to `Country (Renamed from Location)`, `Adopted written national policy on alcohol`.
* Downloaded the dataset through the WHO website.

5. **Tobacco control: Monitor: national tobacco control programmes**
* Filtered the dataset rows to the latest year and the features to `Country (Renamed from Location)`, `Government objectives on tobacco control exist`.
* Downloaded the dataset through the WHO website.
