import re
import zipfile

if __name__ == '__main__':

    pattern = re.compile("Next nothing is (\d+)")
    """
    with open('channel\\readme.txt') as readme:
        whattodo = readme.read()
        print(whattodo)
    """
    num = '90052'

    result = []

    zf = zipfile.ZipFile('channel.zip')

    while True:
        data = zf.read(num + '.txt').decode('utf-8')
        result.append(zf.getinfo(num + '.txt').comment.decode('utf-8'))
        print(data)
        match = pattern.search(data)
        if match is None:
            break
        num = match.group(1)

    print("".join(result))

