class FCaptchaDownException(Exception):
    def __init__(self) -> None:
        self.message = "FCaptcha is currently down, please try again later."

    def __str__(self) -> str:
        return self.message

class FCaptchaAPIKeyNotFoundException(Exception):
    def __init__(self) -> None:
        self.message = "API key not found."

    def __str__(self) -> str:
        return self.message

class FCaptchaTaskNotFoundException(Exception):
    def __init__(self) -> None:
        self.message = "Task not found."

    def __str__(self) -> str:
        return self.message

class UnknownFcaptchaException(Exception):
    def __init__(self, message : str) -> None:
        self.message = f"An unknown error occurred: {message}"

    def __str__(self) -> str:
        return self.message

class FcaptchaTaskFailedException(Exception):
    def __init__(self) -> None:
        self.message = f"Could not complete task due to an unknown error."

    def __str__(self) -> str:
        return self.message

def parse_exception(message : str):
    exceptions = {
        "API key not found": FCaptchaAPIKeyNotFoundException,
        "Task not found": FCaptchaTaskNotFoundException,
    }

    if exception := exceptions.get(message):
        return exception()
    
    return UnknownFcaptchaException(message)