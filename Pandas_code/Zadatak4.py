import pandas as pb


data = pb.read_csv("orders.csv")

data = data.groupby("order_dow").count()
data = data.sort_values("order_id", ascending = [False])
data = data["order_id"]
print(data.head())
