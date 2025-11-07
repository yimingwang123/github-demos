# 演示用 Issue 内容模板

将以下内容复制到 GitHub Issue 中创建演示用的 Issue。

---

## Issue 1: Division by Zero Error

**Title:** Division by zero error in `divide()` function

**Labels:** bug, good first issue

**Body:**

```markdown
## 问题描述
当调用 `divide(10, 0)` 时，程序会抛出 `ZeroDivisionError` 异常，导致程序崩溃。

## 重现步骤
1. 导入 calculator 模块
2. 调用 `divide(10, 0)`
3. 观察到未处理的 `ZeroDivisionError` 异常

```python
from calculator import divide

# 这会导致程序崩溃
result = divide(10, 0)
```

## 期望行为
函数应该妥善处理除以零的情况，可以：
- 返回 `None` 或特殊值
- 抛出自定义的、有意义的异常
- 记录警告日志

## 实际行为
程序直接抛出 `ZeroDivisionError` 异常并崩溃。

## 建议修复
1. 在 `divide()` 函数中添加除零检查
2. 抛出有意义的自定义异常，例如 `ValueError("除数不能为零")`
3. 添加相应的单元测试来验证边界条件
4. 添加函数文档说明可能抛出的异常

## 环境信息
- Python 版本: 3.9+
- 操作系统: Linux/macOS/Windows

## 优先级
中等 - 这是一个常见的边界条件问题，应该被妥善处理。
```

---

## Issue 2: Missing Type Hints

**Title:** Add type hints to all functions

**Labels:** enhancement, documentation

**Body:**

```markdown
## 功能描述
当前所有函数都缺少类型注解（type hints），这降低了代码的可读性和 IDE 支持。

## 建议改进
为所有函数添加类型注解，遵循 PEP 484 标准。

## 示例

当前代码：
```python
def add(a, b):
    return a + b
```

期望代码：
```python
def add(a: float, b: float) -> float:
    """
    计算两个数的和
    
    Args:
        a: 第一个加数
        b: 第二个加数
    
    Returns:
        两数之和
    """
    return a + b
```

## 优先级
低 - 代码改进，不影响功能但能提高代码质量。
```

---

## Issue 3: Insufficient Test Coverage

**Title:** Improve test coverage for edge cases

**Labels:** testing, enhancement

**Body:**

```markdown
## 问题描述
当前的测试覆盖不够全面，缺少对边界条件和异常情况的测试。

## 缺失的测试用例

1. **除法函数**
   - 除以零的测试
   - 负数除法测试
   - 浮点数精度测试

2. **所有函数**
   - 大数测试
   - 负数测试
   - 零值测试
   - 浮点数测试

3. **异常处理**
   - 验证异常类型
   - 验证异常消息

## 建议
使用 pytest 的参数化测试 (`@pytest.mark.parametrize`) 来覆盖多个测试场景。

## 目标
- 代码覆盖率达到 90% 以上
- 所有边界条件都有对应的测试
```

---

## 使用说明

1. **创建 Issue**
   - 登录 GitHub
   - 进入 `yimingwang123/github-demos` 仓库
   - 点击 "Issues" 标签
   - 点击 "New issue"
   - 复制上述内容

2. **演示顺序**
   - 先创建 Issue 1（必需，用于主演示）
   - 可选创建 Issue 2 和 3（用于展示更多功能）

3. **记录 Issue 编号**
   - 创建后记录 Issue 编号（如 #1, #2, #3）
   - 在演示时使用这些编号

4. **Copilot 演示命令**
   ```
   @github List open issues in yimingwang123/github-demos
   @github Implement a fix for issue #1 in yimingwang123/github-demos
   @github Create a pull request for issue #1
   ```
