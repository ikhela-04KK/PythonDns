#Utilise Le module pour faire une requête dns 
import logging
# import sys   # va permettre de recuperer le 1er argument de la ligne de commande 
import asyncio 

import dns.message  #fournie des fonctions pour le message dns 
import dns.asyncquery #fournes des requêtes pour les requêtes de façon asynchrone 
import dns.asyncresolver #fournie une asyncrone pour resoudre les problèmes dns 

logging.basicConfig(level=logging.DEBUG)
async def main():
  host = "www.dnspython.org"
  #requpetes udp 
  q = dns.message.make_query(host,"A")
  r = await dns.asyncquery.udp(q,"8.8.8.8")
  print(f" c'est la requête de {r}")
asyncio.run(main())



# async def main():
#       host = "www.dnspython.org"
#       #requpetes udp 
#       q = dns.message.make_query(host,"A")
#       r = await dns.asyncquery.udp(q,"1.1.1.1")
#       print(r)
    
#       #requetes tcp 
#       q = dns.message.make_query(host,"A")
#       r = await dns.asyncquery.tcp(q,"1.1.1.1")
#       print(r)
    
#       #requêtes tls 
#       tls_dns = host.encode('idna')
#       q =dns.message.make_query(host,"A")
#       r = await dns.asyncquery.tls(q,"1.1.1.1",hostname=tls_dns)
#       print(r)
    
#       a = await dns.asyncresolver.resolve(host,"A")
#       print(a.response)
#       zn = await dns.asyncresolver.zone_for_name(host)
#       print(zn)
    
  
# if __name__ == "__main__":
#   asyncio.run(main())
  

