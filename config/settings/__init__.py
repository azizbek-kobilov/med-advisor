from .base import *

if config("ENVIRONMENT") == 'production':
    from .production import *
else:
    from .development import *
