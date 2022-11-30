# for x in 1..9 {touch $"egg_($x).js"}
import frida
import os
import time

def on_message(message, data):
    print(message)

session = frida.attach("PwnAdventure3-Linux-Shipping")

files = ["./egg_teleporters/" + i for i in os.listdir("./egg_teleporters")]
last_egg = "./egg_teleporters/egg_10.js"
# files.remove(last_egg)

for file in files:
    files.remove(file)
    with open(file, "r") as f:
        script = session.create_script(f.read())
        script.load()   
        time.sleep(3)
        

with open(last_egg, "r") as f:
    script = session.create_script(f.read())
    script.load()
