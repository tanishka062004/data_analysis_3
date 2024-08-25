import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv("Iris.csv")

# List of features
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Create histograms
for feature in features:
    plt.figure()
    plt.hist(iris[feature], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.show()
