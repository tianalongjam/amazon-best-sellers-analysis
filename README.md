# 📚 Amazon Top 50 Bestsellers (2009–2019) — Data Analysis with Pandas  

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.x-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-purple.svg)

## 🔎 Project Overview  
This project explores **Amazon’s Top 50 bestselling books from 2009 to 2019** (a dataset of 550 entries).  
The goal is to analyze **trends in bestselling literature** using Python and pandas.
Key questions include:  
- Who are the most frequent bestselling authors?  
- How do Fiction vs Non Fiction books compare in price, popularity, and ratings?  
- Which books stayed on the bestseller list across multiple years?  
- How have ratings and reviews evolved over time?  
- Is there a relationship between price, reviews, and ratings?  

---

## 🗂 Dataset Description  
The dataset contains **550 rows** (50 bestsellers × 11 years).  

| Column       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `Title`       | Book title                                                                 |
| `Author`     | Book author                                                                |
| `Rating`| Average Amazon rating (0–5)                                                |
| `Reviews`    | Number of user reviews                                                     |
| `Price`      | Book price in USD (as of 2020)                                             |
| `Year`       | Year when the book ranked in the Top 50                                    |
| `Genre`      | Categorized into **Fiction** or **Non Fiction** (via Goodreads metadata)   |

---

## 🎯 Key Objectives  
- Identify **recurring bestselling authors** and books across multiple years.  
- Compare **Fiction vs Non Fiction** in terms of price, popularity, and user ratings.  
- Track **user review and rating trends** from 2009–2019.  
- Explore correlations between **price, reviews, and ratings**.  
- Build **yearly leaderboards** of top authors by cumulative reviews.  

---

## 📊 Analysis Highlights  

1. **Author Popularity**  
- Jeff Kinney (*Diary of a Wimpy Kid* series) was the most frequent author (12 appearances).  

2. **Price Trends**  
- Non Fiction bestsellers were more expensive on average and had higher price variability.  

3. **Most Reviewed Book**  
- *Where the Crawdads Sing* by Delia Owens (2019) → ~88,000 reviews.  

4. **Genre Distribution**  
- Fiction dominated early years, but Non Fiction grew in share over time.  

5. **Multi-Year Bestsellers**

- The Very Hungry Caterpillar, Oh, the Places You’ll Go!, and StrengthsFinder 2.0 appeared across 5 years.

6. **Author Consistency**

- J.K. Rowling achieved one of the highest average ratings among authors with 3+ bestsellers.

7. **Ratings Trend**

- Bestseller ratings stayed consistently high (avg ~4.6–4.7), with a slight upward trend by 2019.

## 🛠 Tools & Libraries

- Python

- pandas

- numpy

- matplotlib

- Jupyter Notebook

## ✅ Outcomes

This project provides insights into what drives a book to become a bestseller on Amazon, highlighting patterns in:

Genre dominance

Author influence

Pricing strategy

Reader engagement (reviews & ratings)

It also demonstrates practical use of pandas groupby, pivot tables, correlation analysis, and visualization to answer real-world data questions.
