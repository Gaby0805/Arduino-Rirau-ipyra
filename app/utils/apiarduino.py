import httpx


async def get_command():
    url = "https://09daaa962cdc80db28f601bd1b870950.serveo.net/"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, timeout=10)
            resp.raise_for_status()  # dispara HTTPError se não for 2xx
            try:
                data = resp.json()
            except ValueError:
                print("⚠️ Resposta não é JSON:", resp.text)
                data = {}
        except httpx.RequestError as e:
            print("❌ Erro de conexão:", e)
            data = {}

    return {"comandos": data.get("commands", [])}