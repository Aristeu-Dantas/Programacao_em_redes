fd=open ("bweb_1t_AC_051020221321.csv","r")

totais = {}
fd.readline()
for linha in fd:
    campos=[campos.replace('"','') for campos in linha.split(';')]
    cargo = campos[17]
    candidato = campos[30]
    numVotos = int(campos[31])
    
    dicCargo=totais.get(cargo,None) 
    if dicCargo == None:
        dicCargo = {}
        totais[cargo] = dicCargo
    dicCargo[candidato] = dicCargo.get(candidato,0) + numVotos
fd.close()
# print(totais)

cargos = {"Presidente":1, "Senador":1,"Governador":1, "Deputado Federal": 10, "Deputado Estadual":15}

for cargo in cargos.keys():
    dicCargo= totais[cargo]
    print(cargo,sorted(dicCargo.items(), key=lambda x:x[1], reverse=True)[:cargos[cargo]])