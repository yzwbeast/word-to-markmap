import json

# 读取 JSON 文件
def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# 生成 Markmap 格式的内容
def json_to_markmap(data):
    markmap_content = """---
title: Word Queries
markmap:
  colorFreezeLevel: 2
  maxWidth: 300
  initialExpandLevel: 2
---\n\n"""

    markmap_content += "# Word Queries\n\n"

    for date, word_list in data.items():
        markmap_content += f"## {date}\n"

        for word_info in word_list:
            word = word_info['word']
            markmap_content += f"### {word}\n"

            # 添加 Definitions
            markmap_content += f"- **Definitions**:\n"
            for definition in word_info['definitions']:
                definition_text = definition.get('text', '')
                part_of_speech = definition.get('partOfSpeech', '')
                markmap_content += f"  - {part_of_speech}: {definition_text}\n"

            # 添加 Synonyms
            if word_info.get('synonyms'):
                markmap_content += f"- **Synonyms**: {', '.join(word_info['synonyms'])}\n"

            # 添加 Antonyms
            if word_info.get('antonyms'):
                markmap_content += f"- **Antonyms**: {', '.join(word_info['antonyms'])}\n"

            # 添加 Examples
            if word_info.get('examples'):
                markmap_content += f"- **Examples**:\n"
                for example in word_info['examples']:
                    markmap_content += f"  - {example}\n"

            markmap_content += "\n"

    return markmap_content

# 将 Markmap 内容保存到文件
def save_markmap_to_file(markmap_content, filename='word_queries.markmap.md'):
    with open(filename, 'w') as file:
        file.write(markmap_content)

# 主函数
def convert_json_to_markmap(json_filename, markmap_filename='word_queries.markmap.md'):
    data = read_json(json_filename)
    markmap_content = json_to_markmap(data)
    save_markmap_to_file(markmap_content, markmap_filename)
    print(f"Markmap file saved to {markmap_filename}")

# 测试
if __name__ == "__main__":
    json_filename = 'word_queries.json'  # 输入你的 JSON 文件名
    convert_json_to_markmap(json_filename)
