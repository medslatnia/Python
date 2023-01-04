from pathlib import Path
from pprint import pprint
 
fichier = Path(r"C:\Users\slatn\Downloads\projet9.txt")
 
liste_noms = fichier.read_text().splitlines()
#pprint(liste_noms)
 
prenoms = []
for line in liste_noms:
    prenoms.extend(line.split())
    
#pprint(prenoms)
 
prenoms_f = [p.strip(""".,' " """) for p in prenoms]
 
pprint(prenoms_f)
 
fichier.write_text(str(prenoms_f))
 
 
