#this is a demo file#


def list_algorithms(dataset):
    if dataset.lower() == "iris":
        print("Preferred algorithms for Iris dataset:")
        print("1. k-Nearest Neighbors (k-NN)")
        print("2. Support Vector Machine (SVM)")
        print("3. Decision Tree")
    elif dataset.lower() == "titanic":
        print("Preferred algorithms for Titanic dataset:")
        print("1. Logistic Regression")
        print("2. Random Forest")
        print("3. Gradient Boosting")
    elif dataset.lower() == "stock market":
        print("Preferred algorithms for Stock Market dataset:")
        print("1. Support Vector Machine (SVM)")
        print("2. Linear Regression")
        print("3. k-Nearest Neighbors (k-NN)")
        print("4. Naive Bayes")
    else:
        print("Dataset not recognized. Please select a valid dataset.")

# Example usage
selected_dataset = input("Enter the name of the dataset (iris/titanic/stock market): ")
list_algorithms(selected_dataset)



