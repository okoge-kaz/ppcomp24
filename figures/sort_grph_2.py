import matplotlib.pyplot as plt

# データファイルのパス
data_file = "data.txt"

# データを読み込む
N_values = []
Time_values = []
OMP_NUM_THREADS_values = []

with open(data_file, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:  # ヘッダーをスキップする
        parts = line.strip().split("|")
        N = int(parts[1].strip())
        Time = float(parts[2].strip().split()[0])
        OMP_NUM_THREADS = int(parts[3].strip())
        N_values.append(N)
        Time_values.append(Time)
        OMP_NUM_THREADS_values.append(OMP_NUM_THREADS)

# グラフ化
plt.figure(figsize=(10, 6))
for N in set(N_values):
    x = [OMP_NUM_THREADS_values[i] for i in range(len(OMP_NUM_THREADS_values)) if N_values[i] == N]
    y = [Time_values[i] for i in range(len(Time_values)) if N_values[i] == N]
    plt.plot(x, y, marker='o', label=f'N = {N}')

plt.xlabel('OMP_NUM_THREADS')
plt.ylabel('Time (s)')
plt.title('Time vs OMP_NUM_THREADS with varying N')
plt.grid(True)
plt.legend()
plt.show()
