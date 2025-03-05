#Habbenurs del: 
from network_config_manager import NetworkConfigManager


class Test_NetworkConfigManager:
    def setup_method(self):

        self.net_config_manager = NetworkConfigManager()

        self.net_config_manager.connect()
        """Skapar en instans av NetworkConfigManager och ansluter till enheten."""
        self.net_config_manager.update_hostname("1")
        self.net_config_manager.update_interface_state("down")
        self.net_config_manager.update_response_prefix("Standard Response")
        """Skapar en instans av NetworkConfigManager och uppdaterar konfigurationerna."""

    def teardown_method(self):
        self.net_config_manager.disconnect()
        """Stäng anslutningen."""

# 1. Verifiera standardvärden efter setup:
    def test_show_hostname(self):
        self.net_config_manager.show_hostname()
        assert self.net_config_manager.show_hostname() == "hostname: 1"
        """Testa att uppdatera hostname-konfiguration"""
 
    def test_show_response_prefix(self):
        self.net_config_manager.show_response_prefix()
        assert self.net_config_manager.show_response_prefix() == "response_prefix: Standard Response"
        """Testa att uppdatera response prefix-konfigurationen."""     

    def test_show_interface_state(self):
        self.net_config_manager.show_interface_state()
        assert self.net_config_manager.show_interface_state() == "interface_state: down"
        """Testa att uppdatera interface state-konfigurationen."""

#. 2. Testa uppdatering av konfiguration:
    def test_update_hostname(self):
        self.net_config_manager.update_hostname("2")
        updated_hostname = self.net_config_manager.show_hostname()
        assert updated_hostname == "hostname: 2"
        """Testa att uppdatera hostname-konfiguration"""

    def test_update_response_prefix(self):
        self.net_config_manager.update_response_prefix("New Response")
        updated_response_prefix = self.net_config_manager.show_response_prefix()
        assert updated_response_prefix == "response_prefix: New Response"
        """Testa att uppdatera response prefix-konfigurationen."""
        
    def test_update_interface_state(self):
        self.net_config_manager.update_interface_state("up")
        updated_interface_state = self.net_config_manager.show_interface_state()
        assert updated_interface_state == "interface_state: up"
        """Testa att uppdatera interface state-konfigurationen."""
 


