import matplotlib.pyplot as plt

# 创建一个图形对象和坐标轴对象
fig, ax = plt.subplots()

# 画出水平直线，y参数表示直线的y坐标，color参数表示线的颜色，linewidth参数表示线的粗细
horizontal_line_y = 2.5
ax.axhline(y=horizontal_line_y, color="lightblue", linewidth=10)

# 设置图形标题和坐标轴标签（可选）
ax.set_title("Horizontal Line Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# 显示图形
plt.show()
