from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.service import (
    ProduitIntrouvable,
    ServiceReservation,
    StockInsuffisant,
    produits_demo,
)

app = FastAPI(title="pharma-reservation")
service = ServiceReservation(produits_demo())


@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/produits")
def rechercher_produits(q: str = ""):
    return [
        {"id": p.id, "nom": p.nom, "stock": p.stock}
        for p in service.rechercher(q)
    ]

class DemandeReservation(BaseModel):
    produit_id: int
    quantite: int = Field(ge=1)


@app.post("/reservations", status_code=201)
def creer_reservation(demande: DemandeReservation):
    try:
        r = service.reserver(demande.produit_id, demande.quantite)
    except ProduitIntrouvable:
        raise HTTPException(status_code=404, detail="Produit introuvable")
    except StockInsuffisant:
        raise HTTPException(status_code=409, detail="Stock insuffisant")
    return {
        "id": r.id,
        "produit_id": r.produit_id,
        "quantite": r.quantite,
        "expire_le": r.expire_le.isoformat(),
    }