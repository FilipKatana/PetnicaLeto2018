import pandas as pb


data = pb.read_csv("products.csv")
data = data.groupby("product_name")
