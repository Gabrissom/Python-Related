A, B, C = map(float, input().split())

delta = B ** 2 - (4 * A * C) #delta

if A <= 0 or delta == 0:
    print("Impossivel calcular")
    
else:
    R2 = (- B - delta ** (1/2)) / (2 * A)
    R1 = (- B + delta ** (1/2)) / (2 * A)
    
    RUm = format(R1, '.5f')
    RDois = format(R2, '.5f')
    
    print("R1 =", RUm)
    print("R2 =", RDois)