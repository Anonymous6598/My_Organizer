import abc, typing, openvino_genai

class LLM_Interface(abc.ABC):
    
    @abc.abstractmethod
    def __initialize_model__(self: typing.Self) -> openvino_genai.LLMPipeline:
        pass
    
    @abc.abstractmethod
    def __response__(self: typing.Self, prompt: str) -> str:
        pass
