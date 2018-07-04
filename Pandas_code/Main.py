import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("order_products__train.csv")

"""
print("Broj proizvoda: ", data["product_id"].size)
data = pd.read_csv("order_products__prior.csv")
print("Narudzbina ima: ", data["order_id"].size)
"""



data2 = data.groupby("order_id")["product_id"].count()
#data3 = data.groupby("product_id")["order_id"].count()

#BITNO
brpbn = data2.groupby("order_id").count()["eval_set"]



brpbn.plot()
plt.show()

