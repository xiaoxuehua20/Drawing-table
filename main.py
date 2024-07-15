import tkinter as tk
import re
import matplotlib.pyplot as plt
import random

# 窗口基本信息
window = tk.Tk()
window.title("绘图可视化操作")
window.geometry("1000x700")

# 图形类型选择
choose_picture_type = tk.StringVar()

# 坐标生成工具
choose_generate = tk.StringVar()    # 选择顺序生成或随机生成
# 起始值
tk.Label(window,text="起始值",font=20,width=5,height=2).place(x=100,y=180)
start = tk.Entry(window,show=None)
start.place(x=175,y=190)
# 结束值
tk.Label(window,text="结束值",font=20,width=5,height=2).place(x=100,y=210)
end = tk.Entry(window,show=None)
end.place(x=175,y=220)
# 步长
tk.Label(window,text="步长",font=20,width=5,height=2).place(x=100,y=240)
step = tk.Entry(window,show=None)
step.place(x=175,y=250)
# 数据个数
display_number = tk.Label(window,text="数据个数",font=20,width=7,height=2)
display_number.place(x=100,y=270)
number = tk.Entry(window,show=None)
number.place(x=175,y=280)
# 生成显示
display_generate = tk.Text(window,height=3)
display_generate.place(x=350,y=240)
# 生成函数
def generate():
    x1 = []
    start_1 = int(start.get())
    end_1 = int(end.get())
    step_1 = int(step.get())
    if choose_generate.get() == "顺序生成":
        for item in range(start_1,end_1,step_1):
            x1.append(item)
    else:
        number_1 = int(number.get())
        for i in range(number_1):
            x1.append(random.randrange(step_1,end_1+1,step_1))
    display_generate.insert("insert",str(x1))
# 生成按钮
tk.Button(window,text="点击生成",width=8,height=1,command=generate).place(x=350,y=190)
# 隐藏_生成工具
def choose_display():
    if choose_generate.get() == "顺序生成":
        display_number.place_forget()
        number.place_forget()
    else:
        display_number.place(x=100,y=270)
        number.place(x=175,y=280)
tk.Label(window,text="坐标生成工具",font=20,width=15,height=2).place(x=100,y=150)
order = tk.Radiobutton(window,text="顺序生成",value="顺序生成",variable=choose_generate,command=choose_display)
order.place(x=250,y=155)
random_ = tk.Radiobutton(window,text="随机生成",value="随机生成",variable=choose_generate,command=choose_display)
random_.place(x=350,y=155)

# 坐标输入
x_tk = tk.Label(window,text="x轴输入",font=20,width=8,height=2)
x_tk.place(x=100,y=320)
x = tk.Text(window,height=3)
x.place(x=180,y=320)
y_tk = tk.Label(window,text="y轴输入",font=20,width=8,height=2)
y_tk.place(x=100,y=370)
y = tk.Text(window,height=3)
y.place(x=180,y=370)

