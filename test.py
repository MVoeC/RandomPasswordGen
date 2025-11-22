"""
测试脚本 - 用于测试密码生成功能
"""
from app import generate_passwords
import string

def test_basic_generation():
    """测试基本密码生成"""
    print("=" * 50)
    print("测试1: 基本密码生成")
    print("=" * 50)

    passwords = generate_passwords(
        length=16,
        count=5,
        include_chars=string.ascii_letters + string.digits + string.punctuation,
        exclude_chars=""
    )

    print(f"生成 {len(passwords)} 个密码:")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd} (长度: {len(pwd)})")
    print()


def test_exclude_chars():
    """测试排除字符功能"""
    print("=" * 50)
    print("测试2: 排除易混淆字符 (0Oo1Il)")
    print("=" * 50)

    exclude = "0Oo1Il"
    passwords = generate_passwords(
        length=20,
        count=3,
        include_chars=string.ascii_letters + string.digits,
        exclude_chars=exclude
    )

    print(f"生成 {len(passwords)} 个密码 (不包含: {exclude}):")
    for i, pwd in enumerate(passwords, 1):
        # 验证是否真的排除了指定字符
        has_excluded = any(c in pwd for c in exclude)
        status = "❌ 包含排除字符" if has_excluded else "✓ 正确"
        print(f"{i}. {pwd} {status}")
    print()


def test_custom_length():
    """测试不同长度"""
    print("=" * 50)
    print("测试3: 不同长度的密码")
    print("=" * 50)

    lengths = [8, 12, 16, 24, 32]
    for length in lengths:
        pwd = generate_passwords(
            length=length,
            count=1,
            include_chars=string.ascii_letters + string.digits + string.punctuation,
            exclude_chars=""
        )[0]
        print(f"长度 {length:2d}: {pwd}")
    print()


def test_different_char_types():
    """测试不同字符类型"""
    print("=" * 50)
    print("测试4: 不同字符类型组合")
    print("=" * 50)

    test_cases = [
        ("仅小写字母", string.ascii_lowercase),
        ("仅大写字母", string.ascii_uppercase),
        ("仅数字", string.digits),
        ("仅特殊字符", string.punctuation),
        ("字母+数字", string.ascii_letters + string.digits),
        ("全部字符", string.ascii_letters + string.digits + string.punctuation),
    ]

    for name, chars in test_cases:
        pwd = generate_passwords(
            length=16,
            count=1,
            include_chars=chars,
            exclude_chars=""
        )[0]
        print(f"{name:12s}: {pwd}")
    print()


def test_error_handling():
    """测试错误处理"""
    print("=" * 50)
    print("测试5: 错误处理")
    print("=" * 50)

    # 测试空字符池
    try:
        generate_passwords(12, 1, "abc", "abc")
        print("❌ 空字符池测试失败 - 应该抛出异常")
    except ValueError as e:
        print(f"✓ 空字符池测试通过: {e}")

    # 测试无效长度
    try:
        generate_passwords(0, 1, "abc", "")
        print("❌ 无效长度测试失败 - 应该抛出异常")
    except ValueError as e:
        print(f"✓ 无效长度测试通过: {e}")

    # 测试无效数量
    try:
        generate_passwords(12, 0, "abc", "")
        print("❌ 无效数量测试失败 - 应该抛出异常")
    except ValueError as e:
        print(f"✓ 无效数量测试通过: {e}")

    print()


if __name__ == "__main__":
    print("\n🔐 随机密码生成器 - 功能测试\n")

    test_basic_generation()
    test_exclude_chars()
    test_custom_length()
    test_different_char_types()
    test_error_handling()

    print("=" * 50)
    print("所有测试完成！")
    print("=" * 50)
    print("\n提示: 运行 'python app.py' 启动 Web 服务器")
    print("然后访问 http://localhost:5000 使用图形界面\n")

