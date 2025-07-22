<div style="display: flex; align-items: center; justify-content: center; text-align: center;">
  <img src="https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/219/original/CT_LOGO_NEW.jpg" width="100" style="margin-right: 10px;">
  <div>
    <h1><b>🧪 Lab - Wine Classifications</b></h1>
  </div>
</div>

## Data Set: 
The red and white wine dataset is a popular dataset used in machine learning and data analysis. It contains various chemical properties of different wine samples, and each sample is labeled as either red or white wine based on its characteristics. The dataset typically includes features such as acidity levels, residual sugar, alcohol content, and other chemical attributes that influence the quality and characteristics of the wine.

## Objective: 
The red and white wine dataset, featuring chemical properties of various wine samples labeled as red or white, serves a practical purpose in developing wine recommendation systems. Imagine a wine enthusiast exploring a recommendation app seeking guidance on their next wine selection. The ability to accurately identify whether a wine is red or white becomes instrumental in providing personalized suggestions. Red wines, with their rich and robust flavors, are apt for pairing with red meats, while white wines, known for their crispness, are versatile for lighter fare like seafood or poultry. This classification not only caters to individual preferences but also aids businesses, such as vineyards or restaurants, in effective inventory management and customer-targeted offerings.

For businesses, the distinction between red and white wines from the dataset becomes pivotal. It allows vineyards and retailers to streamline their product offerings, target specific consumer demographics, and optimize supply chain operations. By leveraging this information, businesses can enhance customer experiences, tailor marketing strategies, and ensure that their wine selection aligns with both individual preferences and broader industry trends. In essence, the red and white wine dataset, through its classification, opens avenues for personalized wine recommendations and facilitates strategic decision-making within the wine industry.

---

## PART 1: Data Cleaning
Before diving into the modeling process, it's crucial to ensure that your data is clean and ready for analysis.

- **Check null values:** Examine the dataset for any missing values. Addressing null values is essential to prevent issues during model training and evaluation.

- **Check dtypes:** Ensure that the data types of your features are appropriate. This step is important for avoiding potential discrepancies between the expected and actual data types.

## PART 2: Exploratory Data Analysis (EDA)
Exploring your data helps you gain insights and identify patterns or trends. Consider the following steps:

- **Visualize the data:** Utilize seaborn's `pairplot` to create a visual representation of relationships between different variables. This can offer a preliminary understanding of how features correlate with each other.
- Feel free to create other visualizations as well!
  
## PART 3: Modeling

Now that your data is clean and you've explored its characteristics, it's time to build and evaluate your models.

- **Establish baseline accuracy score:** Before training any models, establish a baseline accuracy score. This provides a benchmark for evaluating the performance of your models.

- **Train-test-split with `random_state = 42`:** Split your data into training and testing sets using `train_test_split` with a specified random state. This ensures reproducibility in your results.

- **Normalize your data with `StandardScaler`:** Standardize your features using `StandardScaler` to ensure that they are on a similar scale. This step is particularly important for algorithms sensitive to the scale of input features, such as K-Nearest Neighbors.

- **Evaluate K-Nearest Neighbors (KNN):**
  - Set \( k = 5 \) and calculate the training/testing accuracy scores. Explore whether the model performs better with other values of \( k \). <br>

- **Try Logistic Regression and RandomForestClassifier:**
  - Experiment with alternative models such as Logistic Regression and RandomForestClassifier. Compare their performance against the KNN model to identify the most suitable algorithm for your specific classification task.
  - For each model, include a confusion matrix to assess its performance in terms of true positives, true negatives, false positives, and false negatives.
