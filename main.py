import yaml
import subprocess
import logging

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def execute_playbook(playbook_path, params):
    try:
        for task in playbook_path['tasks']:
            script = task['script']
            logging.info(f"Executing script: {script} with params: {params}")
            subprocess.run(["python", f"scripts/{script}"] + params, check=True)
    except Exception as e:
        logging.error(f"Error executing playbook: {e}")

def main():
    logging.basicConfig(filename='logs/incident_response.log', level=logging.INFO)
    
    config = load_config('config/playbook_mapping.yml')
    incident_type = input("Enter incident type (malware/phishing/unauthorized_access): ")

    if incident_type in config['incident_types']:
        playbook_file = config['incident_types'][incident_type]['playbook']
        playbook_path = load_config(f'playbooks/{playbook_file}')
        params = input("Enter parameters for playbook (space-separated): ").split()
        
        logging.info(f"Executing playbook for {incident_type} with params {params}")
        execute_playbook(playbook_path, params)
    else:
        logging.error(f"Unknown incident type: {incident_type}")

if __name__ == "__main__":
    main()
