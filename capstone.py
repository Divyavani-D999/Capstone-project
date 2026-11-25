import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("retail.csv")


# ==========================================
# Task 3: Univariate Analysis
# ==========================================


# ------------------------------------------
# 3(a) Distribution of numerical variables
# ------------------------------------------

# Income
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Income", kde=True)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()


# Age
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Recency
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Recency", kde=True)
plt.title("Recency Distribution")
plt.xlabel("Recency")
plt.ylabel("Frequency")
plt.show()


# ------------------------------------------
# 3(b) Distribution of categorical variables
# ------------------------------------------

# Education
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Education")
plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()


# Marital Status
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Marital_Status")
plt.title("Marital Status Distribution")
plt.xlabel("Marital Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()


# Response
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="Response")
plt.title("Response Distribution")
plt.xlabel("Response")
plt.ylabel("Number of Customers")
plt.show()


# ------------------------------------------
# 3(c) Identify outliers using box plots
# ------------------------------------------

# Income
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Income")
plt.title("Income Outliers")
plt.xlabel("Income")
plt.show()


# Age
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Age")
plt.title("Age Outliers")
plt.xlabel("Age")
plt.show()


# Recency
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Recency")
plt.title("Recency Outliers")
plt.xlabel("Recency")
plt.show()
