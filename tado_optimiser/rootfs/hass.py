import logging
import requests
import os


class HomeAssistantAPI:
    def __init__(self,):
        self.token = os.getenv("SUPERVISOR_TOKEN")
        self.base_url = "http://supervisor/core/api"
        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def update_entity(self, sensor, payload):
        logging.debug(msg=f"Updating entity: {sensor}")
        fullUrl = f"{self.base_url}/states/{sensor}"
        response = requests.post(fullUrl, headers=self.headers, json=payload)
        logging.debug(msg=f"Status code: {response.status_code}")

        if response.status_code == 201:
            logging.debug(msg=f"New entity successfully created: {sensor}")
        elif response.status_code == 200:
            logging.debug(msg=f"Entity successfully updated: {sensor}")
        else:
            logging.error(msg=f"Error updating entity: {sensor}")

    def get_entity_state(self, sensor):
        fullUrl = f"{self.base_url}/states/{sensor}"
        response = requests.get(fullUrl, headers=self.headers)
        return response.json()["state"]

    def set_hvac_mode(self, entity_id, hvac_mode):
        fullUrl = f"{self.base_url}/services/climate/set_hvac_mode"
        payload = {"entity_id": entity_id, "hvac_mode": hvac_mode}
        response = requests.post(fullUrl, headers=self.headers, json=payload)
        logging.debug(msg=f"Status code: {response.status_code}")

        if response.status_code == 200:
            logging.debug(msg=f"HVAC mode set to '{hvac_mode}' for entity: {entity_id}")
        else:
            logging.debug(msg=f"Failed to set HVAC mode to '{hvac_mode}' for entity: {entity_id}")
