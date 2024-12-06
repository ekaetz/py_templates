import serial
import serial.tools.list_ports

"""
device info:

vid: 045E
pid: 0646

BAUD:   9600
8 bit, no parity, 1 stop bit (All default)

"""
def get_serial_port(vid_hex, pid_hex, verbose_level=0):
    vid = int(vid_hex, 16)
    pid = int(pid_hex, 16)
    if verbose_level > 0:
        print(f"Looking for vid:pid {vid_hex}:{pid_hex}")
    found_port = None
    available = False
    ports = serial.tools.list_ports.comports()
    for port in ports:
        d_vid = port.__dict__['vid']
        d_pid = port.__dict__['pid']
        if verbose_level > 1:  # f'{NNNN:0>4X}'
            d_vid_hex = f'{d_vid:0>4X}'
            d_pid_hex = f'{d_pid:0>4X}'
            print(f"Discovered port {port.__dict__['device']} with vid:pid = {d_vid_hex}:{d_pid_hex}")
        if vid == d_vid and pid == d_pid:
            found_port = port.__dict__['device']
            try:
                s = serial.Serial(found_port)
                available = True
                s.close()
            except (OSError, serial.SerialException):
                pass
            if verbose_level > 0:
                print(f"Found port {port.__dict__['device']}")
                print(f"Available = {available}")
            break
    return found_port, available
# Find device

f, a = get_serial_port("045E","0646")
print(f"Found port {f}, Available = {a}")