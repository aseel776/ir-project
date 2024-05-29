def convert_to_str(text_list: list[str]):
    combined_text = ''
    for text in text_list:
        combined_text += text
        combined_text += ' '
    return combined_text