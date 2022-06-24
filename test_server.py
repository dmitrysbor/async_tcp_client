# to run: pytest -s tests\test_server.py
import asyncio
from textwrap import dedent

import pytest

import pytest_asyncio.plugin

@pytest.mark.asyncio
async def test_server(unused_tcp_port, event_loop):
    """Test the unused TCP port fixture."""    
    
    port = 8888    
        
    async def client_cb(reader, writer):
        # print("\nclient_cb()")
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')
        reader.close()
        await reader.wait_closed()
       
    server1 = await asyncio.start_server(client_cb, host="localhost", port=port) #port=unused_tcp_port

    with pytest.raises(IOError):
        await asyncio.start_server(client_cb, host="localhost", port=port) #port=unused_tcp_port

    print("\nunused_tcp_port=", unused_tcp_port)
    print("listen port =", port)

    # server1.close()
    await server1.wait_closed()
