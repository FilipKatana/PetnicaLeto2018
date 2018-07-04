import pandas as pb
import matplotlib.pyplot as plt

data = pb.read_csv("orders.csv")
data = data.sort_values("days_since_prior_order")
data = data.groupby("user_id").count()
data = data["order_id"].head()
print(data)

