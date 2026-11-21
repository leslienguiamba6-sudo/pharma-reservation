# pharma-reservation

pharma-reservation est une application qui permet de rechercher un médicament ou un produit de pharmacie, de le réserver s’il n’est pas soumis à ordonnance, puis de le retirer en pharmacie. La recherche se fera par nom de produit ; la recherche par localisation viendra plus tard. La réservation expire au bout d’un délai défini.
Le projet évolue par étapes ; la version 1 est volontairement minimale.

> Projet pédagogique : ce n’est pas un outil médical, et il ne manipule aucune vraie donnée de santé ou personnelle.

## Objectif du projet

Apprendre à livrer un logiciel de façon automatisée et sécurisée et aussi être davantage autonome. L’application est le prétexte, le support sur lequel je m’entraîne pour l'atteindre. But :
* tester le code automatiquement ;
* l’empaqueter dans un conteneur Docker ;
* le faire passer dans un pipeline qui s’exécute à chaque modification ;
* y ajouter des contrôles de sécurité (secrets, dépendances, image) ;
* comprendre ce que je fais, pour pouvoir l’expliquer.


## Ce que l'application fera (version 1)
- rechercher un produit
- réserver automatiquement un produit disponible
- faire expirer la réservation

## Ce qu'elle ne fera pas (pour l'instant)
- pas de connexion au logiciel de gestion officinale (LGO)
- pas de notifications
- pas de synchronisation des stocks
- pas de réservation soumise à la validation d’un pharmacien (prévue dans une version ultérieure)
- pas de produits soumis à ordonnance

## Données
Toutes les données sont fictives.

## État du projet
En cours de construction.