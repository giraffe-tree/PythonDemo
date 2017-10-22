import json

# 将数据加载到一个列表中
filename = 'file/population_data.json'

def readFile():
    with open(filename) as f:
        pop_data = json.load(f)
        return pop_data

pop_data = readFile()

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name,':',population)



