import wordcloud

file = open('ulysses_edited.txt', 'r')
book_content = file.read()
file.close()

file2 = open('100_common_words.txt', 'r')
common_words = file2.read().lower().split()
file2.close()

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers",
                       "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am",
                       "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
                       "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each",
                       "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

common_words.extend(uninteresting_words)


def edit_content(text):
    """returns a STRING of text with no punctuation"""
    edited_content = ''
    for char in text.lower():
        if char == '\n':
            edited_content += ' '
        if char.isalpha() or char == ' ':
            edited_content += char
    return edited_content


def render_word_count(text, common):
    word = text.split()
    word_frequency = {}
    for word in word:
        if word in common:
            continue
        elif len(word) < 5:
            continue
        else:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


def get_value(value):
    return value[1]


words = render_word_count(edit_content(book_content), common_words)

cloud = wordcloud.WordCloud(height=700, width=1400, max_words=200, background_color='black')

cloud.generate_from_frequencies(words)

cloud.to_file('wordcloud.jpg')
