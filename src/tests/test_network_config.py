from network_config_manager import NetworkConfigManager
from netmiko import ConnectHandler

class Test_NetworkConfigManager:
    def setup_method(self):
        self.device = {
            "device_type": "linux",
            "ip": "127.0.0.1",
            "username": "admin",
            "password": "password",
            "port": 2222,
        }
        self.net_connect = None 

    def test_connect(self) -> None:
        """Etablera SSH-anslutning."""
        self.net_connect = ConnectHandler(**self.device)
        print("Connected to device.")
        assert self.net_connect is not None

    def test_update_hostname(self) -> None:
        assert self.net_connect is not None
        new_value = "1"
        """Uppdatera hostname-konfigurationen."""
        command = f"bash -c \"echo 'hostname: {new_value}' > /etc/config/hostname/config.txt\""
        updated_hostname = self.net_connect.send_command(command)
        print(f"Hostname updated to: {new_value}")
        assert updated_hostname.strip() == "1"
    

    # def update_interface_state(self, new_value: str) -> None:
    #     """Uppdatera interface state-konfigurationen."""
    #     if new_value not in ["up", "down"]:
    #         raise ValueError("Invalid value! Interface state must be 'up' or 'down'.")
    #     command = f"bash -c \"echo 'interface_state: {new_value}' > /etc/config/interface/config.txt\""
    #     self.net_connect.send_command(command)
    #     print(f"Interface state updated to: {new_value}")

    # def update_response_prefix(self, new_value: str) -> None:
    #     """Uppdatera response prefix-konfigurationen."""
    #     command = f"bash -c \"echo 'response_prefix: {new_value}' > /etc/config/response/config.txt\""
    #     self.net_connect.send_command(command)
    #     print(f"Response prefix updated to: {new_value}")