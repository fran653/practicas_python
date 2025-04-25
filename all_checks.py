#!/usr/bin/env python3
  
import os
import sys
def check_reboot():
    pass

def main():
    if check_reboot():
        print("Pendding Reboot.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
