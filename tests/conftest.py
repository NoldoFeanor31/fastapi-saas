import pytest

@pytest.fixture
def anyio_backend():
    # Fuerza el backend de anyio a asyncio para todos los tests
    return "asyncio"