# 参数设置
tk.Label(window,text="参数设置",font=20,width=8,height=2).place(x=100,y=420)
# 散点图参数
# 大小,宽度
size_tk = tk.Label(window,text="大小",font=20,width=5,height=2)
size_tk.place(x=100,y=460)
size = tk.Entry(window,show=None)
size.place(x=150,y=470)
# 颜色
color_tk = tk.Label(window,text="颜色",font=20,width=5,height=2)
color_tk.place(x=310,y=460)
color = tk.Entry(window,show=None)
color.place(x=360,y=470)
# 样式,类型
mark_tk = tk.Label(window,text="样式",font=20,width=5,height=2)
mark_tk.place(x=520,y=460)
mark = tk.Entry(window,show=None)
mark.place(x=570,y=470)
# 底座坐标
buttom_tk = tk.Label(window,text="底座",font=20,width=5,height=2)
buttom_tk.place(x=730,y=460)
buttom = tk.Entry(window,show=None)
buttom.place(x=780,y=470)
# 饼图间隔
explore_tk = tk.Label(window,text="间隔",font=20,width=5,height=2)
explore_tk.place(x=100,y=490)
explore = tk.Entry(window,show=None)
explore.place(x=150,y=500)
# 饼图标签
label_tk = tk.Label(window,text="标签",font=20,width=5,height=2)
label_tk.place(x=310,y=490)
label = tk.Entry(window,show=None)
label.place(x=360,y=500)
# 饼图百分比显示
percent_tk = tk.Label(window,text="百分比",font=20,width=5,height=2)
percent_tk.place(x=520,y=490)
percent = tk.Entry(window,show=None)
percent.place(x=570,y=500)
# 饼图标记位置
size_label_tk = tk.Label(window,text="标记位",font=20,width=5,height=2)
size_label_tk.place(x=730,y=490)
size_label = tk.Entry(window,show=None)
size_label.place(x=780,y=500)
# 饼图阴影
shadow_tk = tk.Label(window,text="阴影",font=20,width=5,height=2)
shadow_tk.place(x=100,y=520)
shadow = tk.Entry(window,show=None)
shadow.place(x=150,y=530)
# 饼图半径
radius_tk = tk.Label(window,text="半径",font=20,width=5,height=2)
radius_tk.place(x=310,y=520)
radius = tk.Entry(window,show=None)
radius.place(x=360,y=530)
# 饼图起始角度
angle_tk = tk.Label(window,text="始角度",font=20,width=5,height=2)
angle_tk.place(x=520,y=520)
angle = tk.Entry(window,show=None)
angle.place(x=570,y=530)
# 饼图是否逆时针绘制
direction_tk = tk.Label(window,text="方向",font=20,width=5,height=2)
direction_tk.place(x=730,y=520)
direction = tk.Entry(window,show=None)
direction.place(x=780,y=530)
# 饼图标签大小
size_label_text_tk = tk.Label(window,text="标签大小",font=20,width=8,height=2)
size_label_text_tk.place(x=100,y=550)
size_label_text = tk.Entry(window,show=None)
size_label_text.place(x=180,y=560)
# 饼图标签颜色
color_label_tk = tk.Label(window,text="标签颜色",font=20,width=8,height=2)
color_label_tk.place(x=340,y=550)
color_label = tk.Entry(window,show=None)
color_label.place(x=420,y=560)
# 饼图中心位置
center_size_tk = tk.Label(window,text="中心位置",font=20,width=8,height=2)
center_size_tk.place(x=580,y=550)
center_size = tk.Entry(window,show=None)
center_size.place(x=660,y=560)
# 饼图是否显示边框
frame_tk = tk.Label(window,text="边框",font=20,width=5,height=2)
frame_tk.place(x=100,y=580)
frame_ = tk.Entry(window,show=None)
frame_.place(x=150,y=590)
# x轴标签
label_x_tk = tk.Label(window,text="x标签",font=20,width=5,height=2)
label_x_tk.place(x=100,y=610)
label_x = tk.Entry(window,show=None)
label_x.place(x=150,y=620)
# y轴标签
label_y_tk = tk.Label(window,text="y标签",font=20,width=5,height=2)
label_y_tk.place(x=310,y=610)
label_y = tk.Entry(window,show=None)
label_y.place(x=360,y=620)
# 标题
title_tk = tk.Label(window,text="标题",font=20,width=5,height=2)
title_tk.place(x=520,y=610)
title = tk.Entry(window,show=None)
title.place(x=570,y=620)

