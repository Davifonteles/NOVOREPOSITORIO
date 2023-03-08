def listanum():
 listanum=[]
 for i in range (2):
  listanum = listanum + [int(input("Digite um numero"))]
 print(min(listanum),max(listanum))

def sumvalores():
 while True:
   print('''
  
   Menu:
   1. Digite uma lista de 3 número:
   0. Sair.    
   ''')
  
   opcoes = input("digite a opçao escolhida")
   match opcoes:
    case "1":
     listanum = []
     for i in range (3):
      listanum = listanum + [int(input("Digite um numero"))]
     print(f"a soma dos numeros é{listanum[0]+listanum[1]+listanum[2]}")


    case "0":
     break 

listanum()
sumvalores()