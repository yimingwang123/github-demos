#!/usr/bin/env python3
"""
Calculator 示例使用脚本

此脚本演示 calculator.py 中各个函数的使用，
包括正常情况和会触发错误的情况。
"""

from calculator import add, subtract, multiply, divide


def main():
    print("=" * 50)
    print("Calculator 功能演示")
    print("=" * 50)
    print()
    
    # 加法示例
    print("1. 加法运算")
    result = add(10, 5)
    print(f"   add(10, 5) = {result}")
    print()
    
    # 减法示例
    print("2. 减法运算")
    result = subtract(10, 5)
    print(f"   subtract(10, 5) = {result}")
    print()
    
    # 乘法示例
    print("3. 乘法运算")
    result = multiply(10, 5)
    print(f"   multiply(10, 5) = {result}")
    print()
    
    # 除法示例 - 正常情况
    print("4. 除法运算（正常）")
    result = divide(10, 5)
    print(f"   divide(10, 5) = {result}")
    print()
    
    # 除法示例 - 除以零（会导致错误）
    print("5. 除法运算（除以零）- 这会导致错误！")
    print("   尝试执行: divide(10, 0)")
    try:
        result = divide(10, 0)
        print(f"   结果: {result}")
    except ZeroDivisionError as e:
        print(f"   ❌ 错误: {type(e).__name__}: {e}")
        print("   这就是 Issue #1 要修复的问题！")
    print()
    
    print("=" * 50)
    print("演示完成")
    print("=" * 50)
    print()
    print("注意事项：")
    print("- divide() 函数在除以零时会抛出未处理的异常")
    print("- 这是故意设计的缺陷，用于演示 Copilot 的修复能力")
    print("- 运行测试查看更多细节: pytest tests/ -v")


if __name__ == "__main__":
    main()
