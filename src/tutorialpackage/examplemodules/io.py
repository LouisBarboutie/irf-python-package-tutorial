def binarywrite(path: str, line: str):
    with open(path, 'wb') as file:
        content = line.encode(encoding='utf-8', errors='strict')
        file.write(content)

def binaryread(path: str) -> str:
    with open(path, 'rb') as file:
        content = file.read()
        text = content.decode(encoding='utf-8', errors='strict')
        return text