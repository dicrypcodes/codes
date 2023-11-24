"""# Importing the useful library
import scipy.stats as stats
# Assigning the parameter of the distribution
mean = 65
std_dev = 19
#defining the cutoff score
cutoff_score = 70
#calculating the probability that a student scored more than 70
prob_more_than_70 = 1 - stats.norm.cdf #(cutoff_score, 1oc=mean, scale=std_dev)
#convert the probability to percentage
perc_more_than_70 = prob_more_than_70 * 100
print(perc_more_than_70)

print("The percentage of students who scored more than 70 is : + str(perc_more_than)")

"""

"""import scipy.stats as stats

# Parameters of the normal distribution
mean = 65  # Mean score
std_dev = 19  # Standard deviation

# Define the normal distribution
normal_dist = stats.norm(loc=mean, scale=std_dev)

# Calculate the percentage of students who scored more than 70
percentage_above_70 = 100 * (1 - normal_dist.cdf(70))

print(f"{percentage_above_70:.2f}% of students scored more than 70.")
"""
"""import scipy.stats as stats

# Parameters of the normal distribution
mu = 65  # Mean
sigma = 19  # Standard deviation

# Calculate the probability that a student scored more than 70
probability_more_than_70 = 1 - stats.norm.cdf(70, loc=mu, scale=sigma)

# Convert the probability to a percentage
percentage_more_than_70 = probability_more_than_70 * 100

print(f"The percentage of students who scored more than 70 is approximately {percentage_more_than_70:.2f}%")"""

"""import scipy.stats as stats

# Parameters of the normal distribution
mu = 65  # Mean
sigma = 19  # Standard deviation

# Calculate the probability that a student scored more than 70
probability_more_than_70 = 1 - stats.norm.cdf(70, loc=mu, scale=sigma)

# Convert the probability to a percentage
percentage_more_than_70 = probability_more_than_70 * 100

print(f"The percentage of students who scored more than 70 is approximately {percentage_more_than_70:.2f}%")
"""

"""import scipy.stats as stats
mean = 65
std_dev = 19
cutoff_score = 70
prob_more_than_70 = 1 - stats.norm.cdf(cutoff_score, loc=mean, scale = std_dev)
perc_more_than_70 = prob_more_than_70 * 100
print(perc_more_than_70)
"""
import scipy.stats as stats

# Parameters of the normal distribution
mean = 65  # Mean
sigma = 19  # Standard deviation

# Calculate the probability that a student scored more than 70
probability_more_than_70 = 1 - stats.norm.cdf(70, loc=mean, scale=sigma)

# Convert the probability to a percentage
percentage_more_than_70 = probability_more_than_70 * 100

print(f"The percentage of students who scored more than 70 is approximately {percentage_more_than_70:.2f}%")

