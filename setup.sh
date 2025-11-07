#!/bin/bash

# GitHub Copilot Demo 快速启动脚本

echo "========================================"
echo "GitHub Copilot 演示项目初始化"
echo "========================================"
echo ""

# 检查 Python
echo "检查 Python 环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装 Python 3.9+"
    exit 1
fi
echo "✅ Python 版本: $(python3 --version)"
echo ""

# 创建虚拟环境
echo "创建虚拟环境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ 虚拟环境已创建"
else
    echo "✅ 虚拟环境已存在"
fi
echo ""

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate
echo "✅ 虚拟环境已激活"
echo ""

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt
echo "✅ 依赖安装完成"
echo ""

# 运行测试
echo "运行测试..."
pytest tests/ -v
TEST_RESULT=$?
echo ""

if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ 所有测试通过"
else
    echo "⚠️  测试失败 - 这是预期的，因为 divide() 函数有已知问题"
fi
echo ""

# 检查 Node.js（MCP 需要）
echo "检查 Node.js（MCP Server 需要）..."
if command -v node &> /dev/null; then
    echo "✅ Node.js 版本: $(node --version)"
else
    echo "⚠️  Node.js 未安装，MCP Server 功能将不可用"
    echo "   请访问: https://nodejs.org/ 安装 Node.js"
fi
echo ""

# 显示下一步
echo "========================================"
echo "🎉 初始化完成！"
echo "========================================"
echo ""
echo "下一步操作："
echo "1. 在 GitHub 上创建 Issue（参考 DEMO_GUIDE.md）"
echo "2. 配置 GitHub Personal Access Token"
echo "3. 在 VS Code 中打开此项目"
echo "4. 开始演示！"
echo ""
echo "演示指南：查看 DEMO_GUIDE.md"
echo "项目说明：查看 README.md"
echo ""
