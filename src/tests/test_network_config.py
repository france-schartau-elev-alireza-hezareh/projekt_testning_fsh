#Habbenurs del: 
from network_config_manager import NetworkConfigManager


class Test_NetworkConfigManager:
    def setup_method(self):

        self.ncm = NetworkConfigManager()  
        self.ncm.connect()                 
        self.ncm.update_hostname("1")       
        self.ncm.update_interface_state("down")
        self.ncm.update_response_prefix("Standard Response")
       

    def teardown_method(self): 
        self.ncm.disconnect()
        """Stäng anslutningen."""

# 1. Verifiera standardvärden efter setup:
    def test_show_hostname(self):
        self.ncm.show_hostname()
        assert self.ncm.show_hostname() == "hostname: 1"
        """Testa att uppdatera hostname-konfiguration"""
        
    def test_show_interface_state(self):
        self.ncm.show_interface_state()
        assert self.ncm.show_interface_state() == "interface_state: down"
        """Testa att uppdatera interface state-konfigurationen."""
 
    def test_show_response_prefix(self):
        self.ncm.show_response_prefix()
        assert self.ncm.show_response_prefix() == "response_prefix: Standard Response"
        """Testa att uppdatera response prefix-konfigurationen."""     


#. 2. Testa uppdatering av konfiguration:
    def test_update_hostname(self):
        self.ncm.update_hostname("2")
        updated_hostname = self.ncm.show_hostname()
        assert updated_hostname == "hostname: 2"
        """Testa att uppdatera hostname-konfiguration"""

    def test_update_response_prefix(self):
        self.ncm.update_response_prefix("New Response")
        updated_response_prefix = self.ncm.show_response_prefix()
        assert updated_response_prefix == "response_prefix: New Response"
        """Testa att uppdatera response prefix-konfigurationen."""
        
    def test_update_interface_state(self):
        self.ncm.update_interface_state("up")
        updated_interface_state = self.ncm.show_interface_state()
        assert updated_interface_state == "interface_state: up"
        """Testa att uppdatera interface state-konfigurationen."""
 


