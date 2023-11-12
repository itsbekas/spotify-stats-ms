from spotipy.cache_handler import CacheHandler

class NoCacheHandler(CacheHandler):
    """No cache handler for spotipy.
    
    This class is used to disable caching when using spotipy.
    """
    def get_cached_token(self):
        return None
    
    def save_token_to_cache(self, token_info):
        pass
