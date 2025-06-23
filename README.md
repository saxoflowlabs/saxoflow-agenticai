# 🤖 SaxoFlow-AgenticAI

**SaxoFlow-AgenticAI** is an experimental, open-source AI-driven framework that automates digital IC design and verification. It leverages LLM-based agents for every stage of the hardware design pipeline, from specification to review and reporting.

**Audience:**

* Students & researchers (ASIC/FPGA/digital design)
* RTL & Verification engineers
* EDA/AI/ML enthusiasts

**Works standalone or as a companion to [SaxoFlow](https://github.com/saxoflowlabs/saxoflow) for RTL-to-GDSII flows.**

---

## 📐 Architecture Overview

SaxoFlow-AgenticAI uses a **modular agent pipeline**, with a dedicated LLM-powered agent for each stage.
Agents can use different LLM providers (Groq, Mistral, Google Gemini, Fireworks, etc) — *configurable per agent!*

### **Block Diagram**

```
[ Natural Language Spec / Markdown ]
                │
         ┌──────▼───────┐
         │ RTLGenAgent  │  ───► [ SystemVerilog RTL ]
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │ TBGenAgent   │  ───► [ SystemVerilog Testbench ]
         └──────┬───────┘
                │
         ┌──────▼─────────┐
         │ FPropGenAgent  │  ───► [ SVA / Formal Properties ]
         └──────┬─────────┘
                │
        ╔═══════▼════════╗
        ║  Review Agents ║  ───► [ RTLReview, TBReview, FPropReview ]
        ╚═══════┬════════╝
                │
         ┌──────▼───────┐
         │ DebugAgent   │  ───► [ Debug Reports ]
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │ ReportAgent  │  ───► [ Full Pipeline Summary Report ]
         └──────────────┘
```

**Every box = one agent = one LLM backend (configurable!).**

---

## 🔧 Features

* ✅ **Natural language → Verilog** (spec-driven)
* ✅ **Auto testbench & assertion generation**
* ✅ **Multi-agent review:** AI checks your code and properties
* ✅ **Iterative improvement loops** (user-configurable)
* ✅ **Debugging & simulation log analysis**
* ✅ **Pipeline report generation**
* ✅ **Pluggable LLM backends per agent:** (Groq, Mistral, Gemini, Fireworks, OpenRouter...)
* ✅ **CLI and (future) FastAPI/GUI support**
* ✅ **Designed for easy VSCode plugin integration**

---

## 🚀 Quick Start

### 1. Clone & set up environment

```bash
git clone https://github.com/saxoflowlabs/saxoflow-agenticai.git
cd saxoflow-agenticai

python3 -m venv _ai_venv
source _ai_venv/bin/activate

pip install -e .
```

---

## 🖥️ Usage

### 🔍 **Pipeline Test**

Quickly test that all agent LLMs are connected and mapped:

```bash
python3 -m saxoflow_agenticai.cli testllms
```

### 🧪 **Full Design Pipeline**

Generate, review, debug, and summarize a design from spec:

```bash
python3 -m saxoflow_agenticai.cli fullpipeline -i input/spec/alu_spec.md --iters 2
```

**Other commands:**

```bash
python3 -m saxoflow_agenticai.cli rtlgen -i input/spec/your_spec.md
python3 -m saxoflow_agenticai.cli tbgen -i output/rtl/your_rtl.v
python3 -m saxoflow_agenticai.cli fpropgen -i output/rtl/your_rtl.v
python3 -m saxoflow_agenticai.cli rtlreview -i output/rtl/your_rtl.v
python3 -m saxoflow_agenticai.cli tbreview -i output/tb/your_tb.sv
python3 -m saxoflow_agenticai.cli fpropreview -i output/formal/your_props.sv
python3 -m saxoflow_agenticai.cli debug -i output/sim/your_log.txt
```

**Outputs are saved to `output/` folders and printed to terminal.**

---

## 🧠 Roadmap

* 🔁 Iterative agent review/improvement (user-settable)
* 🧪 Integrated SymbiYosys/Verilator/Icarus runs for feedback-driven refinement
* 📊 LLM confidence scoring
* 🧑‍💻 Human-in-the-loop review acceptance
* 🧩 VSCode plugin & GUI dashboards

---

## 🤝 Contributing

We welcome all contributions — students, researchers, industry engineers.

* **Fork, branch, and submit PRs**
* For ideas, bugfixes, or agent templates: open an issue!

---

## 📜 License

Apache-2.0 License. See [LICENSE](./LICENSE).

---

## 👥 Maintainers

Built by [SaxoFlow Labs](https://github.com/saxoflowlabs) — a student-led community at TU Dresden.

---

