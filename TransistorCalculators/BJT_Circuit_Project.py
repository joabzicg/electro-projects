#Varíaveis
VCC = int(input("Digite a tensão VCC: "))
IC = int(input("Digite a corrente Ic em mA: "))
R2 = (VCC * 0.1+0.7) / (0.1 * IC * 0.001) 
R1 = (VCC/(0.1*IC*0.001))-R2
RC = (0.9*VCC-(VCC/2))/(0.001*IC)
RE = (1/4)*RC
print("O Rc é igual a:", RC, "Ω" )
print("O R1 é igual a:", R1, "Ω" )
print("O R2 é igual a:", R2, "Ω" )
print("O Re é igual a:", RE, "Ω" )
