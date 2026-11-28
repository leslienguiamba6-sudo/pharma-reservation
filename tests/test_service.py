from datetime import datetime, timedelta, timezone

import pytest

from app.service import (
    ProduitIntrouvable,
    ServiceReservation,
    StockInsuffisant,
    produits_demo,
)

DEBUT = datetime(2026, 11, 21, 12, 0, tzinfo=timezone.utc)


def nouveau_service():
    return ServiceReservation(produits_demo(), duree=timedelta(hours=2))


def test_recherche_ignore_la_casse():
    resultats = nouveau_service().rechercher("SÉRUM")
    assert [p.nom for p in resultats] == ["Sérum physiologique"]


def test_reserver_diminue_le_stock():
    service = nouveau_service()
    service.reserver(1, 2, maintenant=DEBUT)
    assert service.produits[1].stock == 8


def test_reserver_plus_que_le_stock_est_refuse():
    service = nouveau_service()
    with pytest.raises(StockInsuffisant):
        service.reserver(4, 3, maintenant=DEBUT)
    assert service.produits[4].stock == 2


def test_produit_inconnu():
    with pytest.raises(ProduitIntrouvable):
        nouveau_service().reserver(99, 1, maintenant=DEBUT)


def test_expiration_libere_le_stock():
    service = nouveau_service()
    service.reserver(1, 2, maintenant=DEBUT)
    assert service.expirer(maintenant=DEBUT + timedelta(hours=1)) == 0
    assert service.produits[1].stock == 8
    assert service.expirer(maintenant=DEBUT + timedelta(hours=2, minutes=1)) == 1
    assert service.produits[1].stock == 10