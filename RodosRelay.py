import requests
import time

class RodosRelay:
    def __init__(self, ip="192.168.1.20", user="admin", password="admin"):
        """
        Прямое подключение к RODOS 10
        По умолчанию: IP 192.168.1.20, логин/пароль admin/admin
        """
        self.ip = ip
        self.auth = f"{user}:{password}"
    
    # Реле 1    
    def first_relay_on(self):
        """Включить реле 1"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb0n.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb0n.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def first_relay_off(self):
        """Выключить реле 1"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb0f.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb0f.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def first_relay_pulse(self):
        """Импульс на реле 1"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb0s.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb0s.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()
        except Exception as e:
            return f"Ошибка: {e}"
    
    # Реле 2  
    def second_relay_on(self):
        """Включить реле 2"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb1n.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb1n.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def second_relay_off(self):
        """Выключить реле 2"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb1f.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb1f.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def second_relay_pulse(self):
        """Импульс на реле 2"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb1s.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb1s.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()
        except Exception as e:
            return f"Ошибка: {e}"
        
    # Реле 3   
    def third_relay_on(self):
        """Включить реле 3"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb2n.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb2n.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def third_relay_off(self):
        """Выключить реле 3"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb2f.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb2f.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def third_relay_pulse(self):
        """Импульс на реле 3"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb2s.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb2s.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()
        except Exception as e:
            return f"Ошибка: {e}"
        
    # Реле 4    
    def fourth_relay_on(self):
        """Включить реле 4"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb3n.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb3n.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def fourth_relay_off(self):
        """Выключить реле 4"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb3f.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb3f.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()  
        except Exception as e:
            return f"Ошибка: {e}"
    
    def fourth_relay_pulse(self):
        """Импульс на реле 4"""
        try:
            # Команда: http://admin:admin@192.168.1.20/protect/rb3s.cgi
            url = f"http://{self.auth}@{self.ip}/protect/rb3s.cgi"
            response = requests.get(url, timeout=3)
            return response.text.strip()
        except Exception as e:
            return f"Ошибка: {e}"