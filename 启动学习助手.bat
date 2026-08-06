@echo off
chcp 65001 >nul
echo ======================================
echo   暑期学习助手 - 启动中...
echo ======================================
echo.
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr "192.168"') do set IP=%%a
set IP=%IP: =%
echo   孩子平板浏览器打开下面这个地址：
echo.
echo   http://%IP%:8080/暑期学习助手.html
echo.
echo   学完后按 Ctrl+C 关闭
echo ======================================
cd /d D:\date\claude-workspace\get
python -m http.server 8080
pause