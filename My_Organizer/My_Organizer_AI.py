import openvino, openvino_genai, typing, My_Organizer_AI_Interface

class LLM(My_Organizer_AI_Interface.LLM_Interface):
    def __init__(self: typing.Self):
        self.language_model: str = f"ai_model"
        if f"NPU" in openvino.Core().available_devices:
            self.device: str = f"NPU"
        
        elif f"GPU" in openvino.Core().available_devices:
            self.device: str = f"GPU"

        else:
            self.device: str = f"CPU"

    @typing.override
    def __init_model__(self: typing.Self):
        pipe: openvino_genai.LLMPipeline = openvino_genai.LLMPipeline(self.language_model, self.device)
        return pipe

    @typing.override
    def __response_from_AI__(self: typing.Self, pipe: openvino_genai.LLMPipeline = None, query: str = None) -> str:
        self.config: openvino_genai.GenerationConfig = openvino_genai.GenerationConfig()
        self.config.max_new_tokens: int = 1024
        self.config.temperature: float = 0.7
        self.config.top_p: float = 0.5
        self.config.top_k: float = 50
        self.config.repetition_penalty: float = 1.1
        self.config.num_return_sequences: int = 1
        self.config.num_beams: int = 1
        self.config.num_return_sequences; int = 1
        self.config.do_sample: bool = True

        self.result: str = pipe.generate(query, self.config)

        return self.result