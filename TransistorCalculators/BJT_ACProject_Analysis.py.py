#Caculadora de Análise DC de um transistor como PDT
VCC = float(input("Digite a tensão VCC em Volts: "))
R1 = float(input("Digte a resistência R1 em Ω: "))
R2 = float(input("Digte a resistência R2 em Ω: "))
RC = float(input("Digte a resistência RC em Ω: "))
RE = float(input("Digte a resistência RE em Ω: "))
b =  float(input("Digte o β do transistor: "))
ver = R1*R2/(R1+R2)
if ver <= 0.1*b*RE:
  vbb = (R2/(R1+R2))*VCC
  ve = vbb-0.7
  ie = ve/RE
  vc = VCC-RC*ie
  vce = vc-ve
  iee = 1000*ie
  ib = ie/b
  print("A tensão VBB é igual a: ", vbb, "V")
  print("A tensão VE é igual a: ", ve, "V")
  print("A tensão VC é igual a: ", vc, "V")
  print("A tensão VCE é igual a: ", vce, "V")
  print("A corrente Ic (ou Ie) é igual a: ", iee, "mA")
  print("A corrente Ib é igual a: ", ib, "mA")
else:
  vbb = (R2/(R1+R2))*VCC
  ib0 = b+1
  ib01 = ib0*RE
  ib0000 = vbb-0.7
  ib900 = ver+ib01
  ib = ib0000/ib900
  ic = ib*b
  vc = VCC-RC*ic
  ve = RE*ic
  vce = vc - ve 
  icc = ic*1000
  print("A corrente de base é igual a: ", ib, "A")
  print("A tensão VCE é igual a:", vce, "V")
  print("A corrente de coletor (ou emissor) é igual a: ", icc, "mA")
