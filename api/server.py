from fastapi import FastAPI
from pydantic import BaseModel
from saxoflow_agenticai.core.agent_manager import AgentManager
from saxoflow_agenticai.orchestrator.agent_orchestrator import AgentOrchestrator

app = FastAPI(title="SaxoFlow-AgenticAI", version="0.1")

# 📦 Request models
class SpecRequest(BaseModel):
    spec: str

class RTLRequest(BaseModel):
    rtl_code: str

class TestbenchRequest(BaseModel):
    testbench_code: str

class FormalPropRequest(BaseModel):
    prop_code: str

# 🚀 Generation Endpoints
@app.post("/rtlgen")
def generate_rtl(request: SpecRequest):
    result = AgentManager.get_agent("rtlgen").run(request.spec)
    return {"rtl_code": result}

@app.post("/tbgen")
def generate_testbench(request: RTLRequest):
    result = AgentManager.get_agent("tbgen").run(request.rtl_code)
    return {"testbench_code": result}

@app.post("/fpropgen")
def generate_formalprop(request: RTLRequest):
    result = AgentManager.get_agent("fpropgen").run(request.rtl_code)
    return {"formal_properties": result}

# 🧐 Review Endpoints
@app.post("/rtlreview")
def review_rtl(request: RTLRequest):
    result = AgentManager.get_agent("rtlreview").run(request.rtl_code)
    return {"rtl_review_report": result}

@app.post("/tbrev")
def review_testbench(request: TestbenchRequest):
    result = AgentManager.get_agent("tb_review").run(request.testbench_code)
    return {"tb_review_report": result}

@app.post("/fproprev")
def review_fprop(request: FormalPropRequest):
    result = AgentManager.get_agent("fprop_review").run(request.prop_code)
    return {"fprop_review_report": result}

# 🧠 Full Pipeline Endpoint
@app.post("/fullpipeline")
def full_pipeline(request: SpecRequest):
    results = AgentOrchestrator.full_pipeline(request.spec)
    return results
