import pandas as pb
import matplotlib.pyplot as plt

data = pb.read_csv("order_products__train.csv")
values = []
data = data.groupby("product_id").count()
data = data.sort_values("order_id", ascending = [False])
data = data["order_id"]
print(data.head())


