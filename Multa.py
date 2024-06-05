Km = int(input("insira a sua velocidade em KM/H "))

if Km > 80:
   valorMult = (Km - 80) * 7
   print("Você Recebeu uma multa no valor de ", valorMult, "Reais ;-;")

else:
   print("Você não Recebeu multa") 