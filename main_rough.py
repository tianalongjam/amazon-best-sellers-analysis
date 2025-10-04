##import statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##loading the data 
df = pd.read_csv("bestsellers.csv")
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#changing the "Price" column to float
df["Price"] = df["Price"].astype(float)


#Question 1: Which author appears most frequently among Amazon’s Top 50 Bestsellers (2009–2019)?

author_counts = df["Author"].value_counts()
highest_author_counts = author_counts.nlargest(1).index

ans1 = highest_author_counts[0]
# print(ans1)

#Question 2: What is the average price of Fiction vs. Non Fiction bestsellers?

ans2 = df.groupby("Genre")["Price"].mean()
# print(ans2)

#Question 3: Which single book received the highest number of user reviews in the dataset?

books_rev = df.groupby("Title")["Reviews"].sum()
ans3 = books_rev.nlargest(1).index[0]
# print(ans3)

#Question 4: How many unique authors had bestsellers that appeared in multiple years?

authors_year_counts = df.groupby("Author")["Publication Year"].nunique()
filtered_authors = authors_year_counts[authors_year_counts>1]
ans4 = filtered_authors.shape[0]
# print(type(filtered_authors))
# print(filtered_authors.sum(axis=0))

#Question 5: What is the trend in average user ratings of bestsellers across the years 2009-2019?

ans5 = df.groupby("Publication Year")["Rating"].mean().round(3)

# print(ans5)

#Question 6: Which year has the highest average number of reviews per bestseller?

avg_revs = df.groupby("Publication Year")["Reviews"].mean().round(1)

ans_year = avg_revs.idxmax()
ans_avg_revs = avg_revs.max()

# print(ans_year, ans_avg_revs)

#Question 7: Is there a correlation between a book's price and the number of reviews it recieved?

price_revs_corr = df[["Price", "Reviews"]].corr()

ans7 = price_revs_corr.loc["Price", "Reviews"]

#Question 8: Which top 5 books appeared in the Amazon Bestseller list across the most years?

ans8 = df.groupby("Title")["Publication Year"].nunique().sort_values(ascending=False).head()

#Question 9: For each year, which author had the most books in the Top 50 Bestsellers?

counts_year_author = df.groupby(["Publication Year","Author"]).size().reset_index(name="Count")

ans9 = (
    counts_year_author
    .sort_values(["Publication Year","Count","Author"], ascending=[True, False, True])
    .groupby("Publication Year")
    .head(1)
    .reset_index(drop=True)
)

# print(ans9)

#Question 10: How does the price variability (variance) compare between Fiction and Non Fiction bestsellers?

var_genre = df.groupby("Genre")["Price"].var()
std_genre = df.groupby("Genre")["Price"].std()

ans10 = pd.concat([var_genre.rename("Variance"),
                   std_genre.rename("Std")], axis=1)

# print(ans10)

#Question 11: What percentage of bestsellers with a user rating ≥ 4.8 belong to Non Fiction?

matched_rating = df[df["Rating"] >= 4.8]
ans11 = (matched_rating["Genre"].eq("Non Fiction").mean() * 100) if len(matched_rating) else np.nan
# print(f"Q11) % of rating ≥ 4.8 that are Non Fiction: {pct_nonfiction_high:.1f}%")
# print(ans11)

#Question 12: Among authors with at least 3 bestselling books, which author has the highest average rating?

abc = df["Author"].value_counts()
author_list = abc[abc>=3].index
ans12 = (
    df[df["Author"].isin(author_list)]
    .groupby("Author")["Rating"].mean()
    .sort_values(ascending=False)
    .head(1)
)

# print(filtered_df)

#Question 13: Which year had the lowest median price for bestselling books, and what was that price?

pewpew = df.groupby("Publication Year")["Price"].median()

pewpew = (
    df.groupby("Publication Year")["Price"].median()
    .sort_values()
    .head(1)
)

# Question 14: How many bestsellers priced above $20 still managed to achieve a rating ≥ 4.7?

meow = (
    df[
        (df["Price"]>20) &
        (df["Rating"]>=4.7)
    ]
).shape[0]

# print(meow)

#Question 15: Does the dataset suggest a relationship between the number of reviews and user ratings (e.g., do heavily reviewed books tend to have higher ratings)?

corr_reviews_rating = df[["Reviews","Rating"]].corr().loc["Reviews","Rating"]
# print(f"Q15) Pearson correlation (Reviews vs Rating): {corr_reviews_rating:.4f}")
# print()

