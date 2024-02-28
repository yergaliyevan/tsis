import re
def snakeToCamel(text):
    camel_case=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camel_case+=word.capitalize()
        else: 
            camel_case += word
        
    return camel_case
