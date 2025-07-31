import yaml
import os

class ClientManager:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.client_name = self.config['client']['name']
        self.excel_path = self.config['client']['excel_path']
        # self.powerbi_url = self.config['client'].get('powerbi_url', None)

    def get_excel_path(self):
        return self.excel_path

    # def get_powerbi_url(self):
    #     return self.powerbi_url
