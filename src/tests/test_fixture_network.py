#VG delen: 
#Istället för setup_metod använd fixture , på samma sätt som i första uppgiften med databas

from network_config_manager import NetworkConfigManager
from netmiko import ConnectHandler
import pytest

@pytest.fixture  # Skapar en fixture
def ncm(): 
    ncm = NetworkConfigManager() 
    ncm.connect() 
    ncm.update_hostname("1") 
    ncm.update_interface_state("down") 
    ncm.update_response_prefix("Standard Response")
    return ncm 

def test_show_hostname(ncm): 
    ncm.update_hostname("1") 
    assert ncm.show_hostname() == "hostname: 1" 
    print("Hostname updated to 1.") 

def test_show_interface_state(ncm): 
    ncm.update_interface_state("down") 
    assert ncm.show_interface_state() == "interface_state: down"
    print("Interface state updated to down.") 


def test_show_response_prefix(ncm): # Testmetod
    ncm.update_response_prefix("Standard Response") 
    assert ncm.show_response_prefix() == "response_prefix: Standard Response" 
    print("Response prefix updated to Standard Response.") 
    

#Skriv en till testmetod som försöker skicka in ett annat värde än up eller down som värde för interface_state och verifiera att rätt exception kastas. 
#Testet ska alltså visa grönt när exceptionet kastas, det är det som förväntas.
def test_update_interface_state_exception(ncm): # Testmetod
    with pytest.raises(ValueError): 
        ncm.update_interface_state("new") 