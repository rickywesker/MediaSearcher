from MediaSearcher import SearchClient
import time
from dotenv import load_dotenv
import os

load_dotenv()

pixabay_params = {"provider":"pixabay","key":os.getenv("PIXABAY_KEY")}
unsplash_params = {"provider":"unsplash","key":os.getenv("UNSPLASH_KEY")}
pexels_params = {"provider":"pexels","key":os.getenv("PEXELS_KEY")}


#test single client with asynchrously
async def test_search():
    #search for images
    for param in [pixabay_params,unsplash_params,pexels_params]:
        start_time = time.time()
        search_cli = SearchClient(param)
        params = {'query': 'cat'}
        images = await search_cli.asearch(params, 'hybrid')
        print(f"⏰ Time taken for {param['provider']} asynchronous mode: ", time.time() - start_time, " seconds")
        

    
#sync version
def test_search_sync():
    #search for images
    for param in [pixabay_params,unsplash_params,pexels_params]:
        start_time = time.time()
        search_cli = SearchClient(param)
        params = {'query': 'cat'}
        images = search_cli.search(params, 'hybrid')
        print(f"⏰ Time taken for {param['provider']} synchronous mode: ", time.time() - start_time, " seconds")


if __name__ == '__main__':
    import asyncio
    asyncio.run(test_search())
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    test_search_sync()