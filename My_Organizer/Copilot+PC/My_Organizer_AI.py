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
    def __response__(self: typing.Self, pipe: openvino_genai.LLMPipeline = None, query: str = None) -> str:
        self.config: openvino_genai.GenerationConfig = openvino_genai.GenerationConfig()
        self.config.max_new_tokens = 1024
        self.config.temperature = 0.7
        self.config.top_p = 0.5
        self.config.top_k = 50
        self.config.repetition_penalty = 1.1
        self.config.num_return_sequences = 1
        self.config.num_beams = 1
        self.config.num_return_sequences = 1
        self.config.do_sample = True


        self.result: str = pipe.generate(query, self.config)

        return self.result