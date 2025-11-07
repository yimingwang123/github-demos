# 🚀 快速参考卡片

## 📦 项目文件总览

| 文件/目录 | 说明 | 必需 |
|----------|------|------|
| `calculator.py` | 主业务代码（故意有缺陷） | ✅ |
| `tests/test_calculator.py` | 单元测试 | ✅ |
| `requirements.txt` | Python 依赖 | ✅ |
| `.github/copilot-instructions.md` | Copilot 代码规范 | ✅ |
| `.vscode/mcp.json` | MCP Server 配置 | ✅ |
| `.github/workflows/test.yml` | CI/CD 配置 | ⭐ |
| `README.md` | 项目说明 | ⭐ |
| `DEMO_GUIDE.md` | 详细演示指南 | ⭐ |
| `PROJECT_SUMMARY.md` | 项目总结 | ⭐ |
| `ISSUE_TEMPLATES.md` | Issue 创建模板 | ⭐ |
| `setup.sh` | 快速启动脚本 | ⭐ |
| `example.py` | 使用示例 | ⭐ |

✅ = 必需文件  
⭐ = 推荐文件

---

## 🎯 核心演示命令

### 1️⃣ 列出 Issues
```
@github List open issues in yimingwang123/github-demos
```

### 2️⃣ 修复 Issue
```
@github Implement a fix for issue #1 in yimingwang123/github-demos
```

### 3️⃣ 生成测试
```
@workspace Generate comprehensive unit tests for calculator.py including edge cases
```

### 4️⃣ 添加类型注解
```
Add type hints to all functions in calculator.py following PEP 484
```

### 5️⃣ 生成文档
```
Add comprehensive docstrings to all functions in calculator.py using Google style
```

### 6️⃣ 创建 PR
```
@github Create a pull request for the fix to issue #1 in yimingwang123/github-demos
```

### 7️⃣ 代码审查
```
@workspace Review the changes in calculator.py and suggest improvements
```

---

## 🔧 命令行快速参考

### 初始化项目
```bash
./setup.sh
```

### 运行测试
```bash
pytest tests/ -v
```

### 运行测试（带覆盖率）
```bash
pytest tests/ --cov=. --cov-report=html
```

### 运行示例
```bash
python example.py
```

### 查看覆盖率报告
```bash
pytest tests/ --cov=. --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

---

## 📋 演示前检查清单

- [ ] ✅ 项目已推送到 GitHub
- [ ] ✅ Issue #1 已创建
- [ ] ✅ GitHub Token 已准备（权限：repo, read:user, read:project）
- [ ] ✅ VS Code 已打开项目
- [ ] ✅ 已运行 `./setup.sh`
- [ ] ✅ MCP Server 配置已测试
- [ ] ✅ 确认测试会失败（预期行为）

---

## 🎬 演示流程（30 分钟）

| 时间 | 内容 | 命令 |
|-----|------|------|
| 0-5min | 介绍项目结构 | 展示文件树 |
| 5-10min | 列出并分析 Issues | `@github List open issues...` |
| 10-20min | 自动修复 Bug | `@github Implement a fix...` |
| 20-25min | 生成测试/文档 | `@workspace Generate tests...` |
| 25-30min | 创建 PR 和总结 | `@github Create a pull request...` |

---

## 🐛 故意设计的缺陷

1. ❌ **除零错误** - `divide(10, 0)` 会抛出未处理的异常
2. ❌ **缺少类型注解** - 所有函数都没有类型提示
3. ❌ **缺少文档** - 函数没有 docstrings
4. ❌ **测试不完整** - 缺少边界条件测试

这些都是演示要修复的问题！

---

## 💡 演示技巧

### ✅ 应该做
- 让 Copilot 实时生成代码
- 展示修复前后的对比
- 强调遵循项目规范
- 展示 CI/CD 自动化
- 回答观众问题

### ❌ 不应该做
- 提前准备答案
- 跳过错误（展示真实情况）
- 忽略项目规范
- 演示太快
- 使用复杂的示例

---

## 🔗 关键文档

- **演示指南：** `DEMO_GUIDE.md`（详细步骤）
- **项目总结：** `PROJECT_SUMMARY.md`（完整说明）
- **Issue 模板：** `ISSUE_TEMPLATES.md`（创建 Issue）
- **项目说明：** `README.md`（概述）

---

## 🆘 故障排查速查

| 问题 | 解决方案 |
|-----|---------|
| MCP 连接失败 | 检查 Node.js，重新安装 MCP server |
| Token 权限不足 | 确保包含 repo, read:user, read:project |
| 测试失败 | 这是预期的！用于演示修复 |
| Copilot 不遵循规范 | 检查 `.github/copilot-instructions.md` |

---

## 📞 资源链接

- **GitHub Copilot 文档：** https://docs.github.com/copilot
- **MCP 协议：** https://modelcontextprotocol.io/
- **pytest 文档：** https://docs.pytest.org/
- **PEP 484 (Type Hints)：** https://peps.python.org/pep-0484/

---

**打印此卡片，演示时随身携带！** 📄
