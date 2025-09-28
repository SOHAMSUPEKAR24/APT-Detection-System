import requests
import logging
import yaml

def block_ip(ip_address):
    with open('config/settings.yml', 'r') as file:
        config = yaml.safe_load(file)
    firewall_api_url = config['network_settings']['firewall_api_url']
    firewall_api_key = config['network_settings']['firewall_api_key']
    
    logging.info(f"Blocking IP address: {ip_address}")
    response = requests.post(f"{firewall_api_url}/block", json={"ip": ip_address}, headers={"Authorization": f"Bearer {firewall_api_key}"})
    
    if response.status_code == 200:
        logging.info(f"Successfully blocked IP: {ip_address}")
    else:
        logging.error(f"Failed to block IP: {ip_address}, Status Code: {response.status_code}")

if __name__ == "__main__":
    import sys
    block_ip(sys.argv[1])
