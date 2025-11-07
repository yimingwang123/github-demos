# Calculator Demo - GitHub Copilot 演示项目

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Issues](https://img.shields.io/github/issues/yimingwang123/github-demos)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/yimingwang123/github-demos/test.yml)

这是一个用于演示 GitHub Copilot 各种功能的简单计算器项目。

## 项目目标

本项目专门设计用于演示 GitHub Copilot 的以下能力：

- **Issue 分析与修复** - 自动理解并修复代码问题
- **测试生成** - 自动生成全面的单元测试
- **代码补全** - 智能代码建议和补全
- **代码重构** - 改进代码结构和质量
- **文档生成** - 自动生成代码文档
- **MCP 集成** - 通过 MCP Server 连接 GitHub

## 项目结构

```
github-demos/
├── .github/
│   ├── workflows/           # CI/CD 自动化配置
│   └── copilot-instructions.md  # Copilot 项目准则
├── .vscode/
│   └── mcp.json            # MCP 配置（连接到 GitHub MCP server）
├── calculator.py           # 主业务代码
├── tests/
│   └── test_calculator.py  # 测试文件
├── requirements.txt        # 项目依赖
└── README.md              # 项目说明
```

## 功能

计算器提供以下基本运算：
- 加法 (`add`)
- 减法 (`subtract`)
- 乘法 (`multiply`)
- 除法 (`divide`) - **注意：当前版本存在除零错误未处理**

## 安装

```bash
pip install -r requirements.txt
```

## 运行测试

```bash
pytest tests/
```

## 已知问题

- Issue #1: `divide()` 函数未处理除以零的情况

## Copilot 演示功能

本项目可用于演示以下 Copilot 功能：

1. **代码补全** - 自动补全函数和逻辑
2. **修复 Issue** - 使用 `@github` 修复仓库中的 Issue
3. **生成单元测试** - 自动生成测试用例
4. **代码审查** - PR 自动审查和建议
5. **MCP 集成** - 通过 MCP Server 连接 GitHub

## Demo 操作示例

```
# 1. 列出当前仓库的 Issues
List open issues in yimingwang123/github-demos

# 2. 修复特定 Issue
Implement a fix for issue #1 in yimingwang123/github-demos

# 3. 创建 Pull Request
Create a pull request for the fix
```

## 项目准则

- 所有函数应包含类型注解
- 对可能抛出异常的操作需增加错误处理
- 测试文件命名需以 `test_` 开头

## License

MIT
