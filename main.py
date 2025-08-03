import pandas as pd
import numpy as np


user_ids = []
# 創造 100 個 UID
for i in range(100):
    uid = f"user_{i:03d}"  # 格式化 UID 為 user_000, user_001, ..., user_099
    user_ids.append(uid)


col_a = []
col_c = []

for i in range(30):
    # 填補 col_a

    # 選擇人數
    num_people = np.random.randint(1, 10)

    # 選擇人員
    people = np.random.choice(user_ids, size=num_people, replace=False)

    col_a.append(", ".join(people))


    # 填補 col_c
    num_people = np.random.randint(1, 4)

    # 選擇人員
    people = np.random.choice(user_ids, size=num_people, replace=False)

    col_c.append(", ".join(people))



# 隨機抽取 30 個人作為 col_b 的人員
col_b = list(np.random.choice(user_ids, size=30, replace=False))

# 創建 DataFrame
df = pd.DataFrame({
    "col_a": col_a,
    "col_b": col_b,
    "col_c": col_c
})

df.to_csv("docs/data/001_example.tsv", sep="\t", index=False)
