import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from math import comb

df = pd.read_csv('Salary_Data.csv')

x = df[["YearsExperience"]]
y = df['Salary']

split = 0.8

combinations = comb(len(x), int(split*len(x)))
print(combinations)

model = LinearRegression()
# 4272047
# combinations_dict = dict()

# for combination in range(combinations):
#     x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=combination)
#     model.fit(x_train, y_train)
#     combinations_dict[combination] = r2_score(y_test, model.predict(x_test))
#
# sorted_dict_values_list = sorted(combinations_dict)
# best_combination = sorted_dict_values_list[-1]
# print(best_combination)

# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=4272047)
# model.fit(x_train, y_train)