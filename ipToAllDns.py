#Import dns.resolver 
import dns.resolver 
import dns.reversename
import logging


# '''
# A- permet de donner l'addresse ip 
# AAAA- permet de donner uniquement l'addrese ipv6 connecter à ce dommaine
#MX(Mail exchange ) permet de savoir le serveur de messagerie qui responsable de l'acceptation des emaisls 


# les enregistrements de la zone DNS inversée (reverse DNS) sont utilisés pour mapper les adresses IP aux noms de domaine associés , ce qui permet de trouver le nom de domaine d'un hôte à partir de son adresse IP.

  
logging.basicConfig(level=logging.DEBUG)
def reverseip_to_ptr(r_ip):
  
  try: 
    result = dns.resolver.resolve(r_ip,'PTR')
  
    for val in result: 
      print('record reverse',val.to_text())
    
  except Exception as e: 
    print(e)



#creer une fonction qui permet d'inverser une adresse ip 
def inv_dns(ip):
  print("true record...",ip)
  return dns.reversename.from_address(ip)

#creer une fonction qui convertir un prompt de nom de domaine en addresse ip puis faire le reverse DNS 

#convertir les noms de domaines en ipv4
def name_to_ipv4(name):
  try:
    result_ip = dns.resolver.resolve(name,"A") #pour savoir quelle addresse ip est associé à ce nom de domaine 

    for val in result_ip: 
      return val.to_text()

  except Exception as e:
    print(e)

#converir le nom de domaine en ipv6
def name_to_ipv6(name):
  try:
    result_ipv6 = dns.resolver.resolve(name,"AAAA")

    for val in result_ipv6:
      return val.to_text()
      
  except Exception as e: 
    print(e)





name = input("entrer le nom du domaine:  ")
ip = name_to_ipv4(name)
reverse_ip = inv_dns(ip)

reverseip_to_ptr(reverse_ip)
# name_to_ipv6(name)
