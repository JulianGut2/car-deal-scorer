import pandas as pd
from src.data_cleaner import clean_data
from src.model import train_model

df = pd.read_csv("data/vehicles.csv")

df = clean_data(df)

train_model(df)