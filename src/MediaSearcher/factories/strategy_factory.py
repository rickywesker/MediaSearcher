from ..strategies import (
    PixabayImageSearchStrategy,
    PixabayVideoSearchStrategy,
    UnsplashImageSearchStrategy,
    UnsplashVideoSearchStrategy,
    PexelsImageSearchStrategy,
    PexelsVideoSearchStrategy,
)
from abc import ABC, abstractmethod

class MediaServiceFactory(ABC):
    @abstractmethod
    def get_media_service(service: str):
        pass


class PixabayFactory:
    @staticmethod
    def get_search_strategy(api_key: str, content_type: str):
        """
        Returns the appropriate search strategy for Pixabay based on the content type.

        Args:
            api_key (str): The API key for Pixabay.
            content_type (str): The type of content to search for (image or video).

        Returns:
            PixabayImageSearchStrategy or PixabayVideoSearchStrategy: The search strategy object.

        Raises:
            ValueError: If an invalid content type is provided.
        """
        if content_type == "image":
            return PixabayImageSearchStrategy(api_key)
        elif content_type == "video":
            return PixabayVideoSearchStrategy(api_key)

        raise ValueError("Invalid content type for Pixabay")


class UnsplashFactory:
    @staticmethod
    def get_search_strategy(api_key: str, content_type: str):
        """
        Returns the appropriate search strategy for Unsplash based on the content type.

        Args:
            api_key (str): The API key for Unsplash.
            content_type (str): The type of content to search for (image or video).

        Returns:
            UnsplashImageSearchStrategy or UnsplashVideoSearchStrategy: The search strategy object.

        Raises:
            ValueError: If an invalid content type is provided.
        """
        if content_type == "image":
            return UnsplashImageSearchStrategy(api_key)
        elif content_type == "video":
            return UnsplashVideoSearchStrategy(api_key)

        raise ValueError("Invalid content type for Unsplash")


class PexelsFactory:
    @staticmethod
    def get_search_strategy(api_key: str, content_type: str):
        """
        Returns the appropriate search strategy for Pexels based on the content type.

        Args:
            api_key (str): The API key for Pexels.
            content_type (str): The type of content to search for (image or video).

        Returns:
            PexelsImageSearchStrategy or PexelsVideoSearchStrategy: The search strategy object.

        Raises:
            ValueError: If an invalid content type is provided.
        """
        if content_type == "image":
            return PexelsImageSearchStrategy(api_key)
        elif content_type == "video":
            return PexelsVideoSearchStrategy(api_key)

        raise ValueError("Invalid content type for Pexels")
