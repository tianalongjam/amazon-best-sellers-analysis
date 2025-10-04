#import statements
import pandas as pd

#loading the data
df = pd.read_csv("bestsellers.csv")

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#changing the "Price" column to float
df["Price"] = df["Price"].astype(float)

#Question 1: Which author appears most frequently among Amazon’s Top 50 Bestsellers (2009–2019)?

author_counts = df["Author"].value_counts()
# print(author_counts)

# print(type(author_counts))

most_author_counts = author_counts.max()
print(author_counts.nlargest(1).iloc[0])


# print(author_counts.nlargest(1))



