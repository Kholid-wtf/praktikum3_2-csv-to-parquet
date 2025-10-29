import pandas as pd
import os

# 1. muat file csv
df = pd.read_csv("data.csv")

# 2. simpan sebagai parquet
df.to_parquet("data.parquet")

# 3. bandingkan ukuran file
csv_size = os.path.getsize("data.csv") / 1e6
parquet_size = os.path.getsize("data.parquet") / 1e6

print("=== HASIL KONVERSI CSV → PARQUET ===")
print(f"Ukuran CSV     : {csv_size:.2f} MB")
print(f"Ukuran Parquet : {parquet_size:.2f} MB")
print(f"Rasio          : {csv_size / parquet_size:.2f}x lebih kecil")
