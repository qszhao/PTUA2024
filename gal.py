# coding: utf-8
get_ipython().system('pip install numpy')
import numpy as np
def read_gal_file(C:\PTUA\Lab04-1.gal):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            spatial_unit = int(parts[0])
            neighbors = list(map(int, parts[1:]))
            gal_dict[spatial_unit] = neighbors
    
    return gal_dict
def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            spatial_unit = int(parts[0])
            neighbors = list(map(int, parts[1:]))
            gal_dict[spatial_unit] = neighbors
    
    return gal_dict

# 提供你的文件路径
file_path = r"C:\PTUA\Lab04-1.gal"

# 调用read_gal_file函数
gal_dict = read_gal_file(file_path)

# 打印结果
print(gal_dict)
def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            try:
                spatial_unit = int(parts[0])
                neighbors = list(map(int, parts[1:]))
                gal_dict[spatial_unit] = neighbors
            except ValueError:
                # 忽略无法转换为整数的行
                pass
    
    return gal_dict
def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            try:
                spatial_unit = int(parts[0])
                neighbors = list(map(int, parts[1:]))
                gal_dict[spatial_unit] = neighbors
            except ValueError:
                # 忽略无法转换为整数的行
                pass
    
    return gal_dict
def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            try:
                spatial_unit = int(parts[0])
                neighbors = list(map(int, parts[1:]))
                gal_dict[spatial_unit] = neighbors
            except ValueError:
                # 忽略无法转换为整数的行
                pass
    
    return gal_dict

# 提供你的文件路径
file_path = r"C:\PTUA\Lab04-1.gal"

# 调用 read_gal_file 函数
gal_dict = read_gal_file(file_path)

# 打印结果
print("GAL Dictionary:", gal_dict)
import numpy as np

def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            try:
                spatial_unit = int(parts[0])
                neighbors = list(map(int, parts[1:]))
                gal_dict[spatial_unit] = neighbors
            except ValueError:
                # 忽略无法转换为整数的行
                pass
    
    return gal_dict

# 提供你的文件路径
file_path = r"C:\PTUA\Lab04-1.gal"

def neighbor_histogram(gal_dict):
    """
    获取GAL字典并返回第二个字典，其中包含邻居基数的直方图。
    在第二个字典中，键是邻居的数量，值是具有该数量邻居的ID列表。
    """
    histogram = {}
    
    for unit, neighbors in gal_dict.items():
        num_neighbors = len(neighbors)
        if num_neighbors not in histogram:
            histogram[num_neighbors] = []
        histogram[num_neighbors].append(unit)
    
    return histogram

def check_asymmetry(gal_dict):
    """
    测试GAL字典中是否存在任何不对称性。
    当i说j是i的邻居，但j却不说i是j的邻居时，发生不对称性。
    """
    for unit, neighbors in gal_dict.items():
        for neighbor in neighbors:
            if unit not in gal_dict.get(neighbor, []):
                return True
    
    return False
import numpy as np

def read_gal_file(file_path):
    """
    读取GAL文件并返回一个字典，其中键是空间单元的ID，值是其邻居的ID列表。
    """
    gal_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            try:
                spatial_unit = int(parts[0])
                neighbors = list(map(int, parts[1:]))
                gal_dict[spatial_unit] = neighbors
            except ValueError:
                # 忽略无法转换为整数的行
                pass
    
    return gal_dict

def neighbor_histogram(gal_dict):
    """
    获取GAL字典并返回第二个字典，其中包含邻居基数的直方图。
    在第二个字典中，键是邻居的数量，值是具有该数量邻居的ID列表。
    """
    histogram = {}
    
    for unit, neighbors in gal_dict.items():
        num_neighbors = len(neighbors)
        if num_neighbors not in histogram:
            histogram[num_neighbors] = []
        histogram[num_neighbors].append(unit)
    
    return histogram

def check_asymmetry(gal_dict):
    """
    测试GAL字典中是否存在任何不对称性。
    当i说j是i的邻居，但j却不说i是j的邻居时，发生不对称性。
    """
    for unit, neighbors in gal_dict.items():
        for neighbor in neighbors:
            if unit not in gal_dict.get(neighbor, []):
                return True
    
    return False

# 调用read_gal_file函数
gal_dict = read_gal_file(file_path)
print("GAL Dictionary:", gal_dict)

# 调用neighbor_histogram函数
histogram = neighbor_histogram(gal_dict)
print("Neighbor Histogram:", histogram)

# 调用check_asymmetry函数
has_asymmetry = check_asymmetry(gal_dict)
print("Has Asymmetry:", has_asymmetry)
# 在 Jupyter Notebook 中的一个代码单元中运行
get_ipython().run_line_magic('save', 'gal.py 1-25')
# 在 Jupyter Notebook 中的一个代码单元中运行
get_ipython().run_line_magic('save', 'gal.py 1-25')
