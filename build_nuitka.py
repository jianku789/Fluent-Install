#!/usr/bin/env python3
"""
Nuitka 打包脚本
用于将 fluent_app.py 打包成独立的 exe 可执行文件
输出名称: Fluent-Install.exe
"""

import os
import sys
import subprocess
from pathlib import Path


def build_exe():
    current_dir = Path.cwd()

    cmd = [
        sys.executable, "-m", "nuitka",
        "--standalone",                        # 独立模式，包含所有依赖
        "--onefile",                           # 打包成单个 exe
        "--windows-console-mode=disable",      # 无控制台窗口
        "--output-filename=Fluent-Install.exe",
        "--output-dir=dist",
        # 图标
        "--windows-icon-from-ico=assets/icon.ico",
        # 包含数据文件
        "--include-data-files=config.json=config.json",
        "--include-data-dir=assets=assets",
        # PyQt6 插件
        "--enable-plugin=pyqt6",
        # 显式包含模块
        "--include-module=backend",
        "--include-module=qfluentwidgets",
        "--include-module=httpx",
        "--include-module=aiofiles",
        "--include-module=ujson",
        "--include-module=colorlog",
        "--include-module=vdf",
        # 主程序
        "fluent_app.py",
    ]

    # 检查图标是否存在
    if not (current_dir / "assets" / "icon.ico").exists():
        print("警告: 图标文件不存在，跳过图标设置")
        cmd = [c for c in cmd if not c.startswith("--windows-icon-from-ico")]

    # 检查 config.json 是否存在
    if not (current_dir / "config.json").exists():
        print("警告: config.json 不存在，跳过")
        cmd = [c for c in cmd if not c.startswith("--include-data-files=config.json")]

    # 检查 assets 目录是否存在
    if not (current_dir / "assets").exists():
        print("警告: assets 目录不存在，跳过")
        cmd = [c for c in cmd if not c.startswith("--include-data-dir=assets")]

    print("开始 Nuitka 打包...")
    print(f"命令: {' '.join(cmd)}\n")

    result = subprocess.run(cmd, cwd=current_dir)

    if result.returncode == 0:
        print(f"\n打包完成！输出: {current_dir / 'dist' / 'Fluent-Install.exe'}")
        return True
    else:
        print(f"\n打包失败，返回码: {result.returncode}")
        return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
