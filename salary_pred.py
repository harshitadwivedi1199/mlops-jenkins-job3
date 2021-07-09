from sklearn.linear_model import LinearRegression
import pandas

db=pandas.read_csv("Salary_data.csv")
x=db["YearsExperience"].values.reshape(30,1)
y=db["Salary"]
model = LinearRegression()
model.fit(x,y)
print("---------------------------------------------------------------------------")
#exp=float(input("Enter your year of experience : "))
exp=$EXPERIENCE
output=model.predict([[float(exp)]])
print("Salary that u will get : Rs {}".format(output[0]))
print("---------------------------------------------------------------------------")

