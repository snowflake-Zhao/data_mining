import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

# Load the CSV file using pandas
data = pd.read_csv("dataset\\question3.csv")

# Split the data into features (X) and labels (y)
X = data.drop('Class', axis=1)  # Replace 'target_column_name' with the actual column name for your labels
X = pd.get_dummies(X)
y = data['Class']

# Create the Decision Tree classifier object
clf = DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.2)

# Train the Decision Tree classifier on your data
clf.fit(X, y)

tree.plot_tree(clf,feature_names=X.columns.tolist())
plt.show()