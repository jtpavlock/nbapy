import requests_cache

# cache api responses for 1 week
requests_cache.install_cache(expire_after=604800)
