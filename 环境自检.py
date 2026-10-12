"""
环境自检脚本 —— 你的第一个 Python 程序
运行方式：在 VS Code 里打开这个文件，按 Ctrl+F5
"""

import sys
import platform
import shutil
import subprocess


def line(title):
    print("\n" + "=" * 52)
    print(f"  {title}")
    print("=" * 52)


def ok(msg):
    print(f"  [通过] {msg}")


def bad(msg):
    print(f"  [失败] {msg}")


def warn(msg):
    print(f"  [注意] {msg}")


line("1. Python 本身")
print(f"  版本号  : {sys.version.split()[0]}")
print(f"  解释器  : {sys.executable}")
print(f"  系统    : {platform.system()} {platform.release()} ({platform.machine()})")

v = sys.version_info
if v.major == 3 and v.minor >= 11:
    ok("Python 版本符合要求（需要 3.11 或更高）")
else:
    bad(f"Python 版本过低：{v.major}.{v.minor}，建议重装 3.13")


line("2. pip 包管理器")
try:
    import pip
    ok(f"pip 已就绪，版本 {pip.__version__}")
except ImportError:
    bad("pip 没找到，请运行：python -m ensurepip")

line("3. pip 下载源（国内镜像）")
try:
    out = subprocess.run(
        [sys.executable, "-m", "pip", "config", "get", "global.index-url"],
        capture_output=True, text=True, timeout=20
    ).stdout.strip()
    if "tuna" in out or "aliyun" in out or "ustc" in out or "douban" in out:
        ok(f"已使用国内镜像，装包会很快：{out}")
    elif out:
        warn(f"当前源是 {out}，如果不是国内镜像装包会很慢")
    else:
        warn("没配置镜像源，装包可能很慢")
except Exception as e:
    warn(f"读取 pip 配置时出错：{e}")

line("4. 命令行工具（Git / VS Code）")
for name, cmd in [("Git", "git"), ("VS Code 命令行", "code")]:
    path = shutil.which(cmd)
    if path:
        try:
            ver = subprocess.run([cmd, "--version"], capture_output=True,
                                 text=True, timeout=20).stdout.strip().splitlines()[0]
            ok(f"{name}：{ver}")
        except Exception:
            ok(f"{name}：已安装（{path}）")
    else:
        warn(f"{name}：命令行里找不到。可能需要在 VS Code 里重启终端，或重启电脑生效")

line("5. 第三方库实测（联网装一个包试试）")
try:
    import requests
    ok(f"requests {requests.__version__} 可以正常导入")
except ImportError:
    print("  requests 还没装，正在尝试安装……")
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-q", "requests"])
    if r.returncode == 0:
        ok("安装成功！你的 pip 和网络都没问题")
    else:
        bad("安装失败，检查一下网络或镜像源配置")

line("自检完成")
print("""
  接下来你应该做：

   1. 如果上面全是 [通过] —— 恭喜，L0 的环境部分完成了
   2. 还没注册 GitHub 账号的话，去 https://github.com 用邮箱注册一个
   3. 打开 FDE学习计划/02-进度追踪.md，把 L0 的「学习项」逐条打勾
   4. 卡住了就把报错原文发给 AI，或直接问你的教练

  记住：真正的学习从明天开始，不是今天。
""")
