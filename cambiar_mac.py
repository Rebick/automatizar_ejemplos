#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface a usar")
    parser.add_option("-a", "--MAC address", dest="new_mac", help="Nueva MAC adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[-] No se ha especificado una interfaz --help para mas info.")
    elif not options.IP:
        # code to handle error
        parser.error("[-] No se ha especificado una MAC --help para mas info.")
    return options


def change_ip(interface, new_mac):
    print("[+] Cambiando la MAC de " + interface + " a " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "interface", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w\w.\w\w\w.\w\w\w:\w\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No se pudo encontrar la MAC")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("MAC actual = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+]Se cambio exitosamente la MAC a " + str(current_mac))
else:
    print("[-] No se pudo cambiar la MAC")
