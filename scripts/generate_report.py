import yaml
import logging
from jinja2 import Template

def generate_report(incident_details):
    with open('reports/report_template.html', 'r') as file:
        template = Template(file.read())
    
    report_content = template.render(incident_details)
    
    with open(f"reports/incident_report_{incident_details['incident_id']}.html", 'w') as file:
        file.write(report_content)
    
    logging.info(f"Generated incident report for Incident ID: {incident_details['incident_id']}")

if __name__ == "__main__":
    import sys
    import json
    incident_details = json.loads(sys.argv[1])
    generate_report(incident_details)
