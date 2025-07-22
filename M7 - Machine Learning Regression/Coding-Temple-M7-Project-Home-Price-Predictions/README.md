# 🏡 Ames Housing Data and Kaggle Challenge

Welcome to our next project! It's time to start exploring and modeling. 🚀

# Part 1: Exploratory Data Analysis (EDA) and Data Cleaning 🧑‍🔬

### **Primary Learning Objectives:**

1. Understand the Ames Housing dataset through EDA. 📊
2. Perform any necessary data cleaning and feature engineering. 🧹
3. Prepare a clean dataset for modeling. ✔️

### **Exploring the Dataset**

You will start by exploring the Ames Housing dataset, which contains over 70 features related to the properties in Ames, Iowa. Your goal is to identify relationships, correlations, and any potential outliers that could affect the prediction model later on.

In the `EDA.ipynb` notebook, you will:

1. Load and inspect both `train.csv` and `test.csv`. 🔍
2. **Review the [data dictionary](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)** to understand the meaning of each feature in the dataset. This is crucial for making informed decisions during your analysis.
3. Conduct Exploratory Data Analysis (EDA) by:
    - Analyzing distributions of key features. 📈
    - Identifying missing data and handling it appropriately (e.g., filling or removing). ❓
    - Identifying correlations between features and the target (sale price). 🔗
    - Visualizing relationships between variables using plots (e.g., histograms, scatter plots, heatmaps). 🎨
    - Identifying and handling outliers. ⚠️
4. Perform feature engineering:
    - Create new features or transform existing ones if necessary. 🔄
5. Clean the data:
    - **For `train.csv`**: Handle missing values and remove or impute outliers. 🗑️
    - **For `test.csv`**: Apply the same cleaning methods used for `train.csv` to ensure consistency, but **do not drop any rows** from `test.csv`. 🚫
6. At the end of your EDA, you should have a clean dataset ready for modeling.

### **Saving the Cleaned Datasets**

Once you have completed the EDA and data cleaning, **save your cleaned dataframes** as new CSV files. These files will be used for the next step, where you'll build your regression model. Name the files `cleaned_train_data.csv` and `cleaned_test_data.csv`.

- Save your work in `EDA.ipynb`. 💾
- Export the cleaned datasets using:
    ```python
    train_df.to_csv('cleaned_train_data.csv')
    test_df.to_csv('cleaned_test_data.csv')
    ```

### **Next Step**

You will use the cleaned datasets in the `modeling.ipynb` notebook, where you will create your regression model to predict house prices. 📉

---

## 📝 Rubric for Part 1: EDA and Data Cleaning

| Criteria                           | Excellent (4)                               | Good (3)                                   | Fair (2)                                    | Poor (1)                      |
|------------------------------------|---------------------------------------------|--------------------------------------------|---------------------------------------------|-------------------------------|
| **Dataset Exploration**            | Thorough exploration with clear insights.  | Good exploration with some insights.      | Limited exploration with few insights.      | No exploration or insights.   |
| **Data Cleaning**                  | Comprehensive cleaning, all issues addressed. | Good cleaning, most issues addressed.     | Some cleaning, but several issues remain.   | Little to no cleaning done.   |
| **Feature Engineering**            | Innovative and relevant new features created. | Some useful features created.              | Few relevant features created.              | No features created.          |
| **Documentation**                  | Clear and detailed comments throughout.    | Mostly clear comments, minor gaps.        | Some comments, but lacks clarity.          | No comments or documentation. |
| **CSV Export**                     | Successfully exported cleaned datasets.    | Exported with minor issues.                | Exported but incorrect format.              | No export done.               |

<br>

---

## 🚨 Stop Here! 🚨

Before continuing to Part 2, make sure you have completed all the steps in **Part 1** and have reviewed **Lesson 06: How to Submit Predictions on Kaggle**. Understanding how to format and submit your predictions correctly is crucial for your success in the Kaggle competition. 

**Do not proceed to Part 2 until you have completed this review.**

---

<br>


# Part 2: Modeling Process and Submission Guidelines 📈

Once you have completed your EDA and saved your cleaned datasets, you will now build a regression model in the `modeling.ipynb` notebook.

### **Set-Up** 🛠️

Before you begin working on the modeling process, please complete the following steps:

