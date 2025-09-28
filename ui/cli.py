import click
import subprocess
import logging

@click.group()
def cli():
    pass

@click.command()
@click.option('--incident-type', required=True, type=click.Choice(['malware', 'phishing', 'unauthorized_access']), help='Type of incident')
@click.option('--params', required=True, multiple=True, help='Parameters for the playbook')
def run_playbook(incident_type, params):
    logging.info(f"Running playbook for incident type: {incident_type}")
    subprocess.run(["python", "main.py", incident_type] + list(params), check=True)

cli.add_command(run_playbook)

if __name__ == "__main__":
    cli()
