import abc, typing

class AI_Window_Interface(abc.ABC):
    @abc.abstractmethod
    def __response__(self: typing.Self, configure: str | None = None):
        pass

    @abc.abstractmethod
    def __audio_input__(self: typing.Self):
        pass