1. **Sign up for an account on [Kaggle](https://www.kaggle.com/)** if you haven’t already. You should have done this during prework!
2. **IMPORTANT**: Click this link ([Regression Challenge Sign Up](https://www.kaggle.com/t/410f6c886b16445bbe141492b7215311)) to **join the competition** (otherwise, you will not be able to make submissions!).
3. Review the material on the [Coding Temple Regression Challenge](https://www.kaggle.com/competitions/coding-temple-regression-challenge/overview).
4. Review the [data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) for insights into the dataset's features.

Once these steps are completed, you are ready to start working on your model.

### **The Modeling Process**

In `modeling.ipynb`, you will:

1. Load the `cleaned_train_data.csv` and `cleaned_test_data.csv` files. 📥
2. Use the cleaned training data to create and refine a regression model.
    - Split your training data into training and testing sets. 🔄
    - Perform feature selection if necessary. ⚙️
    - Train the model using Linear Regression. 📊
    - Evaluate the performance using metrics like RMSE or R². 📈
3. Use the trained model to make predictions on the `cleaned_test_data.csv` dataset:
    - Format your CSV submission as required by Kaggle. 🗂️
    - Submit at least three times to see improvements over iterations. 🏆

### **Model Evaluation and Iteration**

1. Evaluate your model performance using appropriate metrics.
    - Consider baseline performance for comparison.
    - Look at how your model generalizes to new data.
    - Adjust and iterate on your model as needed.
2. You may not use advanced models like XGBoost or Neural Networks.

### **Submission**

By the end of the project, you will submit the following:

1. **Technical Report on GitHub**:
    - Create your own `README.md` file for this project. You can refer to the `README-Template.md` file as a starting point. After you’ve written your own `README.md`, make sure to **delete this current `README.md`** and rename your file to `README.md`, so it becomes the default file displayed on GitHub.
    - Your `EDA.ipynb` and `modeling.ipynb` notebooks.
    - Your final CSV submission files.
    - A PDF of your presentation slides. 📄
2. **Kaggle Submissions**:
    - Submit predictions on [Kaggle](https://www.kaggle.com/competitions/regression-challenge-bonfire-140/overview).
    - Make sure you see your name on the leaderboard. 🥇
3. **Presentation**:
    - Similar to our other projects, you will record a 5-10 minute presentation. Be sure to **introduce the project** and mention who your **audience** could be (e.g., stakeholders or organizations who would benefit from this model). 
    - Include **visualizations** to support your findings, and walk through the **model performance** in detail. 
    - Conclude with your **key takeaways** or **recommendations** based on the model's results and its potential applications.



## 📝 Rubric for Part 2: Modeling and Kaggle Submission

| Criteria                           | Excellent (4)                               | Good (3)                                   | Fair (2)                                    | Poor (1)                      |
|------------------------------------|---------------------------------------------|--------------------------------------------|---------------------------------------------|-------------------------------|
| **Model Selection and Performance** | Chose appropriate model(s) with excellent performance (e.g., low RMSE, high R²). Clearly explains reasoning behind model selection. | Selected an appropriate model with reasonable performance. Some explanation of model choice provided. | Model selected but poor performance or lack of explanation. | Model selection inappropriate for the task or underperforming. |
| **Model Iteration and Tuning**     | Multiple iterations and improvements shown through tuning or feature engineering. Results improve across iterations. | Some iterations and improvements made, with minor tuning or feature adjustments. | Few iterations and minimal model refinement, showing little improvement. | No iterations made; model performance remains unchanged. |
| **Evaluation Metrics**             | Proper use of evaluation metrics (e.g., RMSE, R²) to assess model performance. Detailed analysis of metrics provided. | Metrics are used correctly, but analysis lacks depth or explanation. | Some metrics used, but analysis is incomplete or inaccurate. | Metrics are not used or are applied incorrectly. |
| **Kaggle Submission**              | Submitted correctly, following Kaggle's requirements. At least 3 additional submissions made with consistent improvement in results. | Submitted correctly with 2-3 additional submissions, some improvement shown. | Submission made but format or method was incorrect, or only 1 additional submission made. | No submissions made or did not follow submission guidelines. |
| **Documentation in `modeling.ipynb`** | Thorough documentation of the modeling process with clear comments and markdown cells explaining each step. | Good documentation with some comments and markdown, but missing a few details. | Basic documentation; missing some critical explanations. | Little to no documentation present. |
| **Organization and File Structure** | Files and notebooks are well-organized, with clear structure and consistent naming. | Mostly organized, but some minor issues with file or notebook structure. | Organization lacking; files not named consistently or structure unclear. | Poor organization, files are messy or hard to navigate. |
| **Presentation**                   | Presentation is clear, engaging, and informative, introducing the project and target audience. Includes visualizations, walkthrough of model performance, and thoughtful conclusions/recommendations. | Presentation is clear and covers most key points, with some visualizations and a model performance explanation. Recommendations may lack depth. | Presentation lacks clarity or skips important sections. Few visualizations or limited explanation of model performance. | Presentation is unclear or incomplete, with minimal visualizations and no clear recommendations or conclusions. |

### Scoring Guide:

- **Excellent (4):** Exceeds expectations in all aspects, demonstrating a deep understanding of the modeling process and competition requirements.
- **Good (3):** Meets the requirements with minor areas for improvement.
- **Fair (2):** Some aspects are fulfilled, but significant improvements are needed in modeling or documentation.
- **Poor (1):** Does not meet expectations, with little to no effort or understanding demonstrated.

