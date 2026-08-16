import pandas as pd

df = pd.read_csv(r"/data/data5.8.csv")

diem = list(df["Điểm Số"])

# Tìm Min
min_value = diem[0]

for x in diem:
    if x < min_value:
        min_value = x

print("Min =", min_value)

# Tìm Max
max_value = diem[0]

for x in diem:
    if x > max_value:
        max_value = x

print("Max =", max_value)

# Tìm Mean
tong = 0

for x in diem:
    tong += x

mean = tong / len(diem)

print("Mean =", mean)

# Tìm Median
diem.sort()

n = len(diem)

if n % 2 == 1:
    median = diem[n // 2]
else:
    median = (diem[n // 2 - 1] + diem[n // 2]) / 2

print("Median =", median)

# Tìm Mode
dem = {}

for x in diem:
    if x in dem:
        dem[x] += 1
    else:
        dem[x] = 1

mode = None
max_dem = 0

for x in dem:
    if dem[x] > max_dem:
        max_dem = dem[x]
        mode = x

print("Mode =", mode)

# tim thanh pho co nhieu hoc sinh gioi nhat
gioi = df[df["Điểm Số"] >= 80]

ket_qua = gioi["Địa Chỉ"].value_counts()

print(ket_qua.to_string())

print("\nThành phố có nhiều điểm giỏi nhất:")
print(ket_qua.idxmax())
print("Số học sinh giỏi:", ket_qua.max())