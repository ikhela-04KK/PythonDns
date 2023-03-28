# modifier les types d'enregistrement 
# en plus j'ai apris que ces important dans des cas spécfiques de creer son propre serveur dns 
# creation d'un pare-feu pour protéger les serveurs dns 
# systeme de mise en cache DNS 
#utilisation de scapy /DNSCHEF :DNS twist pour tester la robustesse d'un serveur DNS 

#tester ce code mais je crois que c'est possible sur des sites ou l'on a assez d'autorisation



import dns.resolver 
import dns.update 

domain = "example.com"
new_ip = "192.168.1.1"

#creer un objet resolver pour interroger les serveurs DNS 
resolver = dns.resolver.Resolver()

#recuperer la liste des enregistrements A pour example.com 
records = resolver.query(domain,'A')

# recuperer le premier enregistrement A 
record = records[0]

# creer un objet update pour mettre à jout l'enregistrement 
update = dns.update.Update(domain)
update.replace(record.name, record.ttl,record.rdtype, new_ip)

# Envoyer la mise à jour au serveur DNS 
response = dns.query.tcp(update, 'ns1.example.com')