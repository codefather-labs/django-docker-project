from apps.core import mixins

from settings.environment.settings import get_settings_module, environment

settings = get_settings_module()


class BaseModel(mixins.AutoincrementIDMixin,
                mixins.UUIDMixin,
                mixins.TimestampMixin,
                mixins.DefaultManagerMixin):
    class Meta:
        abstract = True
