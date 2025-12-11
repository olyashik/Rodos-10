from rodosrelay import *
# Связь с реле (подача команд)
def condition(numbrel, comm):

    relay = RodosRelay(numb_rel = numbrel, command = comm, ip = "192.168.1.20")
    relay._relay_()


