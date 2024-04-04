import asyncio
from .factories.strategy_factory import PixabayFactory, UnsplashFactory, PexelsFactory

class SearchClient:
    """
    A client for searching media content from different providers.

    Args:
        params (dict): A dictionary containing the provider and API key.
            - provider (str): The provider name ('pixabay', 'unsplash', 'pexels').
            - key (str): The API key for the provider.

    Attributes:
        _api_key (str): The API key for the provider.
        _image_searcher (SearchStrategy): The search strategy for image content.
        _video_searcher (SearchStrategy): The search strategy for video content.
    """

    def __init__(self, params: dict) -> None:
        provider = params.get('provider')
        api_key = params.get('key')

        self._api_key = api_key
        if provider == 'pixabay':
            self._image_searcher = PixabayFactory.get_search_strategy(api_key, 'image')
            self._video_searcher = PixabayFactory.get_search_strategy(api_key, 'video')
        elif provider == 'unsplash':
            self._image_searcher = UnsplashFactory.get_search_strategy(api_key, 'image')
            self._video_searcher = UnsplashFactory.get_search_strategy(api_key, 'video')
        elif provider == 'pexels':
            self._image_searcher = PexelsFactory.get_search_strategy(api_key, 'image')
            self._video_searcher = PexelsFactory.get_search_strategy(api_key, 'video')

    async def asearch(self, params: dict, content_type: str):
        """
        Asynchronously search for media content.

        Args:
            params (dict): A dictionary containing the search parameters.
            content_type (str): The type of content to search for ('image', 'video', 'hybrid').

        Returns:
            dict: A dictionary containing the search results.
                - If content_type is 'image' or 'video', returns the search results for that type.
                - If content_type is 'hybrid', returns a dictionary with 'images' and 'videos' keys,
                  containing the search results for both types.

        Raises:
            ValueError: If an invalid content_type is provided.
        """
        if content_type == 'image':
            return await self._image_searcher.asearch(params)
        elif content_type == 'video':
            return await self._video_searcher.asearch(params)
        elif content_type == 'hybrid':
            image_task = asyncio.create_task(self.asearch(params, 'image'))
            video_task = asyncio.create_task(self.asearch(params, 'video'))
            images, videos = await asyncio.gather(image_task, video_task)
            return {'images': images, 'videos': videos}
        else:
            raise ValueError('Invalid content type')

    def search(self, params: dict, content_type: str):
        """
        Synchronously search for media content.

        Args:
            params (dict): A dictionary containing the search parameters.
            content_type (str): The type of content to search for ('image', 'video', 'hybrid').

        Returns:
            dict: A dictionary containing the search results.
                - If content_type is 'image' or 'video', returns the search results for that type.
                - If content_type is 'hybrid', returns a dictionary with 'images' and 'videos' keys,
                  containing the search results for both types.

        Raises:
            ValueError: If an invalid content_type is provided.
        """
        if content_type == 'image':
            return self._image_searcher.search(params)
        elif content_type == 'video':
            return self._video_searcher.search(params)
        elif content_type == 'hybrid':
            images = self.search(params, 'image')
            videos = self.search(params, 'video')
            return {'images': images, 'videos': videos}
        else:
            raise ValueError('Invalid content type')
    
