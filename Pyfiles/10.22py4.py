# 读取输入
name = input().strip()

# 将名字按空格分割成单词列表
words = name.split()

# 处理每个单词：首字母大写，其余小写
formatted_words = []
for word in words:
    formatted_word = word[0].upper() + word[1:].lower()
    formatted_words.append(formatted_word)

# 根据单词数量决定输出格式
if len(formatted_words) <= 2:
    # 1-2个单词：直接输出
    result = ' '.join(formatted_words)
else:
    # 3个及以上单词：中间名缩写
    result = formatted_words[0]  # 第一个名字
    # 处理中间名（除了第一个和最后一个）
    for i in range(1, len(formatted_words) - 1):
        result += ' ' + formatted_words
