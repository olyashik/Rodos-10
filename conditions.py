from rodosrelay import *

def condition():
    k = True
    relay = RodosRelay(ip = "192.168.1.20")
    while k == True:
            command = int(input())
            match command:
                case 10:
                    result = relay.first_relay_off()
                case 11:
                    result = relay.first_relay_on()
                case 12:
                    result = relay.first_relay_pulse()
                case 20:
                    result = relay.second_relay_off()
                case 21:
                    result = relay.second_relay_on()
                case 22:
                    result = relay.second_relay_pulse()
                case 30:
                    result = relay.third_relay_off()
                case 31:
                    result = relay.third_relay_on()
                case 32:
                    result = relay.third_relay_pulse()
                case 40:
                    result = relay.fourth_relay_off()
                case 41:
                    result = relay.fourth_relay_on()
                case 42:
                    result = relay.fourth_relay_pulse()
                case _:
                    print("Неизвестная команда")
                    k = False
