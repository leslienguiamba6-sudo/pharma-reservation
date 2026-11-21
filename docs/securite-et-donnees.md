# Sécurité et données

## Données manipulées
- produits
- stocks
- réservations

## Données personnelles potentielles
- nom
- téléphone
- e-mail

Cela permettra de contacter le client si besoin.

## Règle du projet
- Toutes les données sont fictives. Aucune vraie donnée personnelle ou de santé.

>Une réservation de médicament peut révéler des informations de santé, donc sensibles.

## Risques si les données étaient réelles
- Confidentialité : si les réservations sont lues par une personne malveillante, elle saura qui a réservé quoi et aura toutes les informations sur les clients
- Intégrité : si quelqu’un peut modifier les stocks ou les réservations sans droit, il peut fausser les quantités, annuler la réservation d’un client ou en créer de fausses. Un client se déplace pour rien, et la pharmacie perd confiance dans les informations.

- Disponibilité : si l’application est indisponible, les clients ne peuvent plus chercher ni réserver, et une personne qui a besoin d’un produit peut perdre du temps pour rien. Les pharmacies ne peuvent plus gérer leurs réservations.

## Ce que je mets en place pour limiter ces risques
- aucun secret dans le dépôt : Gitleaks et un .gitignore adapté
- contrôle des dépendances : pip-audit
- scan de l'image : Trivy