""" TODO - for hhtp server should reply 200 OK to comply with protocol
from httpx import AsyncClient
import pytest

@pytest.fixture
async def async_app_client():
    async with AsyncClient(base_url='http://localhost:'+str(port)) as client:
        yield client

@pytest.mark.asyncio
async def test_get(async_app_client):
    response = await async_app_client.get(url='http://localhost:'+str(port))
    assert response.status_code == 200, response.text
    async_app_client.close()
    await async_app_client.wait_closed()
"""

# to run: python tests\test_client.py 
import asyncio

port = 8888

async def tcp_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    """
    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
    """

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

for i in range(20):
    asyncio.run(tcp_client('client'+str(i)))