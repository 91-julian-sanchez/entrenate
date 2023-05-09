import logging

def log_decorator(func):
    logging.basicConfig(filename='app.log', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Call to function {func.__name__}: {result}")
        return result
    return wrapper