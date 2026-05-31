# Secret Santa List Generator

Petit projet Python pour générer un tirage de Secret Santa.

L'objectif : chaque personne tire quelqu'un à qui offrir un cadeau, sans tomber sur elle-même ni sur la personne de son couple.

## Fonctionnement

Le tirage vérifie deux règles :

- une personne ne peut pas s'offrir un cadeau à elle-même ;
- deux personnes d'un même couple ne peuvent pas se tirer entre elles.

Si le tirage n'est pas valide, le script mélange à nouveau les participants jusqu'à trouver une combinaison correcte.

## Structure

```text
.
├── main.py
├── data/
│   └── participants.json
├── functions/
│   ├── create_participants.py
│   ├── shuffle_participants.py
│   ├── check_draw.py
│   └── santa.py
└── requirements.txt
```

## Utilisation prévue

Pour l'instant, la logique principale est dans `functions/santa.py`.

Exemple de données attendues :

```python
couples = [
    ("Alice", "Bob"),
    ("Charlie", "Dana"),
]
```

Puis appel :

```python
santa_list(couples)
```

Exemple de résultat :

```text
Alice offre à Dana
Bob offre à Charlie
Charlie offre à Alice
Dana offre à Bob
```

## A faire

- remplir `data/participants.json` avec les participants ;
- brancher `main.py` pour lancer le tirage facilement ;
- améliorer l'import des fonctions ;
- éventuellement exporter le résultat dans un fichier.

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

Le lancement direct sera prévu depuis :

```bash
python main.py
```

Pour l'instant, `main.py` est encore vide.
