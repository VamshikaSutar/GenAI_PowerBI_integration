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
    
    def get_powerbi_url(self):
        return "https://app.powerbi.com/reportEmbed?reportId=c3c44ac7-7ebe-4ec5-9327-5e0557729e07&autoAuth=true&ctid=5989ece0-f90e-40bf-9c79-1a7beccdb861"

    
    # PowerBI sample url1 - "https://app.powerbi.com/reportEmbed?reportId=c3c44ac7-7ebe-4ec5-9327-5e0557729e07&autoAuth=true&ctid=5989ece0-f90e-40bf-9c79-1a7beccdb861"
    # PowerBI sample iframe URL1 - "<iframe title="PBI_testing1" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=c3c44ac7-7ebe-4ec5-9327-5e0557729e07&autoAuth=true&ctid=5989ece0-f90e-40bf-9c79-1a7beccdb861" frameborder="0" allowFullScreen="true"></iframe>"
    #     return self.powerbi_url