# 隐藏_类型选择
def type_display():
    if choose_picture_type.get() == "散点图":
        # 放置
        size.place(x=150,y=470)
        size_tk.place(x=100,y=460)
        color_tk.place(x=310,y=460)
        color.place(x=360,y=470)
        mark_tk.place(x=520,y=460)
        mark.place(x=570,y=470)
        x_tk.place(x=100,y=320)
        x.place(x=180,y=320)
        y_tk.place(x=100,y=370)
        y.place(x=180,y=370)
        # 隐藏
        buttom.place_forget()
        buttom_tk.place_forget()
        explore.place_forget()
        explore_tk.place_forget()
        label.place_forget()
        label_tk.place_forget()
        percent.place_forget()
        percent_tk.place_forget()
        size_label.place_forget()
        size_label_tk.place_forget()
        shadow.place_forget()
        shadow_tk.place_forget()
        radius.place_forget()
        radius_tk.place_forget()
        angle.place_forget()
        angle_tk.place_forget()
        direction.place_forget()
        direction_tk.place_forget()
        size_label_text.place_forget()
        size_label_text_tk.place_forget()
        color_label.place_forget()
        color_label_tk.place_forget()
        center_size.place_forget()
        center_size_tk.place_forget()
        frame_.place_forget()
        frame_tk.place_forget()
    elif choose_picture_type.get() == "折线图":
        # 放置
        size.place(x=150,y=470)
        size_tk.place(x=100,y=460)
        color_tk.place(x=310,y=460)
        color.place(x=360,y=470)
        mark_tk.place(x=520,y=460)
        mark.place(x=570,y=470)
        x_tk.place(x=100,y=320)
        x.place(x=180,y=320)
        y_tk.place(x=100,y=370)
        y.place(x=180,y=370)
        # 隐藏
        buttom.place_forget()
        buttom_tk.place_forget()
        explore.place_forget()
        explore_tk.place_forget()
        label.place_forget()
        label_tk.place_forget()
        percent.place_forget()
        percent_tk.place_forget()
        size_label.place_forget()
        size_label_tk.place_forget()
        shadow.place_forget()
        shadow_tk.place_forget()
        radius.place_forget()
        radius_tk.place_forget()
        angle.place_forget()
        angle_tk.place_forget()
        direction.place_forget()
        direction_tk.place_forget()
        size_label_text.place_forget()
        size_label_text_tk.place_forget()
        color_label.place_forget()
        color_label_tk.place_forget()
        center_size.place_forget()
        center_size_tk.place_forget()
        frame_.place_forget()
        frame_tk.place_forget()
    elif choose_picture_type.get() == "柱状图":
        # 放置
        color_tk.place(x=310,y=460)
        color.place(x=360,y=470)
        buttom_tk.place(x=730,y=460)
        buttom.place(x=780,y=470)
        x_tk.place(x=100,y=320)
        x.place(x=180,y=320)
        y_tk.place(x=100,y=370)
        y.place(x=180,y=370)
        # 隐藏
        size.place_forget()
        size_tk.place_forget()
        mark.place_forget()
        mark_tk.place_forget()
        explore.place_forget()
        explore_tk.place_forget()
        label.place_forget()
        label_tk.place_forget()
        percent.place_forget()
        percent_tk.place_forget()
        size_label.place_forget()
        size_label_tk.place_forget()
        shadow.place_forget()
        shadow_tk.place_forget()
        radius.place_forget()
        radius_tk.place_forget()
        angle.place_forget()
        angle_tk.place_forget()
        direction.place_forget()
        direction_tk.place_forget()
        size_label_text.place_forget()
        size_label_text_tk.place_forget()
        color_label.place_forget()
        color_label_tk.place_forget()
        center_size.place_forget()
        center_size_tk.place_forget()
        frame_.place_forget()
        frame_tk.place_forget()
    else:
        # 放置
        x_tk.place(x=100,y=320)
        x.place(x=180,y=320)
        # 颜色
        color_tk.place(x=310,y=460)
        color.place(x=360,y=470)
        # 饼图间隔
        explore_tk.place(x=100,y=490)
        explore.place(x=150,y=500)
        # 饼图标签
        label_tk.place(x=310,y=490)
        label.place(x=360,y=500)
        # 饼图百分比显示
        percent_tk.place(x=520,y=490)
        percent.place(x=570,y=500)
        # 饼图标记位置
        size_label_tk.place(x=730,y=490)
        size_label.place(x=780,y=500)
        # 饼图阴影
        shadow_tk.place(x=100,y=520)
        shadow.place(x=150,y=530)
        # 饼图半径
        radius_tk.place(x=310,y=520)
        radius.place(x=360,y=530)
        # 饼图起始角度
        angle_tk.place(x=520,y=520)
        angle.place(x=570,y=530)
        # 饼图是否逆时针绘制
        direction_tk.place(x=730,y=520)
        direction.place(x=780,y=530)
        # 饼图标签大小
        size_label_text_tk.place(x=100,y=550)
        size_label_text.place(x=180,y=560)
        # 饼图标签颜色
        color_label_tk.place(x=340,y=550)
        color_label.place(x=420,y=560)
        # 饼图中心位置
        center_size_tk.place(x=580,y=550)
        center_size.place(x=660,y=560)
        # 饼图是否显示边框
        frame_tk.place(x=100,y=580)
        frame_.place(x=150,y=590)
        # 隐藏
        y.place_forget()
        y_tk.place_forget()
        buttom_tk.place_forget()
        buttom.place_forget()
        size_tk.place_forget()
        size.place_forget()
        mark.place_forget()
        mark_tk.place_forget()

# 图形类型选择
scatter_plot = tk.Radiobutton(window,text="散点图",value="散点图",variable=choose_picture_type,command=type_display)
scatter_plot.place(x=100,y=120)
line_chart = tk.Radiobutton(window,text="折线图",value="折线图",variable=choose_picture_type,command=type_display)
line_chart.place(x=180,y=120)
histogram = tk.Radiobutton(window,text="柱状图",value="柱状图",variable=choose_picture_type,command=type_display)
histogram.place(x=260,y=120)
pie = tk.Radiobutton(window,text="饼图",value="饼图",variable=choose_picture_type,command=type_display)
pie.place(x=340,y=120)

