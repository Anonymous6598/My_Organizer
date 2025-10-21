import abc, typing

class LLM_Interface(abc.ABC):
    @abc.abstractmethod
    def __response_from_AI__(self: typing.Self, prompt: str) -> str:
        pass