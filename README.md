# Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python
**algorithme pour suggérer une liste des actions les plus rentables à  acheter pour maximiser le profit d'un client au bout de deux ans**

- [Bruteforce](#id-bruteforce)

- [Programmation dynamique(algorithme du sac à dos)](#id-optimized)


## Initialisation du projet

### Windows :
    git clone https://github.com/hmignon/P7_mignon_helene.git

    cd [nom du projet]
    python -m venv env
    env\scripts\activate

    pip install -r requirements.txt


### MacOS et Linux :
    git clone https://github.com/hmignon/P7_mignon_helene.git

    cd [nom du projet]
    python3 -m venv env
    source env/bin/activate

    pip install -r requirements.txt


Note : Lors du traitement des données, le programme affiche une barre de progression (tqdm).

## Exécution du programme


### Bruteforce
<div id='id-bruteforce'></div>
**Le montant d'investissement par défaut est fixé à 500€.**

pour lancer le projet
`python bruteforce.py`
`python3 bruteforce.py` (Mac)

### Programmation dynamique
<div id='id-optimized'></div>
La version optimisée nécessite d'entrer le nom du fichier à traiter, **sans le chemin d'accès ni l'extension de fichier** :

`python optimized.py dataset1`
`python3 optimized.py dataset1` (Mac)
