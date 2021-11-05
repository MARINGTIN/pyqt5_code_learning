"""
快速生成大量数据
制作一个包含800个数据的list，以便于pyqt6绘制测试
数据从-4 -> 4
"""
import numpy as np
import math

f1 = open('list_data.txt', 'a+')
print('read file', f1.read())
count = 0.01
data = 0
f1.write('list_data = [')
while count <= 6:
    data_str = '%.4f' % data
    f1.write(data_str)
    f1.write(', ')
    if (count*100) % 10 == 0:
        f1.write('\n')
    data = np.log(count)
    count += 0.01
f1.write(']')
f1.close()
