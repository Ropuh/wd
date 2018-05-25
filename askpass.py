while True:
    print('Kim jesteś?')
    name = input()
    if name != 'Robert':
        continue
    print('Witaj, Robert. Podaj hasło?')
    password = input()
    if password == 'password':
        break
print('Access granted.')