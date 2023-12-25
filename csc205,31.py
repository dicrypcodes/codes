import numpy as np
from scipy.stats import skew, kurtosis

# Given data
age = np.array([25,26,25,23,30,29,23,34,40,30,51,46])
rating = np.array([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])

# Descriptive statistics
mean_age = np.mean(age)
median_age = np.median(age)
mode_age = np.argmax(np.bincount(age))
skewness_age = skew(age)
kurtosis_age = kurtosis(age)

mean_rating = np.mean(rating)
median_rating = np.median(rating)
mode_rating = np.argmax(np.bincount(rating.astype(int)))  # Note: Mode for continuous data is less straightforward
skewness_rating = skew(rating)
kurtosis_rating = kurtosis(rating)

# Output
print("Age:")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Mode: {mode_age}")
print(f"Skewness: {skewness_age}")
print(f"Kurtosis: {kurtosis_age}")
print("\nRating:")
print(f"Mean: {mean_rating}")
print(f"Median: {median_rating}")
print(f"Mode: {mode_rating}")
print(f"Skewness: {skewness_rating}")
print(f"Kurtosis: {kurtosis_rating}")


import scipy.stats as stats

# Parameters of the normal distribution
mu = 65  # Mean
sigma = 19  # Standard deviation

# Calculate the probability that a student scored more than 70
probability_more_than_70 = 1 - stats.norm.cdf(70, loc=mu, scale=sigma)

# Convert the probability to a percentage
percentage_more_than_70 = probability_more_than_70 * 100

print(f"The percentage of students who scored more than 70 is approximately {percentage_more_than_70:.2f}%")