# 生成图
def create_b():
    plt.xlabel(label_x.get())
    plt.ylabel(label_y.get())
    plt.title(title.get())
    # 储存数据
    x1 = []
    for i in re.findall(r'\d+\.\d+|\d+',x.get('1.0','end')):
        x1.append(int(i))
    y1 = []
    result_image_choice = []
    for item in re.findall(r'\d',choice_image_number.get()):
        result_image_choice.append(int(item))
    if choose_picture_type.get() == "散点图":
        # 散点图
        for j in re.findall(r'\d+\.\d+|\d+',y.get('1.0','end')):
            y1.append(int(j))
        if color.get() == '':
            color_result = None
        else:
            color_result = color.get()
        if mark.get() == '':
            mark_result = None
        else:
            mark_result = mark.get()
        if size.get() == '':
            size_result = None
        else:
            size_result = int(size.get())
        axs[result_image_choice[0],result_image_choice[1]].scatter(x1,y1,c=color_result,s=size_result,marker=mark_result)
    elif choose_picture_type.get() == "折线图":
        # 折线图
        for j in re.findall(r'\d+\.\d+|\d+',y.get('1.0','end')):
            y1.append(int(j))
        if mark.get() == '':
            mark_result = None
        else:
            mark_result = mark.get()
        if color.get() == '':
            color_result = None
        else:
            color_result = color.get()
        if size.get() == '':
            size_result = None
        else:
            size_result = int(size.get())
        axs[result_image_choice[0],result_image_choice[1]].plot(x1,y1,lw=size_result,c=color_result,ls=mark_result)
    elif choose_picture_type.get() == "柱状图":
        # 柱状图
        for j in re.findall(r'\d+\.\d+|\d+',y.get('1.0','end')):
            y1.append(int(j))
        if color.get() == '':
            color_result = None
        else:
            color_result = color.get()
        if buttom.get() == '':
            buttom_result = None
        else:
            buttom_result = buttom.get()
        axs[result_image_choice[0],result_image_choice[1]].bar(x1,y1,color=color_result,bottom=buttom_result)
    else:
        # 饼图
        if color.get() == '':
            color_result_1 = None
        else:
            color_result_1 = []
            color_result = color.get()
            for item in re.findall(r'\w+',color_result):
                color_result_1.append(item)
        if explore.get() == '':
            explore_result_1 = None
        else:
            explore_result_1 =[]
            explore_result = explore.get()
            for item in re.findall(r'\d+\.\d+|\d+',explore_result):
                explore_result_1.append(float(item))
        if label.get() == '':
            label_result_1 = None
        else:
            label_result_1 = []
            label_result = label.get()
            for item in re.findall(r'\w+',label_result):
                label_result_1.append(item)
        if percent.get() == '':
            percent_result = None
        else:
            percent_result = percent.get()
        if size_label.get() == '':
            size_label_result = 0.5
        else:
            size_label_result = float(size_label.get())
        if shadow.get() == '':
            shadow_result = None
        else:
            shadow_result = True
        if radius.get() == '':
            radius_result = 1
        else:
            radius_result = float(radius.get())
        if angle.get() == '':
            angle_result = 0
        else:
            angle_result = int(angle.get())
        if direction.get() == '':
            direction_result = None
        else:
            direction_result = False
        if size_label_text.get() == '':
            size_label_text_result = 15
        else:
            size_label_text_result = float(size_label_text.get())
        if color_label.get() == '':
            color_label_result = 'k'
        else:
            color_label_result = color_label.get()
        if center_size.get() == '':
            center_size_result_1 = (0,0)
        else:
            center_size_result = center_size.get()
            center_size_result_1 = []
            for item in re.findall(r'\d+\.\d+|\d+',center_size_result):
                center_size_result_1.append(int(item))
        if frame_.get() == '':
            frame_result = None
        else:
            frame_result = True
        axs[result_image_choice[0],result_image_choice[1]].pie(x1,explode=explore_result_1,labels=label_result_1,colors=color_result_1,autopct=percent_result,labeldistance=size_label_result,shadow=shadow_result,radius=radius_result,startangle=angle_result,counterclock=direction_result,textprops={'fontsize':size_label_text_result,'color':color_label_result},center=center_size_result_1,frame=frame_result)
         
# 绘制多图
tk.Label(window,text="绘制多图",font=20,width=8,height=2).place(x=440,y=110)
image_number = tk.Entry(window,show=None)
image_number.place(x=520,y=120)
tk.Label(window,text="图数",font=20,width=5,height=2).place(x=680,y=110)
choice_image_number = tk.Entry(window,show=None)
choice_image_number.place(x=730,y=120)

def create_d():
    global axs
    result_image = []
    for item in re.findall(r'\d',image_number.get()):
        result_image.append(int(item))     
    fig,axs = plt.subplots(result_image[0],result_image[1])
        
# 绘制生成
create_image = tk.Button(window,text="多图生成",font=20,width=8,height=1,command=create_b)
create_image.place(x=890,y=115)
image_choice = tk.Button(window,text="确定",font=20,width=5,height=1,command=create_d)
image_choice.place(x=520,y=150)

# 生成按钮
def create_c():
    plt.show()
create = tk.Button(window,text="生成",font=20,bg='#9da5b4',fg='#23272e',highlightbackground='black',width=30,height=5,command=create_c)
create.pack()

window.mainloop()
