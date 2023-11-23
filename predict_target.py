import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
data = pd.DataFrame({'Feature': X.flatten(), 'Target': y.flatten()})
X_train, X_test, y_train, y_test = train_test_split(data[['Feature']], data['Target'], test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
x_to_predict = np.array([[1.5]])
predicted_value = model.predict(x_to_predict)
print(f'Predicted Value for x={x_to_predict[0, 0]}: {predicted_value[0]}')
plt.scatter(X_test, y_test, alpha=0.5, label='Actual')
plt.plot(X_test, model.predict(X_test), color='red', linewidth=2, label='Regression Line')
plt.scatter(x_to_predict, predicted_value, color='green', marker='X', s=100, label='Predicted Value')
plt.title('Actual vs. Predicted Values with Linear Regression Line')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()
