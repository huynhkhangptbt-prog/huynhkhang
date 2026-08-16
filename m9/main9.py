import pandas as pd

df = pd.read_csv("data.csv")

nha_dat_nhat = df.loc[df["Giá bán (tổng)"].idxmax()]

print("NGÔI NHÀ ĐẮT NHẤT")
print(nha_dat_nhat)


nha_re_nhat = df.loc[df["Giá bán (tổng)"].idxmin()]

print("\nNGÔI NHÀ RẺ NHẤT")
print(nha_re_nhat)