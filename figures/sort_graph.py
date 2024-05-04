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
for omp_threads in set(OMP_NUM_THREADS_values):
    x = [N_values[i] for i in range(len(N_values)) if OMP_NUM_THREADS_values[i] == omp_threads]
    y = [Time_values[i] for i in range(len(Time_values)) if OMP_NUM_THREADS_values[i] == omp_threads]
    plt.plot(x, y, marker='o', label=f'OMP_NUM_THREADS = {omp_threads}')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (array size)')
plt.ylabel('Time (s)')
plt.title('Time vs N with varying OMP_NUM_THREADS')
plt.grid(True)
plt.legend()
plt.show()
