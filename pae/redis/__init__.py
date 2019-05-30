"""
PyApp - Redis Extension

This extension provides a factory method for connecting to a Redis instance.

"""
from pyapp.versioning import get_installed_version

from .factory import *

__name__ = "PyApp Redis Extension"
__version__ = get_installed_version("pyApp-Redis", __file__)
__default_settings__ = ".default_settings"
__checks__ = ".checks"
