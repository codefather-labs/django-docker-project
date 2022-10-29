from typing import Optional

from settings.environment.settings import \
    get_settings_module, environment, Environment
from apps.core.repositories.monobank_repository import \
    AbstractRepository, MonobankRepository, SimpleMonobankRepository

settings = get_settings_module()

monobank_repository: Optional[AbstractRepository] = None

match environment:
    case Environment.LOCAL:
        monobank_repository = SimpleMonobankRepository()

    case Environment.PRODUCTION:
        monobank_repository = MonobankRepository()
