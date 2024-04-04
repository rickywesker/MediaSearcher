import requests
from abc import ABC, abstractmethod
import requests.exceptions
import aiohttp
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query):
        """
        Abstract method for searching media based on a query.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        pass

    def asearch(self, query):
        """
        Abstract method for asynchronously searching media based on a query.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        pass


class PixabayImageSearchStrategy(SearchStrategy):
    """
    A search strategy for searching images using the Pixabay API.

    Args:
        api_key (str): The API key for accessing the Pixabay API.
    """
    API_URL = 'https://pixabay.com/api/'


    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def search(self, query):
        """
        Search for images using the Pixabay API.

        Args:
            query (str): The search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        params = {'key': self._api_key, 'q': query}
        try:
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
        
    async def asearch(self, params: dict):
        """
        Asynchronously search for images using the Pixabay API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            aiohttp.ClientError: If the API request fails.
        """
        query = params.get('query')
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.API_URL, params={'key': self._api_key, 'q': query}) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            # Handle client errors
            print(f"Client Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None

class PixabayVideoSearchStrategy(SearchStrategy):
    """
    A search strategy for searching videos using the Pixabay API.

    Args:
        api_key (str): The API key for accessing the Pixabay API.
    """
    API_URL = 'https://pixabay.com/api/videos/'


    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

        
    async def asearch(self, params: dict):
        """
        Asynchronously search for videos using the Pixabay API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            aiohttp.ClientError: If the API request fails.
        """
        query = params.get('query')
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.API_URL, params={'key': self._api_key, 'q': query}) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            # Handle client errors
            print(f"Client Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
        
    def search(self, query):
        """
        Search for videos using the Pixabay API.

        Args:
            query (str): The search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        params = {'key': self._api_key, 'q': query}
        try:
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None

class UnsplashImageSearchStrategy(SearchStrategy):
    """
    A search strategy for searching images using the Unsplash API.

    Args:
        api_key (str): The API key for accessing the Unsplash API.
    """
    API_URL = 'https://api.unsplash.com/search/photos'

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def asearch(self, params: dict):
        """
        Search for images using the Unsplash API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': f'Client-ID {self._api_key}'}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.API_URL, params=params, headers=headers) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            # Handle client errors
            print(f"Client Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
    def search(self, params: dict):
        """
        Search for images using the Unsplash API.

        Args:
            query (str): The search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': f'Client-ID {self._api_key}'}
        try:
            response = requests.get(self.API_URL, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None

class UnsplashVideoSearchStrategy(SearchStrategy):
    """
    A search strategy for searching videos using the Unsplash API.

    Args:
        api_key (str): The API key for accessing the Unsplash API.
    """
    API_URL = 'https://api.unsplash.com/search/videos'


    def __init__(self, api_key: str) -> None:
        self._api_key = api_key


    async def asearch(self, params: dict):
        """
        Search for videos using the Unsplash API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            str: A message indicating that video search is not implemented yet.
        """
        return "Unsplash video search not implemented yet."

    def search(self, params: dict):
        """
        Search for videos using the Unsplash API.

        Args:
            query (str): The search query.

        Returns:
            str: A message indicating that video search is not implemented yet.
        """
        return "Unsplash video search not implemented yet."

class PexelsImageSearchStrategy(SearchStrategy):
    """
    A search strategy for searching images using the Pexels API.

    Args:
        api_key (str): The API key for accessing the Pexels API.
    """
    API_URL = 'https://api.pexels.com/v1/search'


    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def asearch(self, params: dict):
        """
        Search for images using the Pexels API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': self._api_key}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.API_URL, params=params, headers=headers) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            # Handle client errors
            print(f"Client Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
    
    def search(self, params: dict):
        """
        Search for images using the Pexels API.

        Args:
            query (str): The search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': self._api_key}
        try:
            response = requests.get(self.API_URL, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
        

class PexelsVideoSearchStrategy(SearchStrategy):
    """
    A search strategy for searching videos using the Pexels API.

    Args:
        api_key (str): The API key for accessing the Pexels API.
    """
    API_URL = 'https://api.pexels.com/videos/search'


    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def asearch(self, params: dict):
        """
        Search for videos using the Pexels API.

        Args:
            params (dict): The parameters for the search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': self._api_key}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.API_URL, params=params, headers=headers) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            # Handle client errors
            print(f"Client Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
        
    def search(self, params: dict):
        """
        Search for videos using the Pexels API.

        Args:
            query (str): The search query.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        headers = {'Authorization': self._api_key}
        try:
            response = requests.get(self.API_URL, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error: {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            return None
        

class EngineBasedSearchStrategy(SearchStrategy):
    """
    A search strategy that uses different search strategies based on the engine.

    Args:
        api_key (str): The API key for accessing the search engine.
        engine (str): The search engine to use ('pixabay', 'unsplash', 'pexels').
    """
    def __init__(self, api_key: str, engine: str) -> None:
        self._api_key = api_key
        self._engine = engine
        self._strategy = self._get_strategy(engine)

    def asearch(self, query):
        raise NotImplementedError
    
    def search(self, query):
        raise NotImplementedError
    
    
    def _get_strategy(self, engine: str) -> SearchStrategy:
        """
        Get the appropriate search strategy based on the search engine.

        Args:
            engine (str): The search engine to use.

        Returns:
            SearchStrategy: The search strategy object.
        """
        raise NotImplementedError


class ModelGeneratedSearchStrategy(SearchStrategy):
    """
    A search strategy that uses a model to generate search results.

    Args:
        model (Model): The model used to generate search results.
    """
    def __init__(self, model) -> None:
        self._model = model

    def asearch(self, query: str) -> dict:
        """
        Generate search results using the model.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        raise NotImplementedError
    
    def search(self, query: str) -> dict:
        """
        Generate search results using the model.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        raise NotImplementedError