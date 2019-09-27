import matplotlib.pyplot as plt

# 我也可以指定输入参数和输出参数，这样就能按照我的意愿绘制图形了
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

dic = {'a':2, 'b':5, 'c':6, 'd':1, 'e':8}
dict = tuple(dic.keys())
nums = tuple(dic.values())
input_values = (dict) # 指定输入参数
squares = (nums)  # 指定输出参数
plt.plot(input_values, squares)  # 调用绘制函数，传入输入参数和输出参数
plt.title("Square Numbers")  # 指定标题，并设置标题字体大小
plt.xlabel("Value")  # 指定X坐标轴的标签，并设置标签字体大小
plt.ylabel("Square of Value")  # 指定Y坐标轴的标签，并设置标签字体大小
plt.tick_params(axis='both')  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
plt.show()  # 打开matplotlib查看器，并显示绘制的图形