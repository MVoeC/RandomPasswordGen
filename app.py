from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)


def generate_passwords(length, count, include_chars, exclude_chars):
    """
    生成随机密码
    :param length: 密码长度
    :param count: 密码数量
    :param include_chars: 包含的字符集
    :param exclude_chars: 排除的字符
    :return: 密码列表
    """
    # 从包含字符集中排除指定字符
    char_pool = ''.join([c for c in include_chars if c not in exclude_chars])

    if not char_pool:
        raise ValueError("字符池为空，请检查字符设置")

    if length <= 0:
        raise ValueError("密码长度必须大于0")

    if count <= 0:
        raise ValueError("密码数量必须大于0")

    passwords = []
    for _ in range(count):
        password = ''.join(random.choice(char_pool) for _ in range(length))
        passwords.append(password)

    return passwords


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """生成密码API"""
    try:
        data = request.get_json()

        # 获取参数
        length = int(data.get('length', 12))
        count = int(data.get('count', 1))

        # 构建字符集
        include_chars = ''
        if data.get('lowercase', True):
            include_chars += string.ascii_lowercase
        if data.get('uppercase', True):
            include_chars += string.ascii_uppercase
        if data.get('digits', True):
            include_chars += string.digits
        if data.get('special', True):
            include_chars += string.punctuation

        # 添加自定义字符
        custom_chars = data.get('customChars', '')
        if custom_chars:
            include_chars += custom_chars

        # 获取排除字符
        exclude_chars = data.get('excludeChars', '')

        # 生成密码
        passwords = generate_passwords(length, count, include_chars, exclude_chars)

        return jsonify({
            'success': True,
            'passwords': passwords
        })

    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'生成密码时发生错误: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

