import requests_cache

# cache api responses for 1 day
requests_cache.install_cache(expire_after=86400)
