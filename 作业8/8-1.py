import numpy as np

# 从input.txt中读取数据
with open('input.txt', 'r', encoding='utf-8') as f:
    data = [int(x) for x in f.read().split()]

# 计算中位数、算术平均数和标准差
median = np.median(data)
mean = np.mean(data)
std_dev = np.std(data)

# 将结果写入output.txt文件
#with open('out.txt', 'w') as f:
#    f.write(f"中位数: {median:.2f}\n")
#    f.write(f"算术平均数: {mean:.2f}\n")
#    f.write(f"标准差: {std_dev:.2f}\n")

print(f"{median:.2f}", end=' ')
print(f"{mean:.2f}", end=' ')
print(f"{std_dev:.2f}")