# GitHub Copilot 演示指南

## 准备工作

### 1. 在 GitHub 上创建 Issue

在仓库中创建一个 Issue 用于演示修复功能：

**Issue Title:** Division by zero error in `divide()` function

**Issue Body:**
```
## 问题描述
当调用 `divide(10, 0)` 时，程序会抛出 `ZeroDivisionError` 异常。

## 期望行为
- 应该妥善处理除以零的情况
- 可以返回 `None` 或抛出自定义异常，并附带清晰的错误消息

## 重现步骤
1. 运行 `python calculator.py`
2. 调用 `divide(10, 0)`
3. 观察到 `ZeroDivisionError` 异常

## 建议修复
- 添加除零检查
- 抛出有意义的异常或返回特殊值
- 添加相应的单元测试
```

记录下 Issue 编号（例如 #1）。

### 2. 配置 MCP Server

确保 `.vscode/mcp.json` 已正确配置，并准备好 GitHub Personal Access Token。

所需权限：
- `repo`（完整仓库权限）
- `read:user`（读取用户信息）
- `read:project`（读取项目信息）

## 演示流程

### Demo 1: 列出仓库 Issues

在 Copilot Chat 中输入：

```
@github List open issues in yimingwang123/github-demos
```

**预期结果：** 显示仓库中所有开放的 Issues 列表，包括你刚创建的除零错误 Issue。

---

### Demo 2: 分析并修复 Issue

```
@github Analyze issue #1 in yimingwang123/github-demos and suggest a fix
```

或直接：

```
@github Implement a fix for issue #1 in yimingwang123/github-demos
```

**预期结果：** 
- Copilot 会分析 Issue 内容
- 提供修复建议
- 自动修改 `calculator.py` 文件，添加除零检查
- 可能会更新或建议更新测试文件

---

### Demo 3: 生成单元测试

```
@workspace Generate comprehensive unit tests for calculator.py, including edge cases
```

**预期结果：**
- 补充缺失的测试用例
- 添加边界条件测试（如除零测试）
- 添加负数、零等特殊情况测试

---

### Demo 4: 修复类型注解

由于我们的代码故意缺少类型注解，可以让 Copilot 修复：

```
Add type hints to all functions in calculator.py following PEP 484
```

**预期结果：**
- 所有函数参数和返回值都添加类型注解
- 遵循项目的 `.github/copilot-instructions.md` 中的规范

---

### Demo 5: 创建 Pull Request

修复完成后：

```
@github Create a pull request for the fix to issue #1 in yimingwang123/github-demos
```

**预期结果：**
- 自动创建 PR
- 生成有意义的 commit message
- PR 描述包含修复的详细说明
- 关联到原始 Issue

---

### Demo 6: 代码审查

```
@workspace Review the changes in calculator.py and suggest improvements
```

**预期结果：**
- 提供代码质量建议
- 检查是否遵循最佳实践
- 建议额外的改进（如添加 docstrings）

---

### Demo 7: 生成文档

```
Add comprehensive docstrings to all functions in calculator.py using Google style
```

**预期结果：**
- 每个函数添加详细的 docstring
- 包含参数说明、返回值说明、异常说明
- 使用示例

---

## 高级演示

### 演示 8: 使用自定义 Prompt

创建 `.github/prompts/fix-template.md`：

```markdown
# Issue 修复模板

修复 Issue 时，请遵循以下步骤：

1. 分析问题的根本原因
2. 提供修复方案
3. 添加必要的错误处理
4. 更新或创建相关单元测试
5. 确保代码符合项目规范
6. 添加或更新文档注释
```

然后使用：

```
@workspace Using the template in .github/prompts/fix-template.md, fix the division function
```

---

### 演示 9: 批量重构

```
@workspace Refactor all functions in calculator.py to follow these requirements:
1. Add type hints
2. Add docstrings
3. Add error handling
4. Follow PEP 8
```

---

### 演示 10: CI/CD 集成

提交代码后，GitHub Actions 会自动运行测试：

```bash
git add .
git commit -m "Fix division by zero error (fixes #1)"
git push origin main
```

在 GitHub 上查看 Actions 标签页，展示自动化测试的运行情况。

---

## 演示技巧

1. **准备工作**
   - 提前创建好 Issue
   - 确保 MCP 配置正确
   - 准备好 GitHub Token

2. **演示顺序**
   - 从简单到复杂
   - 先展示 Issue 列表
   - 再展示修复功能
   - 最后展示高级功能

3. **互动性**
   - 让观众提出要修复的问题
   - 实时演示 Copilot 的建议
   - 对比修复前后的代码

4. **强调重点**
   - 项目准则的作用（`.github/copilot-instructions.md`）
   - MCP Server 的集成能力
   - 自动化测试的重要性

5. **常见问题准备**
   - Token 权限问题
   - MCP 连接问题
   - 如何自定义 Copilot 行为

---

## 故障排查

### MCP 连接失败

```bash
# 检查 Node.js 是否安装
node --version

# 检查 npx 是否可用
npx --version

# 手动安装 MCP server
npm install -g @modelcontextprotocol/server-github
```

### Token 权限不足

确保 Token 包含以下权限：
- `repo`
- `read:user`
- `read:project`
- `workflow`（如果需要操作 Actions）

### 测试失败

```bash
# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest tests/ -v

# 查看覆盖率
pytest tests/ --cov=. --cov-report=html
```

---

## 后续步骤

演示完成后，可以：

1. 展示 GitHub 上的 PR 和 Issue 关联
2. 查看 CI/CD 运行结果
3. 讨论如何在实际项目中应用
4. 回答观众问题

---

## 资源链接

- [GitHub Copilot 文档](https://docs.github.com/en/copilot)
- [MCP 协议文档](https://modelcontextprotocol.io/)
- [GitHub CLI 文档](https://cli.github.com/)
- [pytest 文档](https://docs.pytest.org/)
