import pymem
import keyboard
import time

pm = pymem.Pymem('csgo.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

dwLocalPlayer = 0xDEB964

while True:
    plr = pm.read_uint(client + dwLocalPlayer)
    if keyboard.is_pressed('space'):
        if pm.read_int(plr + 0x104) == 257:
            pm.write_int(client + 0x52BCDB0, 6)
            time.sleep(0.01)
            