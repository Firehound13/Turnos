turno = input("Em que turno você estuda?Digite 'M' para matutino, 'V' para Vespertino ou 'N' para noturno")

if turno == 'M':
    print("Bom dia")
elif turno == 'V':
        print("Boa Tarde")
elif turno == 'N':
        print("Boa Noite")
else:
        print("Argumento inválido.")