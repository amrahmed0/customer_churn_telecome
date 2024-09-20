


# **Customer Churn Prediction Project**

## **Overview**
This project aims to build a Machine Learning (ML) model that predicts whether a customer will churn (leave the service) based on a set of features such as age, subscription tenure, number of support calls, etc.  
The model has been trained using customer data, and an API has been developed using **Flask** to allow users to send requests and receive churn predictions.

---

## **Objectives**
- Build a machine learning model capable of predicting customer churn based on specified features.
- Develop an API using **Flask** that allows users to submit customer data and get predictions on whether the customer will churn.

---

## **Key Steps in the Project**

### **1. Data Preparation**

#### **a. Data Collection:**
A dataset containing customer information was used, including:
- Age
- Subscription tenure
- Number of support calls
- Payment delays
- Total spend
- Subscription type (Basic, Standard, Premium)
- Contract length (Monthly, Quarterly, Annual)

#### **b. Data Processing:**
- **Data Cleaning**: Missing values were handled, and incorrect data types were corrected.
- **Feature Encoding**: **One-Hot Encoding** was used to convert categorical features (e.g., gender, subscription type, contract length) into a numerical format that the model can understand.

#### **c. Data Splitting:**
- **Training Set**: Used to train the model.
- **Test Set**: Used to evaluate the model.

---

### **2. Building the Machine Learning Model**

#### **a. Model Selection:**
A **Random Forest Classifier** was chosen for predicting customer churn due to its ability to handle multi-dimensional data and its feature importance capabilities.

#### **b. Model Training:**
The model was trained using the training set, with hyperparameter tuning to ensure accurate results.

#### **c. Model Evaluation:**
The model was evaluated using several performance metrics such as:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

The model performed well on the test set, achieving an accuracy of **93%** and a high recall of **98%**.

#### **d. Saving the Model:**
The trained model was saved in a file **`model.pkl`** for later use in the API.

#### **e. Saving the Encoder:**
The **One-Hot Encoder** used to encode categorical features was saved in **`encoder.pkl`** so it can be reused during predictions in the API.

---

### **3. Creating the API with Flask**

#### **a. Flask API Development:**
A **Flask** API was created to handle requests and provide churn predictions based on the input customer data.

#### **b. Endpoint for Prediction:**
The main endpoint **`/predict`** accepts a **POST** request with customer features and returns a prediction on whether the customer will churn.

#### **c. Input Validation:**
The API validates the input data to ensure that all fields are provided in the correct format (e.g., integers for numerical fields, strings for categorical fields).

