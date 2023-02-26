x = int(input(" Para calcular impedância de entrada digite 1 \n Para calcular Zo digite 2 \n Para calcular ganho digite 3 \n Para calcular Capacitor de entrada digite 4 \n Para calcular Cout digite 5 \n Para calcular Cdesvio digite 6 \n "))
if x == 1:
    R1 = int(input("Digite o valor do R1 em Ω: "))
    R2 = int(input("Digite o valor do R2 em Ω: "))
    b = int(input("Digite o valor do β do transistor: "))
    IE = float(input("Digite o valor da corrente IE em mA: "))
    zi = ((R1*R2/(R1+R2))*((0.025/(IE*0.001))*b))/(((R1*R2)/(R1+R2))+((0.025/(IE*0.001))*b))
    print("A impedância de entrada é igual a: ", format(zi,'.2f'), "Ω")
elif x == 2:
    RC = int(input("Digite o valor do RC em Ω: "))
    q = str(input("O circuito possui RL ? (s/n)"))
    if q == "s":
        RL = int(input("Digite o valor do RL em Ω: "))
        zo = (RC*RL)/(RC+RL)
        print("A impedância de saída é igual a: ", format(zo,'.2f'), "Ω")
    else:
        zo = RC
        print("A impedância de saída é igual a: ", format(zo,'.2f'), "Ω")
elif x == 3:
    RC = int(input("Digite o valor do RC em Ω: "))
    RL = str(input("O circuito possui RL ? (s/n)"))
    if RL == "s":
        RL = int(input("Digite o valor do RL em Ω: "))
        IE = float(input("Digite o valor da corrente IE em mA: "))
        av = ((RC*RL)/(RC+RL))/(0.025/(IE*0.001))
        print("O ganho é igual a: ", format(av,'.2f'))
    else:
        IE = float(input("Digite o valor da corrente IE em mA: "))
        av = (RC)/(0.025/(IE*0.001))
        print("O ganho é igual a: ", format(av,'.2f'))
elif x == 4:
    R1 = int(input("Digite o valor do R1 em Ω: "))
    R2 = int(input("Digite o valor do R2 em Ω: "))
    b = int(input("Digite o valor do β do transistor: "))
    IE = float(input("Digite o valor da corrente IE em mA: "))
    f = int(input("Digite a frequência em Hz: "))
    zi = ((R1*R2/(R1+R2))*((0.025/(IE*0.001))*b))/(((R1*R2)/(R1+R2))+((0.025/(IE*0.001))*b))
    ci = 1/(0.1*zi*f*2*3.14)
    print("O valor do capacitor de entrada é igual a: ", ci, "F")
elif x == 5:
    RC = int(input("Digite o valor do RC em Ω: "))
    RL = str(input("O circuito possui RL? (s/n):"))
    if RL == "s":
        RL = int(input("Digite o valor do RL em Ω: "))
        f = int(input("Digite a frequência em Hz: "))
        co = 1/(0.1*(RC+RL)*f*2*3.14)
        print("O valor do capacitor de saída é igual a: ", co, "F")
    else:
        f = int(input("Digite a frequência em Hz: "))
        co = 1/(0.1*(RC)*f*2*3.14)
        print("O valor do capacitor de saída é igual a: ", co, "F")
elif x == 6:
    R1 = int(input("Digite o valor do R1 em Ω: "))
    R2 = int(input("Digite o valor do R2 em Ω: "))
    b = int(input("Digite o valor do β do transistor: "))
    f = int(input("Digite a frequência em Hz: "))
    IE = float(input("Digite o valor da corrente IE em mA: "))
    re = 0.025/(0.001*IE)
    cd = 1/(0.1*(re+((R1*R2/(R1+R2))/b))*2*3.14*f)
    print("O valor do capacitor de desvio é igual a: ", cd, "F")
else:
    print("Opção errônea")