# print(corr_reviews_rating)

#Question 16: Using a pivot table, how did the distribution of Fiction vs. Non Fiction bestsellers change from 2009 to 2019?

df["Genre"] = df["Genre"].str.strip()

# Pivot table: count of Fiction vs Non Fiction by year
pivot_counts = pd.pivot_table(
    df, 
    index="Publication Year", 
    columns="Genre", 
    values="Title", 
    aggfunc="count", 
    fill_value=0
)

# Optional: ensure column order is consistent
if {"Fiction", "Non Fiction"}.issubset(pivot_counts.columns):
    pivot_counts = pivot_counts[["Fiction", "Non Fiction"]]

# Plot stacked bar chart
# pivot_counts.plot(
#     kind="bar",
#     stacked=False,
#     figsize=(10, 6),
#     color = ["skyblue", "pink"]
# )

# plt.title("Distribution of Fiction vs Non Fiction Bestsellers (2009–2019)", fontsize=14)
# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Count of Bestsellers", fontsize=12)
# plt.legend(title="Genre")
# plt.tight_layout()
# plt.show()

#Question 17: Which author had the most consistent user ratings (lowest standard deviation across all their bestsellers)?

rating_std_by_author = df.groupby("Author")["Rating"].agg(["std","count"])
rating_std_by_author = rating_std_by_author[rating_std_by_author["count"] >= 2].copy()
rating_std_by_author["std"] = rating_std_by_author["std"].fillna(0).round(4)
q17 = rating_std_by_author.sort_values(["std","Author"]).head(1)
print("Q17) Most consistent author ratings (≥2 books):")
print(q17.rename(columns={"std":"Rating STD","count":"Count"}).to_string())
print()

#Question 18: If you group bestsellers into price quartiles, how do their average number of reviews differ across quartiles?

df["Price Quartile"] = pd.qcut(df["Price"], 4, duplicates="drop")

avg_reviews_by_quartile = df.groupby("Price Quartile")["Reviews"].mean().round(1)
print("Q18) Avg reviews by price quartile:")
print(avg_reviews_by_quartile.to_string())
print()

# 19) For books in multiple years: rating trend (improve/decline/stable) via slope
# multi_year_books = df.groupby("Name").filter(lambda g: g["Year"].nunique() > 1)

# def slope_per_book(g):
#     tmp = g[["Year","User Rating"]].dropna().drop_duplicates().sort_values("Year")
#     if tmp["Year"].nunique() < 2:
#         return np.nan
#     x = tmp["Year"].values
#     y = tmp["User Rating"].values
#     return np.polyfit(x, y, 1)[0]  # slope

# slopes = (
#     multi_year_books.groupby("Name")
#     .apply(slope_per_book)
#     .dropna()
#     .rename("slope_per_year")
# )

# improving = (slopes > 0).sum()
# declining = (slopes < 0).sum()
# stable = (slopes.abs() < 1e-6).sum()
# avg_slope = slopes.mean() if not slopes.empty else np.nan
# print(f"Q19) Multi-year rating trend — improving={int(improving)}, declining={int(declining)}, stable={int(stable)}, average slope per year={avg_slope:.6f}")
# print()

# # 20) Year-wise leaderboard: top 3 authors by cumulative reviews
# reviews_by_year_author = df.groupby(["Year","Author"])["Reviews"].sum().reset_index()
# reviews_by_year_author["Rank"] = reviews_by_year_author.groupby("Year")["Reviews"].rank(method="dense", ascending=False)
# leaderboard_top3 = (
#     reviews_by_year_author[reviews_by_year_author["Rank"] <= 3]
#     .sort_values(["Year","Rank","Author"])
#     .reset_index(drop=True)
# )
# print("Q20) Year-wise top-3 authors by cumulative reviews:")
# print(leaderboard_top3.to_string(index=False))

# --- Optional: save useful tables ---
# pivot_counts.to_csv("q16_counts.csv", index=True)
# pivot_pct.to_csv("q16_percentages.csv", index=True)
# leaderboard_top3.to_csv("q20_leaderboard_top3.csv", index=False)
# avg_rating_by_year.to_csv("q5_avg_rating_by_year.csv")
# avg_reviews_by_year.to_csv("q6_avg_reviews_by_year.csv")
# avg_rating_authors_ge3.to_csv("q12_authors_ge3_avg_rating.csv")