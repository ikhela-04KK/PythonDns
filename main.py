#Utilise Le module pour faire une requête dns 

import sys   # va permettre de recuperer le 1er argument de la ligne de commande 
import trio  

import dns.message  #fournie des fonctions pour le message dns 
import dns.asyncquery #fournes des requêtes pour les requêtes de façon asynchrone 
import dns.asyncresolver #fournie une asyncrone pour resoudre les problèmes dns 


async def main():
  if len(sys.argv)>1:
    host = sys.argv[0]
  else:
    host = "www.dnspython.org"

  #requpetes udp 
  q = dns.message.make_query(host,"A")
  r = await dns.asyncquery.udp(q,"8.8.8.8")
  print(r)

  #requetes tcp 
  q = dns.message.make_query(host,"A")
  r = await dns.asyncquery.tcp(q,"8.8.8.8")
  print(r)

  #requêtes tls 
  q =dns.message.make_query(host,"A")
  r = await dns.asyncquery.tls(q,"8.8.8.8")
  print(r)

  a = await dns.asyncresolver.resolve(host,"A")
  print(a.response)
  zn = await dns.asyncresolver.zone_for_name(host)
  print(zn)
  
  
if __name__=="__main__":
  trio.run(main)

