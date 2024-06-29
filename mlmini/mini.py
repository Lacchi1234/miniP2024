def list_algorithms(dataset):
    if dataset == "dataset1":
        print("Preferred algorithms for dataset1:")
        print("1. Algorithm A")
        print("2. Algorithm B")
    elif dataset == "dataset2":
        print("Preferred algorithms for dataset2:")
        print("1. Algorithm C")
        print("2. Algorithm D")
    elif dataset == "dataset3":
        print("Preferred algorithms for dataset3:")
        print("1. Algorithm E")
        print("2. Algorithm F")
    else:
        print("Dataset not recognized. Please select a valid dataset.")

# Example usage
selected_dataset = input("Enter the name of the dataset: ")
list_algorithms(selected_dataset)
