import customtkinter, typing, tkinter, speech_recognition, My_Organizer_AI, My_Organizer_AI_Window_Interface

class AI_Window(customtkinter.CTkToplevel, My_Organizer_AI_Window_Interface.AI_Window_Interface):

    TITLE: typing.Final[str] = f"My Organizer AI chatbot"
    WIDTH: typing.Final[int] = 525
    HEIGHT: typing.Final[int] = 300
    ICON: typing.Final[str] = f"My_Organizer_icon.ico"

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.title(self.TITLE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.after(250, lambda: self.iconbitmap(self.ICON))
        
        self.ai_window_textbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
        self.ai_window_textbox.place(x=0, y=0)

        self.ai_window_textbox.configure(state=f"disabled")

        self.ai_window_entry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
        self.ai_window_entry.place(x=0, y=269)

        self.ai_window_microphone_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
        self.ai_window_microphone_button.place(x=465, y=269)

        self.ai_window_send_request_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response__)
        self.ai_window_send_request_button.place(x=495, y=269)

        self.ai_window_entry.bind(f"<Return>", self.__response__)

    @typing.override
    def __response__(self: typing.Self, configure: str | None = None):
        self.ai_window_entry_data: str = self.ai_window_entry.get()

        self.query: str = My_Organizer_AI.LLM().__response_from_AI__(f"<|system|>You are a helpful AI assistant, who knows everything about business and organization.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>")

        self.ai_window_textbox.configure(state=f"normal")
        self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nGPT-4o-mini:\n{self.query}\n")
        self.ai_window_textbox.configure(state=f"disabled")
        self.ai_window_entry.delete(0, tkinter.END)

    @typing.override
    def __audio_input__(self: typing.Self):
        self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as self.source:
            self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
            self.text: typing.Any = self.recognizer.recognize_google(self.audio_data)

        self.ai_window_entry.insert(f"0", self.text)