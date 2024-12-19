import requests
import json
from datetime import datetime

# 输入你的 Wordnik API 密钥
API_KEY = 'your_api_key_here'

# Wordnik API URL
BASE_URL = "https://api.wordnik.com/v4"
# API_URL = "https://api.wordnik.com/v4/word.json"
# API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"(free)

# 查询单词的函数
def get_word_info(word):
    url = f"{BASE_URL}/word.json/{word}/definitions?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        definitions = response.json()
    else:
        print(f"Error fetching definitions for {word}")
        return None

    # 获取同义词和反义词
    synonyms_url = f"{BASE_URL}/word.json/{word}/relatedWords?api_key={API_KEY}&relationshipTypes=synonym,antonym"
    synonyms_response = requests.get(synonyms_url)

    if synonyms_response.status_code == 200:
        related_words = synonyms_response.json()
        synonyms = []
        antonyms = []
        for item in related_words:
            if item['relationshipType'] == 'synonym':
                synonyms.extend(item['words'])
            elif item['relationshipType'] == 'antonym':
                antonyms.extend(item['words'])
    else:
        print(f"Error fetching synonyms/antonyms for {word}")
        return None

    # 获取示例句子
    example_url = f"{BASE_URL}/word.json/{word}/examples?api_key={API_KEY}"
    example_response = requests.get(example_url)

    if example_response.status_code == 200:
        examples = example_response.json().get('examples', [])
    else:
        print(f"Error fetching examples for {word}")
        return None

    # 获取当前日期
    date = datetime.now().strftime('%Y-%m-%d')

    # 构造查询结果
    word_info = {
        'word': word,
        'definitions': definitions,
        'synonyms': synonyms,
        'antonyms': antonyms,
        'examples': [example['text'] for example in examples]
    }

    return date, word_info

# 将结果按日期保存到本地 json 文件
def save_to_json(date, data, filename='word_queries.json'):
    try:
        with open(filename, 'r') as f:
            all_data = json.load(f)
    except FileNotFoundError:
        all_data = {}

    # 如果该日期还没有记录过，初始化日期
    if date not in all_data:
        all_data[date] = []

    all_data[date].append(data)

    with open(filename, 'w') as f:
        json.dump(all_data, f, indent=4)

# 查询单词并保存
def query_and_save(word):
    date, word_info = get_word_info(word)
    if word_info:
        save_to_json(date, word_info)
        print(f"Word info for '{word}' saved successfully on {date}!")
    else:
        print(f"Failed to get information for '{word}'.")

# 测试查询功能
if __name__ == '__main__':
    word_to_query = input("Enter the word to search: ")
    query_and_save(word_to_query)
