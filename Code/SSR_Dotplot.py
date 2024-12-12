# First, let's load the data and analyze its structure.
import pandas as pd

# Load the uploaded data
file_path = '/mnt/data/image.png'
# Note: Create a dictionary
data_dict = {
    'Name of Model': ['E. Coli', 'B. Subtilis', 'C. Botulin', 'S. Aureus', 'S. Anterica', 
                      'P. Aeruginosa', 'S. Cerevisiae', 'C. Auris', 'A. Vaga', 'A. Thaliana', 
                      'C. Elegans', 'O. Latipes'],
    'RSS/ESS': [5.483, 14.494, 8.089, 9.874, 13.402, 7.241, 8.851, 9.417, 9.417, 6.278, 9.794, 8.869],
    'Constant': [0.102, 0.02, 0.009, 0.013, 0.021, 0.011, 0.001, 0.002, 0.002, 0.002, 0.002, 0],
    'N50 versus Missing': [-0.997, -0.988, -1, -0.996, -0.983, -0.996, -1, -1, -1, -1, -1, -1]
}

# Convert to DataFrame
df = pd.DataFrame(data_dict)

# Let's plot the scatter plot
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='RSS/ESS', y='Constant', hue='N50 versus Missing', palette='coolwarm', s=100)
plt.title("Scatter Plot of Constant vs RSS/ESS with Correlation as Hue")
plt.xlabel("RSS/ESS")
plt.ylabel("Constant")
plt.legend(title="N50 vs Missing", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
