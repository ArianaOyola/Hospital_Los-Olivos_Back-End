from sqlalchemy import inspect, text
from app.database import engine

tablas = [
    "users",
    "patients",
    "doctors",
    "appointments",
    "medical_records",
]

inspector = inspect(engine)

with engine.connect() as conexion:
    for tabla in tablas:
        if inspector.has_table(tabla):
            cantidad = conexion.execute(
                text(f'SELECT COUNT(*) FROM "{tabla}"')
            ).scalar_one()
            print(f"{tabla}: {cantidad} registros")
        else:
            print(f"{tabla}: no encontrada")
