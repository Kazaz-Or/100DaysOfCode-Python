from data import morse_code_rules

ans = input('Morse Code Converter\nType text to convert to Morse Code!\n')
output_list = []


def text_to_morse():
    for letter in ans:
        letter = letter.lower()
        output_list.append(morse_code_rules[letter])
    # print(output_list)


text_to_morse()

result = ' '.join(output_list)
print(f'The Morse Code of {ans} is {result}')