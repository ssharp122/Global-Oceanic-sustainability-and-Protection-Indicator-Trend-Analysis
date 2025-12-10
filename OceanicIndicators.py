import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("OceanData.csv")


# Standardize column names


df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# Identify year columns dynamically


year_cols = [col for col in df.columns if col.isdigit()]


# Convert to numeric (remove potential commas or NaNs)


for col in year_cols:

    df[col] = pd.to_numeric(df[col], errors="coerce")


# Check missing


df.isna().sum()


# Dataset Shape and Metadata


df.shape

df.head()

df.info()

df.describe()


# Check for missing data patterns


df[year_cols].isna().mean().sort_values()


# Top / Bottom in terms of sustainability and protection


top = df.sort_values("2024", ascending=False).head(10)

bottom = df.sort_values("2024", ascending=True).head(10)


# Year-over-year change 


df["change_20_24"] = df["2024"] - df["2020"]


#Global Trend Over time


global_avg = df[year_cols].mean()

plt.figure(figsize=(8,5))

plt.plot(global_avg.index, global_avg.values, marker='o')

plt.title("Global Indicator Average (2020–2024)")

plt.xlabel("Year")

plt.ylabel("Average Score")

plt.grid(True)

plt.show()


#Top 10 Countries 


plt.figure(figsize=(10,6))

plt.barh(top["ref_area_label"], top["2024"], color="skyblue")

plt.title("Top 10 Countries in 2024")

plt.xlabel("Score")

plt.gca().invert_yaxis()

plt.show()


# Year over year change distribution


plt.figure(figsize=(8,5))

plt.hist(df["change_20_24"], bins=20)

plt.title("Distribution of 2020–2024 Score Changes")

plt.xlabel("Score Change")

plt.ylabel("Frequency")

plt.grid(True)

plt.show()


# Heat Map of yearly values


import seaborn as sns


plt.figure(figsize=(12,6))

sns.heatmap(df[year_cols].corr(), annot=True, cmap="Blues")

plt.title("Correlation Between Yearly Scores")

plt.show()


