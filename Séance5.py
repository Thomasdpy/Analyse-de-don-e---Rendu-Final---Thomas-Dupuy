import pandas as pd
from scipy.stats import shapiro

# Chemins locaux
df1 = pd.read_csv("/home/thomas04dupuy/Desktop/Loi-normale-Test-1 (1).csv")
df2 = pd.read_csv("/home/thomas04dupuy/Desktop/Loi-normale-Test-2.csv")

# Test de Shapiro-Wilk
stat1, p1 = shapiro(df1)
stat2, p2 = shapiro(df2)

print("Test 1 → Stat =", stat1, "p-value =", p1)
print("Test 2 → Stat =", stat2, "p-value =", p2)

# Interprétation
if p1 > 0.05:
    print("✅ Test 1 suit une distribution normale.")
else:
    print("❌ Test 1 ne suit pas une distribution normale.")

if p2 > 0.05:
    print("✅ Test 2 suit une distribution normale.")
else:
    print("❌ Test 2 ne suit pas une distribution normale.")

import matplotlib.pyplot as plt
df1.hist(bins=30)
plt.title("Distribution Test 1")
plt.show()

df2.hist(bins=30)
plt.title("Distribution Test 2")
plt.show()

