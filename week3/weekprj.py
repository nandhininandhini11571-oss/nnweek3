import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd
bmw=pd.read_csv("BMW_data.csv ")
print(bmw)
print("Min Max Scaler")
numeric_col=bmw.select_dtypes(include=['int64','float64']).columns
scaler=MinMaxScaler()
bmw_normalized=pd.DataFrame(scaler.fit_transform(bmw[numeric_col]),columns=numeric_col)
print(bmw_normalized.head())
print("Standard Scaler")
numeric_col1=bmw.select_dtypes(include=['int64','float64']).columns
scaler=StandardScaler()
bmw_standardized=pd.DataFrame(scaler.fit_transform(bmw[numeric_col1]),columns=numeric_col1)
print(bmw_standardized.head())
plt.figure(figsize=(8,6))
plt.hist(bmw['Mileage_KM'],bins=5)
plt.title("Distribution of Sales of BMW", )
plt.xlabel(" Mileage_KM")
plt.ylabel("Frequency")
plt.show()

