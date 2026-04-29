import random
from faker import Faker
from faker.providers import BaseProvider

f=Faker("en_us") #creeaza o instanta a clasei Faker pentru limba romana

def genereaza_clienti(numar_clienti): #functie care genereaza client
    clienti=[]
    for i in range(1,numar_clienti+1):
        
        clienti.append({'id_client':i,'Nume':f.name(),'Salary':random.randint(2400,100000)})
    return clienti
def genereaza_tranzactii(lista_conturi,numar_tranzactii):
    print("WIP")

def genereaza_conturi(lista_clienti):
      counter=1
      conturi=[]
      for i in lista_clienti:
          conturi.append({'id_client': i['id_client'],'id_cont': counter,  'iban': f.iban()})
          counter+=1
      return conturi
def afiseaza_situatie(lista_clienti, lista_conturi):
    print("\n--- SITUATIE CLIENTI SI CONTURI ---")
    # Luam fiecare cont pe rand
    for cont in lista_conturi:  
        # Cautam clientul care are acelasi id_client ca si contul curent
        nume_gasit = "Necunoscut"
        for client in lista_clienti:
            if client['id_client'] == cont['id_client']:
                nume_gasit = client['Nume']
                break # Am gasit omul, oprim cautarea in lista de clienti       
        # Acum avem si numele, si iban-ul, printam frumos cu f-string
        print(f"Clientul {nume_gasit} detine contul IBAN: {cont['iban']}")
if __name__ == "__main__":
    print("Incepem generarea datelor...")
    
    # 1. Generam 3 clienti
    clienti_generati = genereaza_clienti(3)
    
    # 2. Generam conturile pentru acesti clienti
    conturi_generate = genereaza_conturi(clienti_generati)
    afiseaza_situatie(clienti_generati,conturi_generate) #afisam conuri
    
    print("Script executat cu succes.")