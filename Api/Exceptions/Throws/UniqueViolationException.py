class UniqueViolationException:
    title: str
    message: str

    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

        self.code = 404
