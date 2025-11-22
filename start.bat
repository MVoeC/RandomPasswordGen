@echo off
python app.py

echo.
echo ==========================================
echo.
echo 提示: 按 Ctrl+C 可以停止服务器
echo.
echo 服务器地址: http://127.0.0.1:5000
echo 服务器地址: http://localhost:5000
echo.
echo ==========================================
echo    🚀 启动服务器...
echo ==========================================
echo.
echo ✓ 依赖已就绪

)
    )
        exit /b 1
        pause
        echo ❌ 安装失败，请手动运行: pip install -r requirements.txt
    if errorlevel 1 (
    pip install -r requirements.txt
    echo ⚠ Flask 未安装，正在安装依赖...
if errorlevel 1 (
python -c "import flask" >nul 2>&1
echo 正在检查 Flask...
echo.
echo ✓ Python 已安装

)
    exit /b 1
    pause
    echo ❌ 错误: 未检测到 Python，请先安装 Python 3.7+
if errorlevel 1 (
python --version >nul 2>&1
echo 正在检查依赖...
echo.
echo ==========================================
echo    🔐 随机密码生成器 启动程序
echo ==========================================
echo.
chcp 65001 >nul

