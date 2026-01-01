import openvino_genai, typing, My_Organizer_AI_Interface

class LLM(My_Organizer_AI_Interface.LLM_Interface):
    def __init__(self: typing.Self):
        self.language_model: str = f"Llama-3.2-1B-Instruct"
        self.device: str = f"NPU"

    @typing.override
    def __init_model__(self: typing.Self):
        pipeline_config = {f"GENERATE_HINT": f"BEST_PERF"}
        pipe: openvino_genai.LLMPipeline = openvino_genai.LLMPipeline(self.language_model, self.device, pipeline_config)
        return pipe

    @typing.override
    def __response_from_AI__(self: typing.Self, prompt: str, pipe: str):
        config: openvino_genai.GenerationConfig = openvino_genai.GenerationConfig()
        config.max_new_tokens: int = 1024
        config.temperature: float = 0.3
        config.top_p: float = 0.5
        config.top_k: float = 1
        config.repetition_penalty: float = 1.1
        config.num_return_sequences: float = 1
        config.num_beams: float = 1
        config.num_return_sequences: float = 1
        config.do_sample: bool = False
        config.eos_token_id: float = -1

        result: str = pipe.generate(prompt, config)
        return result