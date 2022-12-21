while True:
    try:
        print(f'{input()}')
    except:
        EOFError
        break