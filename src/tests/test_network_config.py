#Habbenurs del: 

from network_config_manager import NetworkConfigManager
from netmiko import ConnectHandler

class Test_NetworkConfigManager: # Testklass
    def setup_method(self): # Metod som körs innan varje test
        self.ncm = NetworkConfigManager() 
        self.ncm.connect() 
        self.ncm.update_hostname("1") 
        self.ncm.update_interface_state("down") 
        self.ncm.update_response_prefix("Standard Response") 

    def teardown_method(self): # Metod som körs efter varje test
        self.ncm.disconnect()
        print("Disconnected from device.") 

        
#Alis del:
# 1. Verifiera standardvärden efter setup:
    def test_show_hostname(self): # Testmetod
        """Testa att uppdatera hostname.""" 
        self.ncm.update_hostname("1")
        assert self.ncm.show_hostname() == "hostname: 1" 
        print("Hostname updated to 1.")


    def test_show_interface_state(self): # Testmetod
        """Testa att uppdatera interface state.""" 
        self.ncm.update_interface_state("down") 
        assert self.ncm.show_interface_state() == "interface_state: down" 
        print("Interface state updated to down.") 
    
    def test_show_response_prefix(self): # Testmetod
        """Testa att uppdatera response prefix."""
        self.ncm.update_response_prefix("Standard Response") 
        assert self.ncm.show_response_prefix() == "response_prefix: Standard Response" 
        print("Response prefix updated to Standard Response.")

#. 2. Testa uppdatering av konfiguration:
    def test_update_hostname(self): # Testmetod
        """Testa att uppdatera hostname.""" 
        self.ncm.update_hostname("2") 
        assert self.ncm.show_hostname() == "hostname: 2" 

    def test_update_interface_state(self): # Testmetod
        """Testa att uppdatera interface state.""" 
        self.ncm.update_interface_state("up") 
        assert self.ncm.show_interface_state() == "interface_state: up" 
        
    
    def test_update_response_prefix(self): 
        """Testa att uppdatera response prefix.""" 
        self.ncm.update_response_prefix("New Response") 
        assert self.ncm.show_response_prefix() == "response_prefix: New Response"
       