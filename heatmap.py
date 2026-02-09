import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
excel_file_path = 'D:/133/ML/LOAD/Al2O3/inputdata-Al2O3.xlsx'
df = pd.read_excel(excel_file_path)

# 计算相关性矩阵
correlation_matrix = df.corr()

# 创建一个与相关性矩阵相同形状的布尔掩码，其中的 True 表示空白部分
mask = np.zeros_like(correlation_matrix, dtype=bool)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True)
plt.show()
plt.savefig('D:/133/ML/LOAD/Al2O3/111/heatmap.tif', dpi=600)



