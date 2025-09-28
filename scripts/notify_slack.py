import requests
import yaml
import logging

def notify_slack(message):
    with open('config/settings.yml', 'r') as file:
        config = yaml.safe_load(file)
    webhook_url = config['slack_settings']['webhook_url']
    
    logging.info(f"Sending Slack notification")
    response = requests.post(webhook_url, json={"text": message})
    
    if response.status_code == 200:
        logging.info("Slack notification sent")
    else:
        logging.error(f"Failed to send Slack notification, Status Code: {response.status_code}")

if __name__ == "__main__":
    import sys
    message = sys.argv[1]
    notify_slack(message)
