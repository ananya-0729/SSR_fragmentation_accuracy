import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'table.xlsx'  # Replace with your file path
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Cleaning and restructuring the data for the heatmap
# Extracting RSS/ESS columns only for the heatmap
heatmap_data = data.iloc[1:, [0, 1, 3, 5]]  # Selecting 'Name of Model' and RSS/ESS columns
heatmap_data.columns = ['Model', 'Missing', 'Missing_Penta', 'Missing_Hexa']

# Converting numerical columns to float for plotting
heatmap_data[['Missing', 'Missing_Penta', 'Missing_Hexa']] = heatmap_data[
    ['Missing', 'Missing_Penta', 'Missing_Hexa']
].astype(float)

# Setting 'Model' as the index for a clear heatmap
heatmap_data.set_index('Model', inplace=True)

# Plotting the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar_kws={'label': 'RSS/ESS Values'},
    linewidths=0.5,
)
plt.title("RSS/ESS Heatmap for Different Microbial Models")
plt.xlabel("Condition")
plt.ylabel("Microbial Model")
plt.tight_layout()
plt.show()
