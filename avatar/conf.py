from django.conf import settings
from PIL import Image

from appconf import AppConf


class AvatarConf(AppConf):
    DEFAULT_SIZE = 80
    RESIZE_METHOD = Image.ANTIALIAS
    STORAGE_DIR = 'avatars'
    GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar/'
    GRAVATAR_BACKUP = True
    GRAVATAR_DEFAULT = None
    DEFAULT_URL = 'avatar/img/default.jpg'
    MAX_AVATARS_PER_USER = 42
    MAX_SIZE = 1024 * 1024
    THUMB_FORMAT = 'JPEG'
    THUMB_QUALITY = 85
    HASH_FILENAMES = False
    HASH_USERDIRNAMES = False
    ALLOWED_FILE_EXTS = None
    CACHE_TIMEOUT = 60 * 60
    STORAGE = settings.DEFAULT_FILE_STORAGE
    CLEANUP_DELETED = False
    AUTO_GENERATE_SIZES = (DEFAULT_SIZE,)
    # -1 do not refresh, 0 refresh every time
    SOCIAL_AVATAR_REFRESH_DAYS = 0

    def configure_auto_generate_sizes(self, value):
        return getattr(settings, 'AUTO_GENERATE_AVATAR_SIZES', None) or value
