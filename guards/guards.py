import re

if __name__ == "__main__":
    with open('chars') as f:

        data = f.read()
        result = ""
        pattern = r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"

        matches = re.finditer(pattern, data, re.MULTILINE)

        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            dupa = match.group()
            
            result = result + dupa[4]

        print(result)

