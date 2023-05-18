from datetime import datetime

def saudacao():
     hora = datetime.now(tz=None)
     if hora.hour >= 5 and hora.hour < 13:
          print("bom dia")

     elif hora.hour >= 13 and hora.hour < 18:
          print("boa tarde")

     else:
          print("boa noite")

def create(cliente):
     with open("hotel.txt", "a") as arquivo:
          arquivo.write(str(cliente)+"\n")

def relatorioHospedes():
     with open("hotel.txt", "r") as arquivo:
          print(arquivo.read())
       





          
          

