def create_dict_once():
    alphabet = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    bet = "yzabcdefghijklmnopqrstuvwx"
    i = 0
    for letter in alpha:
        alphabet[letter] = bet[i]
        i = i + 1
    return alphabet

def create_dict_twice():
    alphabet = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    bet = "efghijklmnopqrstuvwxyzabcd"
    i = 0
    for letter in alpha:
        alphabet[letter] = bet[i]
        i = i + 1
    return alphabet


if __name__ == "__main__":

    sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(sentence)
    alphabet = create_dict_once()
    second_alphabet = create_dict_twice()
    new_sentence = ""

    for letter in sentence:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            new_sentence = new_sentence + alphabet[letter]
        else:
            new_sentence = new_sentence + letter
    print(new_sentence)
    result = ""

    for letter in new_sentence:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            result = result + second_alphabet[letter]
        else:
            result = result + letter
    print(result)
    map = "map"
    translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "yzabcdefghijklmnopqrstuvwx")
    new_map = map.translate(translation_table)
    another_translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd")
    result_map = new_map.translate(another_translation_table)
    print(result_map)