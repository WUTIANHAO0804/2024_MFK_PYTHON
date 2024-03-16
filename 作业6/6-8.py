# 读取输入文件
with open('input.txt', 'r') as file:
    lines = file.readlines()

# 创建一个字典，用于存储每个物种对应的动物ID
species_dict = {}

# 解析每一行数据，并将ID添加到相应的物种列表中
for line in lines:
    data = line.strip().split()
    animal_id = data[0]
    species = data[1]
    
    if species in species_dict:
        species_dict[species].append(animal_id)
    else:
        species_dict[species] = [animal_id]

# 按照物种名称的长度进行排序
sorted_species = sorted(species_dict.keys(), key=lambda x: len(x))

# 输出每个物种的所有动物ID
for species in sorted_species:
    animal_ids = ', '.join(sorted(species_dict[species]))
    print(f"{species}: {animal_ids}")