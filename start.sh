#!/bin/bash

echo ""
echo "=========================================="
echo "   🔐 随机密码生成器 启动程序"
echo "=========================================="
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未检测到 Python，请先安装 Python 3.7+"
    exit 1
fi

echo "✓ Python 已安装"
echo ""

# 检查并安装依赖
if ! python3 -c "import flask" &> /dev/null; then
    echo "⚠ Flask 未安装，正在安装依赖..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ 安装失败，请手动运行: pip3 install -r requirements.txt"
        exit 1
    fi
fi

echo "✓ 依赖已就绪"
echo ""
echo "=========================================="
echo "   🚀 启动服务器..."
echo "=========================================="
echo ""
echo "服务器地址: http://localhost:5000"
echo "服务器地址: http://127.0.0.1:5000"
echo ""
echo "提示: 按 Ctrl+C 可以停止服务器"
echo ""
echo "=========================================="
echo ""

python3 app.py

