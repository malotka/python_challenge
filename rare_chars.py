from collections import Counter

if __name__ == "__main__":
    with open('chars.txt') as file:
        data = file.read()
        a = Counter(data)
        b = a.most_common()
        """<equality>""""