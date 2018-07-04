import pandas as pb
import matplotlib.pyplot as plt

data = pb.read_csv("orders.csv")

data = data.groupby("days_since_prior_order").count()
data = data["order_id"]
print(data)
data.plot()
plt.show()

