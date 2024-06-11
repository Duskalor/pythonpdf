def signo(dia,mes):
    if (dia>=20 and mes==1) or (dia<=18 and mes==2):
        return "Acuario"
    elif (dia>=19 and mes==2) or (dia<=20 and mes==3):
        return "Piscis"
    elif (dia>=21 and mes==3) or (dia<=19 and mes==4):
        return "Aries"
    elif (dia>=20 and mes==4) or (dia<=20 and mes==5):
        return "Tauro"
    elif (dia>=21 and mes==5) or (dia<=20 and mes==6):
        return "Géminis"
    elif (dia>=21 and mes==6) or (dia<=22 and mes==7):
        return "Cáncer"
    elif (dia>=23 and mes==7) or (dia<=22 and mes==8):
        return "Leo"
    elif (dia>=23 and mes==8) or (dia<=22 and mes==9):
        return "Virgo"
    elif (dia>=23 and mes==9) or (dia<=22 and mes==10):
        return "Libra"
    elif (dia>=23 and mes==10) or (dia<=21 and mes==11):
        return "Escorpio"
    elif (dia>=22 and mes==11) or (dia<=21 and mes==12):
        return "Sagitario"
    else:
        return "Capricornio"
ultimo_dia=[31,29,31,30,31,30,31,31,30,31,30,31]


while True:
    while True : 
      try :
        dia=int(input("Inserte día: "))
      except ValueError:
        print("Error: ingrese el dia correctamente")
        continue
      break
    while True : 
      try :
        mes=int(input("Inserte mes: "))
      except ValueError:
        print("Error: ingrese el mes correctamente")
        continue
      break
        
    if mes<1 or mes>12:
       print("Inserte fecha correcta")
    elif dia not in range(1,ultimo_dia[mes-1]+1):
       print("Inserte fecha correcta")
    else:
      print(signo(dia,mes))
      break
    