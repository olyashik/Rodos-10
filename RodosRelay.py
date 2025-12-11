import requests
import time

# Включение, выключение и подача импульсов на реле
class RodosRelay:
    def __init__(self, numb_rel, command, ip, user="admin", password="admin"):
        """
        Прямое подключение к RODOS 10
        По умолчанию: IP 192.168.1.20, логин/пароль admin/admin
        """
        self.ip = ip
        self.auth = f"{user}:{password}"
        self.numb_rel = numb_rel
        self.command = command
    
    # Реле 1    
    def _relay_(self):
        """Включить реле 1"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb0n.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb{self.numb_rel}{self.command}.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    
