from __future__ import unicode_literals

# uggly fix for #41
# from django.utils import version

__all__ = ['VERSION', '__version__']

VERSION = (1, 2, 1, 'alpha', 0)

# uggly fix for #41
__version__ = ".".join([str(x) for x in VERSION[0:3]])
