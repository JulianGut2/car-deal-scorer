import pandas as pd
from src.data_cleaner import clean_data
from src.model import train_model

df = pd.read_csv("data/vehicles.csv")

df = clean_data(df)

train_model(df)

from src.scorer import score_deal

print(score_deal(20000, 15000))
print(score_deal(20000, 20000)) 
print(score_deal(20000, 25000))  