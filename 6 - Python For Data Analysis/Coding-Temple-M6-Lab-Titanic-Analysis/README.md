<div style="display: flex; align-items: center; justify-content: center; text-align: center;">
  <img src="https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/219/original/CT_LOGO_NEW.jpg" width="100" style="margin-right: 10px;">
  <div>
    <h1><b>🧪 Lab - Titanic Analysis</b></h1>
  </div>
</div>

<br>


This module so far has been all about Pandas. For this lab, we're going to take a look at the Titanic manifest. We'll be exploring this data to see what we can learn regarding the survival rates of different groups of people. If you get stuck on a task, we challenge you to use Google to your advantage! We believe that using resources available to you *is* a career skill and we want to ensure you get plenty practice.

## Prework
Fork and clone this repo.

In the blank Jupyter notebook, follow the steps outlined below. **You'll be working with a blank notebook, which mirrors the real-world data analysis process!** To elevate your lab experience, I encourage you to add Markdown cells to separate your work and enhance readability. Use these cells to create headers for different sections, making your notebook well-organized and easy to follow.

## Step 1: Reading the data

1. Import `pandas`.
1. Load [train.csv](./data/train.csv) as a `pandas` DataFrame.
1. In each of the following sections, copy the question as a python comment, then answer the question with your own code.
1. Refer to the [Titanic Kaggle competition](https://www.kaggle.com/c/titanic/data) if you need an explanation for any of the columns.

## Step 2: Cleaning the data

1. Create a bar chart showing how many missing values are in each column
  - *Bonus* : Theres a good library for visualizing missing values called Missingno.
      - [Install Instructions](https://pypi.org/project/missingno/)
      - [Usage Documentation](https://github.com/ResidentMario/missingno)
2. Which column has the most `NaN` values? How many cells in that column are empty?
3. Delete all rows where `Embarked` is empty
4. Fill all empty cabins with **¯\\_(ツ)_/¯**

Note: `NaN`, empty, and missing are synonymous.

## Step 3: Feature extraction
1.  There are two columns that pertain to how many family members are on the boat for a given person. Create a new column called `FamilyCount` which will be the sum of those two columns.
2. Reverends have a special title in their name (`'Rev.'`). Create a column called `IsReverend`: 1 if they're a preacher, 0 if they're not.

## Step 4: Exploratory analysis 
_[`df.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) may be very useful._

1. What was the survival rate overall?
2. Which gender fared the worst? What was their survival rate?
3. What was the survival rate for each `Pclass`?
4. Did any reverends survive? How many?
5. What is the survival rate for cabins marked **¯\\_(ツ)_/¯**
6. What is the survival rate for people whose `Age` is empty?
7. What is the survival rate for each port of embarkation?
8. What is the survival rate for children (under 12) in each `Pclass`?
9. Did the captain of the ship survive? Is he on the list?
10. Of all the people that died, who had the most expensive ticket? How much did it cost?
11. Does having family on the boat help or hurt your chances of survival?
