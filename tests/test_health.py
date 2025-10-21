import os
import sys

import pytest
from httpx import AsyncClient, ASGITransport

# Añade .../src al sys.path para que Python pueda importar "app"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from app.main import app  # noqa: E402


# Fuerza a usar asyncio (evita el backend "trio")
@pytest.mark.anyio("asyncio")
async def test_health() -> None:
    transport = ASGITransport(app=app)  # nuevo estilo httpx (sin 'app=' directo)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

