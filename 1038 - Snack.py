X = int(input()) #código
Y = int(input()) #quantidade

if X > 5:
    print("código inválido, tente novamente")
    
elif X == 1:
    R1 = 4.00 * Y
    print("Total: R$", format(R1, '.2f'))
    
elif X == 2:
    R2 = 4.50 * Y
    print("Total: R$", format(R2, '.2f'))

elif X == 3:
    R3 = 5.00 * Y
    print("Total: R$", format(R3, '.2f'))
    
elif X == 4:
    R4 = 2.00 * Y
    print("Total: R$", format(R4, '.2f'))

elif X == 5:
    R5 = 1.50 * Y
    print("Total: R$", format(R5, '.2f'))
    