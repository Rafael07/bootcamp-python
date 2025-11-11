from functools import wraps

from loguru import logger

logger.remove()

logger.add("logs/pipeline.log", format="{time} {level} {message} {file}", level="INFO")


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")

        except Exception as e:
            logger.exception(f"Erro ao executar '{func.__name__}': {e}")
            raise

    return wrapper
