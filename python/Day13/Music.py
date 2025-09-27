# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("vedikagupta0/youtube-top-100-songs-2025-dataset")
#
# print("Path to dataset files:", path)
import pandas as pd

d = pd.read_csv("youtube-top-100-songs-2025.csv")
print(d.head())
print(d.describe())
print(d.info())

print(d.loc[1])