# Santa List Generator

Un petit outil pour générer et gérer des listes de cadeaux (liste du Père Noël).

## Description

Ce projet permet de créer, modifier et exporter des listes de cadeaux pour des destinataires variés. Conçu pour être simple, extensible et scriptable.

## Installation

1. Cloner le dépôt :

	 git clone <url-du-depot>

2. Installer les dépendances (si nécessaire) :

	 pip install -r requirements.txt

## Utilisation

- Pour générer une liste par défaut :

	python -m santa_list_generator.generate

- Pour ajouter un cadeau à un destinataire :

	python -m santa_list_generator.add --name "Alice" --gift "Livre"

- Pour exporter la liste en CSV :

	python -m santa_list_generator.export --format csv --output liste.csv

Adapter les commandes selon l'implémentation réelle des modules.

## Configuration

Configurer via un fichier config.yml ou variables d'environnement selon le projet.

## Tests

Lancer la suite de tests :

	pytest

## Contribution

Les contributions sont bienvenues : ouvrir une issue ou une pull request.

## Licence

Sous licence MIT — voir le fichier LICENSE pour plus de détails.

---

Fichier généré automatiquement — court et factuel.

```
