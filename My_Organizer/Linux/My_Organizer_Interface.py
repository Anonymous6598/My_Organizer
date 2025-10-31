import abc, typing

class My_Organizer_Interface(abc.ABC):
    @abc.abstractmethod
    def __load_data__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __save_data__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __clean_table__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __new_line__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __delete_line__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __edit_line__(self: typing.Self, row: int, column: int, new_value: str) -> None:
        pass

    @abc.abstractmethod
    def __fullscreen__(self: typing.Self) -> None:
        pass