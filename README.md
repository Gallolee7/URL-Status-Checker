# URL Status Checker

一个轻量级的Python工具，用于批量检查URL的可访问性和状态码。

## 功能特点
- 批量检查URL状态
- 支持超时设置
- 并发检查提高效率
- 简单的命令行界面
- 详细的检查报告

## 安装
bash
pip install -r requirements.txt

## 使用方法
python
from src.url_checker import URLChecker
checker = URLChecker(timeout=5)
results = checker.check_urls(['https://github.com
', 'https://google.com
'])
print(results)

## 命令行使用

bash
python src/checker_cli.py --file urls.txt

## 许可证
MIT License
