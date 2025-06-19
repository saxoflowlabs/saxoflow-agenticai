import click
from saxoflow_agenticai.core.agent_manager import AgentManager
from saxoflow_agenticai.orchestrator.agent_orchestrator import AgentOrchestrator

@click.group()
def cli():
    """🧠 SaxoFlow-AgenticAI CLI"""
    pass

# 🔧 Generation Commands
@cli.command()
@click.option('--spec', prompt='Enter design spec', help='Specification for RTL generation')
def rtlgen(spec):
    """Generate RTL code from a specification."""
    result = AgentManager.get_agent("rtlgen").run(spec)
    click.echo(result)

@cli.command()
@click.option('--rtl_code', prompt='Enter RTL code', help='RTL code for Testbench generation')
def tbgen(rtl_code):
    """Generate testbench for given RTL code."""
    result = AgentManager.get_agent("tbgen").run(rtl_code)
    click.echo(result)

@cli.command()
@click.option('--rtl_code', prompt='Enter RTL code', help='RTL code for Formal Property generation')
def fpropgen(rtl_code):
    """Generate formal properties for given RTL code."""
    result = AgentManager.get_agent("fpropgen").run(rtl_code)
    click.echo(result)

# 📋 Review Commands
@cli.command()
@click.option('--rtl_code', prompt='Enter RTL code', help='RTL code for RTL Review')
def rtlreview(rtl_code):
    """Run RTL review on given RTL code."""
    result = AgentManager.get_agent("rtlreview").run(rtl_code)
    click.echo(result)

@cli.command()
@click.option('--testbench_code', prompt='Enter Testbench code', help='Testbench code for review')
def tbrev(testbench_code):
    """Run review on testbench code."""
    result = AgentManager.get_agent("tb_review").run(testbench_code)
    click.echo(result)

@cli.command()
@click.option('--prop_code', prompt='Enter Formal Properties', help='Formal Properties for review')
def fproprev(prop_code):
    """Run review on formal property code."""
    result = AgentManager.get_agent("fprop_review").run(prop_code)
    click.echo(result)

# 🔄 Full Design Flow
@cli.command()
@click.option('--spec', prompt='Enter full design spec', help='Full specification for full pipeline')
def fullpipeline(spec):
    """Run the full pipeline: RTL + Testbench + Formal Props + Reviews"""
    results = AgentOrchestrator.full_pipeline(spec)

    click.secho("\n[RTL Code]", fg="cyan", bold=True)
    click.echo(results['rtl_code'])

    click.secho("\n[Testbench Code]", fg="cyan", bold=True)
    click.echo(results['testbench_code'])

    click.secho("\n[Formal Properties]", fg="cyan", bold=True)
    click.echo(results['formal_properties'])

    click.secho("\n[RTL Review Report]", fg="green")
    click.echo(results['rtl_review_report'])

    click.secho("\n[Testbench Review Report]", fg="green")
    click.echo(results['tb_review_report'])

    click.secho("\n[Formal Property Review Report]", fg="green")
    click.echo(results['fprop_review_report'])

if __name__ == "__main__":
    cli()
