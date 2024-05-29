from nltk.tokenize import word_tokenize

def convert_to_str(text_list: list[str]):
    combined_text = ''
    for text in text_list:
        combined_text += text
        combined_text += ' '
    return combined_text

def list2word_tokenizer(text_list: list[str]):
    text = convert_to_str(text_list)
    return word_tokenize(text)