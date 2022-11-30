import frida
import sys

session = frida.attach("PwnAdventure3-Linux-Shipping")

with open("hooks.js", "r") as f:
    script = session.create_script(f.read())

script.load()
sys.stdin.read()
