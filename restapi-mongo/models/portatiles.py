from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class Portatil(BaseModel):
    marca: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(
        ..., description="Marca del portátil"
    )
    modelo: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(
        ..., description="Modelo del portátil"
    )
    procesador: constr(strip_whitespace=True, min_length=3, max_length=50) = Field(
        ..., description="Procesador del portátil"
    )
    ram: conint(ge=2, le=128) = Field(
        ..., description="Memoria RAM en GB (mínimo 8, máximo 128)"
    )
    almacenamiento: conint(ge=128, le=4000) = Field(
        ..., description="Almacenamiento en GB (mínimo 128, máximo 4000)"
    )
    precio: conint(ge=1000000, le=15000000) = Field(
        ..., description="Precio en COP (entre 1M y 15M)"
    )
    estado: constr(max_length=10) = Field(
        ..., description="Disponibilidad en inventario (disponible o agotado)"
    )