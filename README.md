# My_Organizer

**A lightweight employee records manager with a built-in local AI assistant — no cloud, no API keys, just your data and your machine.**

Manage employee records in a clean spreadsheet-style table, import/export across five file formats, and chat with a locally-running LLM (any OpenVINO-compatible model) for help — all running offline via OpenVINO GenAI, with automatic NPU → GPU → CPU fallback.

<img width="1919" height="924" alt="Snimak ekrana 2026-08-16 230349" src="https://github.com/user-attachments/assets/81c992a2-f6d8-4b60-be9e-93875993ca5d" />

<img width="1919" height="1145" alt="Snimak ekrana 2026-08-16 230337" src="https://github.com/user-attachments/assets/4b6291f1-2136-40c4-add5-b2cf7905f9f2" />

<img width="1919" height="1137" alt="Snimak ekrana 2026-08-16 230614" src="https://github.com/user-attachments/assets/d1cd38c0-72a7-4d74-a89e-fd71593f6d7a" />

<img width="1919" height="1139" alt="Snimak ekrana 2026-08-16 230716" src="https://github.com/user-attachments/assets/e9f98cdf-6e7d-41f0-a74e-1928a2c6fe5f" />

<img width="1919" height="1140" alt="Snimak ekrana 2026-08-16 230702" src="https://github.com/user-attachments/assets/15de5c21-1ea3-4a05-b424-e4d5455becdc" />

## Features

- **Employee records table** — add, edit, and delete rows (Name/Surname, Manager, Department, Job Title, Working Hours, Comments) in a CTkTable grid
- **Import/export** — CSV, Excel, JSON, XML, and SQLite, all through the same load/save workflow
- **Local AI assistant** — chat with an OpenVINO-optimized LLM, rendered with markdown formatting
- **Voice input** — talk to the assistant instead of typing, via speech recognition
- **Runs fully offline** — once the model is downloaded, no internet connection or external API is required
- **Automatic hardware fallback** — picks NPU if available, otherwise GPU, otherwise CPU

## Requirements

- Windows
- A microphone, if you want to use voice input

## Getting started

1. Download and unzip the release package.
2. Set up the AI model (see below) — the `ai_model` folder must sit next to `My_Organizer.exe` inside the extracted folder.
3. Run `My_Organizer.exe`.

No Python installation or dependencies needed — everything is bundled.

## Setting up the AI assistant

The assistant expects an OpenVINO-optimized model in a folder named **`ai_model`**, placed directly next to `My_Organizer.exe`. Any OpenVINO-compatible causal language model works — the app doesn't hardcode a specific one.

Exporting a model requires the `optimum-cli` tool, which needs Python — this is a one-time setup step on any machine (doesn't have to be the one running the app), and the resulting `ai_model` folder can just be copied over afterward.

### 1. Install Optimum Intel

```bash
pip install optimum[openvino]
```

### 2. Export a model with the Optimum CLI

Pick any compatible model from Hugging Face and convert it to OpenVINO IR format. For example, using a small Llama-based chat model:

```bash
optimum-cli export openvino \
  --model meta-llama/Llama-3.2-1B-Instruct \
  --task text-generation-with-past \
  --weight-format int4 \
  ai_model
```

- Swap `--model` for any other Hugging Face model ID you'd like to use.
- `--weight-format int4` (or `int8`) quantizes the model, which is recommended for reasonable performance on NPU/CPU — drop it for full precision if you have the VRAM/RAM to spare.
- The output folder name (`ai_model`) matters — this is exactly what `My_Organizer_AI.py` looks for at startup.

### 3. Place the model folder

Move (or export directly into) the resulting `ai_model` folder so your directory looks like:

```
My_Organizer/
├── My_Organizer.exe
└── ai_model/
    ├── openvino_model.xml
    ├── openvino_model.bin
    └── ...
```

### 4. Run the app

Double-click `My_Organizer.exe`. On first launch, the assistant loads the model onto the best available device (NPU, then GPU, then CPU) — this can take a moment depending on model size and hardware.

## Usage

- Use the ☰ menu to **add**, **edit**, or **delete** rows in the employee table
- **Load table** / **Save table** to import or export data as CSV, Excel, JSON, XML, or SQLite
- Open the AI panel to chat with the assistant, or use the microphone button for voice input

## License

See [LICENSE](LICENSE) for details.

## Important
- New version will be released in September, due to exams at my faculty.
