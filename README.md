# URL Status Checker

一个轻量级的 Python 工具，用于批量检查 URL 的可访问性和 HTTP 状态码。

## 功能特点
- 批量检查 URL 状态
- 支持超时设置
- 并发检查提高效率
- 简单的命令行界面
- 详细的检查报告

## 安装
```bash
pip install -r requirements.txt
```

## 使用（作为库）
```python
from src.url_checker import URLChecker

checker = URLChecker(timeout=5)
results = checker.check_urls(['https://github.com', 'https://google.com'])
print(results)
```

要在文件中列出要检查的 URL（每行一个），例如 urls.txt：
```
https://github.com
https://httpbin.org/status/200
https://httpbin.org/status/404
```

## 命令行使用
推荐使用模块方式运行，以确保相对导入工作：

```bash
# 从仓库根目录运行（推荐）
python -m src.checker_cli --file urls.txt

# 或者直接运行脚本（也应正常工作，因为已增加兼容导入）
python src/checker_cli.py --file urls.txt

# 检查单个 URL 并以 JSON 输出
python -m src.checker_cli --url https://httpbin.org/status/200 -t 5 -o json
```

## 测试
仓库中包含单元测试，单元测试已将网络调用模拟（mock）以保证稳定性和速度：

```bash
python -m unittest discover
```

## 许可证
MIT License
