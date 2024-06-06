from typing import Protocol


class SendCrmEvent(Protocol):
    def __call__(self, message: str, obj):
        ...
 
