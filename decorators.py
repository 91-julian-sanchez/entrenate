import logging

def log_decorator(func):
    logging.basicConfig(filename='app.log', level=logging.INFO)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Call to function {func.__name__}: {result}")
        return result
    return wrapper