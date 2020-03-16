def order(sentence):
    sent_list = sentence.split()
    final_list = [None for i in range(0, len(sent_list))]
    for id, word in enumerate(sent_list):
        num = None
        for char in word:
            if char.isdigit():
                num = int(char) - 1
                final_list[num] = word
    final_list = " ".join(final_list)

    return final_list
