"""Logique de réservation, version 1 : données en mémoire."""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


class ProduitIntrouvable(Exception):
    """Aucun produit ne porte cet identifiant."""


class StockInsuffisant(Exception):
    """Il n'y a pas assez d'exemplaires pour cette réservation."""


@dataclass
class Produit:
    id: int
    nom: str
    stock: int


@dataclass
class Reservation:
    id: int
    produit_id: int
    quantite: int
    expire_le: datetime


def produits_demo():
    """Données fictives uniquement."""
    return [
        Produit(1, "Sérum physiologique", 10),
        Produit(2, "Pastilles pour la gorge", 5),
        Produit(3, "Crème hydratante", 3),
        Produit(4, "Thermomètre", 2),
    ]


class ServiceReservation:
    def __init__(self, produits, duree=timedelta(hours=2)):
        self.produits = {p.id: p for p in produits}
        self.duree = duree
        self.reservations = []
        self._prochain_id = 1

    def rechercher(self, terme):
        terme = terme.strip().casefold()
        return [p for p in self.produits.values() if terme in p.nom.casefold()]

    def reserver(self, produit_id, quantite, maintenant=None):
        maintenant = maintenant or datetime.now(timezone.utc)
        if quantite < 1:
            raise ValueError("La quantité doit être au moins 1")
        produit = self.produits.get(produit_id)
        if produit is None:
            raise ProduitIntrouvable(produit_id)
        if quantite > produit.stock:
            raise StockInsuffisant(produit_id)
        produit.stock -= quantite
        reservation = Reservation(
            self._prochain_id, produit_id, quantite, maintenant + self.duree
        )
        self._prochain_id += 1
        self.reservations.append(reservation)
        return reservation

    def expirer(self, maintenant=None):
        maintenant = maintenant or datetime.now(timezone.utc)
        expirees = [r for r in self.reservations if r.expire_le <= maintenant]
        for r in expirees:
            self.produits[r.produit_id].stock += r.quantite
            self.reservations.remove(r)
        return len(expirees)