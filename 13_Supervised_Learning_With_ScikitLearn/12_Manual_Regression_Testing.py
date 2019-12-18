import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
df = pd.read_csv('../Dataset/Supervised Learning with scikit-learn/gm_2008_region.csv')

X = df['fertility'].values
Y = df['life'].values

# print(X[:5])
# print(Y[:5])


# [2.73 6.43 2.24 1.4  1.96]
# [75.3 58.3 75.5 72.5 81.5]

X_Bar = np.mean(X)
Y_Bar = np.mean(Y)

# print(X_Bar)
# print(Y_Bar)

# 3.005107913669065
# 69.60287769784172

# B1 = Summation((Xi-X_Bar)(Yi-Y_Bar)) / Summation((Xi-X_Bar)^2)
# B0 = Y_Bar - B1 * X_Bar

Summation_Numerator = np.sum((X-X_Bar) * (Y-Y_Bar))
Summation_Denominator = np.sum((X-X_Bar)**2)
# print(f"Numerator : {Summation_Numerator}") # -1600.2100431654676
# print(f"Denominator : {Summation_Denominator}") # 360.09307338129497

B1 = Summation_Numerator / Summation_Denominator
print(f"B1: {Summation_Numerator / Summation_Denominator}") # -4.443878989782841

B0 = Y_Bar - (B1 * X_Bar)
print(f"B0: {B0}") # 82.95721361742582

# # Y_Cap = 82.95721361742582 - 4.443878989782841 * X
Y_Cap = B0 - (B1 * X)
# print(Y_Cap)

# [70.82542398 54.38307171 73.00292468 76.73578303 74.2472108  76.69134424
#  74.11389443 74.55828233 72.38078162 74.82491507 76.64690545 74.86935386
#  70.02552576 59.53797134 71.80307735 67.49251473 70.24771971 74.51384354
#  76.60246666 56.11618452 54.16087776 69.4033827  59.98235924 75.49149691
#  52.6943977  74.55828233 72.15858767 60.51562472 60.29343077 74.46940475
#  61.13776778 76.60246666 76.29139513 74.55828233 66.24822862 70.82542398
#  69.8477706  72.64741436 59.36021618 60.02679803 75.75812965 70.78098519
#  74.73603749 74.20277201 63.93741154 57.18271548 75.00267023 76.8690994
#  64.33736065 76.46915029 64.64843218 59.22689981 59.62684892 70.78098519
#  67.40363715 68.42572932 77.04685456 73.53619016 71.22537308 71.93639372
#  74.60272112 74.06945564 69.98108697 76.78022182 72.33634283 77.00241577
#  71.80307735 61.80434963 76.29139513 75.9803236  68.11465779 59.89348166
#  76.64690545 75.71369086 61.67103326 57.27159306 73.84726169 72.38078162
#  52.64995891 76.82466061 61.00445141 75.93588481 72.51409799 76.33583392
#  72.42522041 72.11414888 58.33812401 73.84726169 70.06996455 75.09154781
#  73.53619016 70.86986277 49.22817208 56.2050621  74.2472108  70.11440334
#  67.04812683 71.35868945 64.87062613 69.35894391 71.49200582 68.47016811
#  77.04685456 76.91353819 73.18067984 77.00241577 76.33583392 60.47118593
#  60.24899198 76.69134424 60.1601144  77.26904851 77.13573214 76.60246666
#  51.58342795 71.66976098 76.64690545 72.64741436 61.67103326 72.24746525
#  66.51486136 74.42496596 76.4247115  66.51486136 58.33812401 76.38027271
#  61.27108415 74.95823144 73.89170048 73.40287379 54.78302082 76.82466061
#  74.64715991 73.75838411 73.58062895 72.0252713  74.6915987  56.82720516
#  65.84827951]

# SSR = (Y_Cap - Y_Bar) ** 2
# print(np.sum(SSR)) # 7111.1397900625150.......................................

# SST = (Y - Y_Bar) ** 2
# print(SST)

# R_Square = np.sum(SSR)/np.sum(SST)
# print(f"R Square : {R_Square}") # 0.6192442167740037

# RMSE = np.sqrt(np.mean((Y - Y_Cap)**2))
# print(f"RMSE : {RMSE}") # 5.608600191393089
# y = df['life'].values

# X = X.reshape(-1, 1)
# y = Y.reshape(-1, 1)

# # # split data into train and test
# # # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# reg_all = LinearRegression()

# reg_all.fit(X, Y)

# y_pred = reg_all.predict(X)

# print(y_pred)
# SSResiduals = 4372.439058858349
# print(f"R^2: {reg_all.score(X,y)}") # R^2: 0.6192442167740035
# print(f"RMSE: {np.sqrt(mean_squared_error(y,y_pred))}") # 5.60860019139309
# ridge = Ridge(normalize=True)
# print(ridge)
# ridge.fit(X, Y)
# print(ridge.coef_)	# [-2.22193949]