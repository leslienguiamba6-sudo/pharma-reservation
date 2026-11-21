# pharma-reservation

Pharma-reservation est une application de recherche des médicaments et produits pharmaceutiques, les réserver s'il s'agit d'un produit non soumis à des prescriptions médicales et le retirer en pharmacie. La recherche se fera par nom de produit ; la recherche par localisation viendra plus tard. Cette réservation a un délai d'expiration.

PS : Le projet évolue par étapes ; la version 1 est volontairement minimale.

!!! -->> Projet pédagogique : ce n’est pas un outil médical, et il ne manipule aucune vraie donnée de santé ou personnelle.

## Objectif du projet

Apprendre à livrer un logiciel de façon automatisée et sécurisée et aussi être davantage autonome. L’application est le prétexte, le support sur lequel je m’entraînes pour l'atteindre. But :
* tester le code automatiquement ;
* l’empaqueter dans un conteneur Docker ;
* le faire passer dans un pipeline qui s’exécute à chaque modification ;
* y ajouter des contrôles de sécurité (secrets, dépendances, image) ;
* comprendre ce que ju fais, pour pouvoir l’expliquer.


## Ce que l'application fera (version 1)
- rechercher un produit
- réserver automatiquement de produit disponible
- faire expirer la réservation

## Ce qu'elle ne fera pas (pour l'instant)
- Pas de connexion au logiciel de gestion officinale (LGO)
- pas de notifications
- pas de synchronisation des stocks
- Pas de réservation soumise à la validation d’un pharmacien (prévue dans une version ultérieure)
- Pas de produits soumis à ordonnance

## Données
Toutes les données sont fictives.

## État du projet
En cours de construction.