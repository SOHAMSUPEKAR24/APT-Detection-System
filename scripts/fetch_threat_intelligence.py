import requests
import yaml
import logging

def fetch_threat_intelligence(indicator):
    with open('config/settings.yml', 'r') as file:
        config = yaml.safe_load(file)
    api_url = config['threat_intelligence_settings']['api_url']
    api_key = config['threat_intelligence_settings']['api_key']
    
    logging.info(f"Fetching threat intelligence for indicator: {indicator}")
    response = requests.get(f"{api_url}/lookup", params={"indicator": indicator}, headers={"Authorization": f"Bearer {api_key}"})
    
    if response.status_code == 200:
        logging.info("Threat intelligence fetched successfully")
        return response.json()
    else:
        logging.error(f"Failed to fetch threat intelligence, Status Code: {response.status_code}")
        return None

if __name__ == "__main__":
    import sys
    indicator = sys.argv[1]
    data = fetch_threat_intelligence(indicator)
    if data:
        print(data)
