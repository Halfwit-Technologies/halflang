class Error():
    def __init__(self, error_name, details) -> None:
        self.error_name = error_name
        self.details = details

    def to_string(self) -> str:
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self,  details) -> None:
        super().__init__("Illegal Character", details)
    