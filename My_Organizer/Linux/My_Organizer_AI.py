import g4f, typing, My_Organizer_AI_Interface

class LLM(My_Organizer_AI_Interface.LLM_Interface):

    LANGUAGE_MODEL: typing.Final[str] = f"gpt-4o-mini"

    def __init__(self: typing.Self) -> None:
        self.ai_client: g4f.Client = g4f.Client()

    @typing.override
    def __response_from_AI__(self: typing.Self, prompt: str) -> str:
        self.user_query: list[dict[str, str]] = [{f"role": f"user", f"content": prompt}]

        self.response: str = self.ai_client.chat.completions.create(model=self.LANGUAGE_MODEL, messages=self.user_query)
        return self.response.choices[0].message.content