from typing import Protocol


class SendMail(Protocol):
    def __call__(self, email: str, message: str):
        ...

