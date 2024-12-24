
# 单词导图

[English README available here](README.md)

这个项目是一个**Python工具**，旨在帮助您通过Wordnik API查询单词的定义、同义词、反义词和例句。查询结果将保存在本地的JSON文件中，按日期分类存储。此外，工具还可以将保存的JSON数据转换为**Markmap**格式的Markdown文件，使您能够以交互式思维导图的形式可视化您的单词学习进度。

## 功能
- **Wordnik API 查询**：通过Wordnik API获取单词的定义、同义词、反义词和例句。
- **每日进度记录**：将查询结果保存在本地JSON文件中，并按日期分类。
- **Markmap转换**：将存储的JSON数据转换为Markmap友好的Markdown格式。
- **可视化**：使用Markmap工具查看单词数据的交互式思维导图。

## 获取 Wordnik API 密钥
要获取 Wordnik API 密钥，你需要注册一个 Wordnik 开发者账户并创建 API 密钥。以下是详细步骤：

1. 访问 [Wordnik 开发者网站](https://developer.wordnik.com)
2. 注册或登录账户
3. 创建 API 密钥
	- 点击 My Account 或导航栏中的 API Key。
	- 选择 Create an API Key 或类似选项。
	- 填写 API 密钥的相关信息：
	    - Name: 为你的 API 密钥命名（例如：My Python App）。
	    - Description: 简要描述密钥的用途（例如：Word lookup for my app）。
	    - API Access Level: 通常可以选择默认权限。
	- 点击 Submit 或 Create Key。

4. 查看和保存 API 密钥
    - 生成后，页面会显示你的 API Key。
	- 重要：妥善保存这个密钥！你可以复制并粘贴到安全的地方（例如：密码管理器或代码中的环境变量）。

5. 使用 API 密钥
    ```bash
    # 输入你的 Wordnik API 密钥
    API_KEY = 'your_api_key_here'
    ```

## 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/yzwbeast/word-to-markmap.git
   ```
2. 进入项目目录：
   ```bash
   cd word-to-markmap
   ```
<details>
<summary>为什么推荐使用虚拟环境</summary>

>当你遇到 “**externally-managed-environment**” 错误时，可能是操作系统 使用 APT 安装的 Python 版本对系统环境进行了严格管理，防止用户通过 pip 修改系统级的 Python 包。<br />
>要解决这个问题，**推荐方法**：<br />使用虚拟环境是最干净、安全的方法。它不会影响系统的 Python 环境，同时方便你自由管理依赖。
</details>

3. 创建虚拟环境<br />在项目目录下运行：
   ```bash
   python3 -m venv map
   ```
   - `map` 是虚拟环境的名称，可以替换为任意名字。
4. 激活虚拟环境：
   ```bash
   source map/bin/activate
   ```
5. 安装依赖：
   ```bash
   pip install requests
   ```
6. 运行单词查询脚本：
   ```bash
   python word_query.py
   ```

## 使用方法
1.	运行 `word_query.py` 脚本，从Wordnik API查询一个单词，并将结果保存到JSON文件中。
2.	使用 `json_to_markmap.py` 脚本将保存的JSON数据转换为Markmap Markdown格式。
3.	在Markmap工具中查看生成的Markdown文件，以可视化您的单词学习进度。

## 文件结构
- `word_query.py`：用于查询单词并将结果保存到JSON文件的主脚本。
- `json_to_markmap.py`：用于将保存的JSON文件转换为Markmap格式的脚本。
- `word_queries.json`：存储按日期分类的查询单词数据的JSON文件（由`word_query.py`生成）。

## 示例
对于查询的单词，生成的Markmap Markdown输出可能如下所示：
```bash
---
title: Word Queries
markmap:
  colorFreezeLevel: 2
  maxWidth: 300
  initialExpandLevel: 2
---

# Word Queries

## 2024-12-19
### example
- **Definitions**:
  - noun: A representative form or pattern.
- **Synonyms**: model, exemplar
- **Antonyms**: counterexample
- **Examples**:
  - This is an example sentence.
```
将生成的Markdown文件导入Markmap中，可以看到单词及其数据的可视化表示。

## 许可证
本项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

[English README available here](README.md)
