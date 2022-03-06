import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

data = pd.read_csv("data.csv",delimiter=";")
df = pd.DataFrame({'MPG': data['MPG'],'Cylinders': data['Cylinders'],'Horsepower':data['Horsepower'], 'Weight':data['Weight'], 'Acceleration': data['Acceleration']})
df = df[df['MPG'] != 0]
df = df[df['Horsepower'] != 0.0]

x = df.drop("MPG", axis=1).values
y = df["MPG"].values

k = 3

#split the dataset for training and tests
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=12345) #random is set for reproductability

#train and predict
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(x_train, y_train)
train_preds = knn_model.predict(x_train)
test_preds = knn_model.predict(x_test)

mse = mean_squared_error(y_test, test_preds)
rmse = sqrt(mse)
print("RMSE = {}".format(round(rmse,3)))

#set one Normalized colormap for both scatters
norm = plt.Normalize(min(min(y_test),min(test_preds)),max(max(y_test),max(test_preds)))
cmap = plt.cm.get_cmap('viridis', 256)
f, (ax1,ax2) = plt.subplots(1,2)

#prediction values
points1 = ax1.scatter(x_test[:, 1], x_test[:, 2], c=test_preds, s=40, cmap=cmap, norm=norm)
ax1.set_ylabel('Weight')
ax1.set_xlabel('Horsepower')
ax1.title.set_text("Tests Predictions")
f.colorbar(points1, ax=ax1)

#actual values
points1 = ax2.scatter(x_test[:, 1], x_test[:, 2], c=y_test, s=40, cmap=cmap,norm=norm)
ax2.set_ylabel('Weight')
ax2.set_xlabel('Horsepower')
ax2.title.set_text("Real Values")
f.colorbar(points1, ax=ax2)

plt.show()