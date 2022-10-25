import halflang

while True:
    text = input("Halflang > ")
    if (text.lower() == 'exit'): exit()
    result, error = halflang.run(text)

    if error: print(error.to_string())
    else: print(result)
    