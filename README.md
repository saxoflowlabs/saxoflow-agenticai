# 🤖 SaxoFlow-AgenticAI

**SaxoFlow-AgenticAI** is an experimental AI-driven framework that automates digital hardware design and verification using LLM-based agents. Designed for ASIC/FPGA students, researchers, design and verification engineers seeking automation in the RTL development lifecycle. It works standalone or in tandem with [SaxoFlow](https://github.com/saxoflowlabs/saxoflow) to generate, review, and refine RTL designs from natural language specifications.

---

## 📐 Architecture Overview

This project follows an **agentic architecture**, where each stage of the hardware design flow is handled by a dedicated AI agent:

```

\[ Natural Language Spec ]
│
┌─────▼──────┐
│ RTLGenAgent│ ──▶ SystemVerilog RTL
└─────┬──────┘
│
┌─────▼──────┐
│ TBGenAgent │ ──▶ SystemVerilog Testbench
└─────┬──────┘
│
┌─────▼────────┐
│ FPropGenAgent│ ──▶ SVA / Formal Assertions
└─────┬────────┘
│
▼
\[ Review Agents ]
RTL / TB / FProp

````

---

## 🔧 Features

✅ Natural Language to Verilog Generator  
✅ Testbench & Assertion Auto-Generator  
✅ AI-based Code Review Agents  
✅ Iterative improvement pipeline (upcoming)  
✅ Easy integration with [SaxoFlow](https://github.com/saxoflowlabs/saxoflow) for full RTL-to-GDSII flow (upcoming)

---

## 🚀 Quick Start

### 1. Clone and set up virtual environment

```bash
git clone https://github.com/saxoflowlabs/saxoflow-agenticai.git
cd saxoflow-agenticai

python3 -m venv _ai_venv
source _ai_venv/bin/activate

pip install -e .
````

### 2. Configure the model

Edit the file `config/model_config.yaml`:

```yaml
default_provider: groq

groq:
  model: llama3-8b-8192

openrouter:
  model: meta-llama-3-8b-instruct
```

Ensure your API keys are set as environment variables:

```bash
export GROQ_API_KEY=your_key
export OPENROUTER_API_KEY=your_key
```

---

## 🖥️ Usage

### 🧪 CLI Mode

```bash
python3 -m saxoflow_agenticai.cli fullpipeline
```

You will be prompted:

```bash
Enter full design spec:
> Create a 4-bit binary counter with enable and reset.
```

It will print:

* RTL code
* Testbench
* Formal properties
* Review reports

Other CLI commands:

```bash
python3 -m saxoflow_agenticai.cli rtlgen
python3 -m saxoflow_agenticai.cli tbgen
python3 -m saxoflow_agenticai.cli fpropgen
python3 -m saxoflow_agenticai.cli rtlreview
python3 -m saxoflow_agenticai.cli tbrev
python3 -m saxoflow_agenticai.cli fproprev
```

---

## 📁 Repo Structure

```
saxoflow_agenticai/
│
├── agents/
│   ├── generators/
│   └── reviewers/
│
├── core/
│   ├── agent_base.py
│   ├── agent_manager.py
│   ├── log_manager.py
│   ├── model_selector.py
│   └── prompt_manager.py
│
├── orchestrator/
│   └── agent_orchestrator.py
│
├── utils/
│   ├── formatters.py
│   └── validators.py
│
├── prompts/
│   └── *.txt   ← prompt templates
│
├── config/
│   └── model_config.yaml
│
├── cli.py         ← CLI Interface
└── api_server.py  ← FastAPI Server
```

---

## 🧠 What’s Coming Next

* 🔁 Iterative design improvement loop (LLM-based fixing via review)
* 🧪 Symbiyosys, Verilator and Icarus Verilog integration for tool-assisted verification
* 📉 Confidence scoring and metrics per design phase
* 🧠 Human-in-the-loop RTL acceptance
* 🧩 Tight GUI integration with SaxoFlow VSCode plugin

---

## 🤝 Contributing

We welcome contributions from the EDA/FPGA/ML community. To contribute:

1. Fork this repo
2. Work on a branch
3. Submit a Pull Request

Let’s build the future of AI-assisted digital design together.

---

## 📜 License

This project is released under the Apache-2.0 License.

---

## 🧑‍💻 Maintainers

Built by [SaxoFlow Labs](https://github.com/saxoflowlabs) — a student-led initiative from TU Dresden.



