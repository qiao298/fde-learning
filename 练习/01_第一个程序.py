# -*- coding: utf-8 -*-
"""
L1 预热 · 你的第一个 Python 程序
--------------------------------
怎么运行：在 VS Code 里打开这个文件，按 Ctrl + F5
怎么看结果：下面那个「终端」面板会打印出文字
"""

# ========== 1. 变量：给一个值起个名字 ==========
student = "qiao298"   # 字符串（文字）—— 要加引号
day = 5               # 整数（数字）—— 不加引号
hours = 4.5           # 小数

# ========== 2. f-string：把变量塞进文字里 ==========
# 注意每一行前面的 f，没有它 { } 里的变量不会被替换
print(f"你好，我是 {student}，这是我学 FDE 的第 {day} 天。")
print(f"今天计划学习 {hours} 小时。")
print("-" * 40)       # 打印 40 个横线，用来分隔内容

# ========== 3. 列表 list：一串有顺序的东西 ==========
# 方括号 [ ]，每一项用逗号隔开
tasks = [
    "变量与数据类型",
    "列表与字典",
    "if / for 循环",
    "写第一个函数",
    "异常处理",
]

# ========== 4. 字典 dict：带标签的一堆东西 ==========
# 大括号 { }，格式是「键: 值」
progress = {
    "变量与数据类型": True,
    "列表与字典": True,
    "if / for 循环": True,
    "写第一个函数": False,
    "异常处理": False,
}

# ========== 5. for 循环：把列表里每一项挨个拿出来 ==========
# enumerate 会额外给你一个序号，start=1 表示从 1 开始数
print("我的学习清单：")
for i, task in enumerate(tasks, start=1):
    mark = "✅" if progress[task] else "⬜"   # 完成了打勾，否则打框
    print(f"  {mark} {i}. {task}")

# ========== 6. 函数：把一段逻辑包起来，起个名字以后反复用 ==========
def count_done(progress: dict) -> int:
    """统计已完成的条目数。括号里的 progress 是输入，return 的是输出。"""
    n = 0
    for done in progress.values():   # .values() 取出所有「值」
        if done:
            n += 1                   # 等价于 n = n + 1
    return n

done = count_done(progress)          # 调用上面定义的函数
total = len(tasks)                   # len() 数一个列表有几项

print("-" * 40)
print(f"进度：{done} / {total} 项已完成")

# ========== 7. if 判断：根据不同情况走不同分支 ==========
if done == total:
    print("L1 全部学完，可以来考我了！")
else:
    print(f"还剩 {total - done} 项，继续加油。")
