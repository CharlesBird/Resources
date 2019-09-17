import asyncio

from aioelasticsearch import Elasticsearch

index = "share_datas_history-00001"

async def go():
    es = Elasticsearch(['47.103.32.102:9200'])

    print(await es.search(index))

    await es.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()