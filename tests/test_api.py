from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

from app import main
from app.service import ServiceReservation, produits_demo


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main, "service", ServiceReservation(produits_demo()))
    return TestClient(main.app)


def stock_serum(client):
    produits = client.get("/produits", params={"q": "sérum"}).json()
    return produits[0]["stock"]


def test_sante(client):
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.json() == {"statut": "ok"}


def test_recherche_par_nom(client):
    reponse = client.get("/produits", params={"q": "sérum"})
    assert reponse.status_code == 200
    assert [p["nom"] for p in reponse.json()] == ["Sérum physiologique"]


def test_reservation_creee_et_stock_diminue(client):
    reponse = client.post("/reservations", json={"produit_id": 1, "quantite": 2})
    assert reponse.status_code == 201
    assert stock_serum(client) == 8


def test_stock_insuffisant_donne_409(client):
    reponse = client.post("/reservations", json={"produit_id": 4, "quantite": 5})
    assert reponse.status_code == 409


def test_produit_inconnu_donne_404(client):
    reponse = client.post("/reservations", json={"produit_id": 99, "quantite": 1})
    assert reponse.status_code == 404


def test_quantite_invalide_donne_422(client):
    reponse = client.post("/reservations", json={"produit_id": 1, "quantite": 0})
    assert reponse.status_code == 422


def test_reservation_expiree_libere_le_stock(monkeypatch):
    monkeypatch.setattr(
        main, "service", ServiceReservation(produits_demo(), duree=timedelta(0))
    )
    client = TestClient(main.app)
    client.post("/reservations", json={"produit_id": 1, "quantite": 2})
    assert stock_serum(client) == 10