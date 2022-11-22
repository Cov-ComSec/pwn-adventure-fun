import frida
import cxxfilt


if __name__ == "__main__":
    session = frida.attach("PwnAdventure3-Linux-Shipping")
    script = session.create_script("""
        var exports = Module.enumerateExportsSync("libGameLogic.so");
        var i;
        for (i = 0; i < exports.length; i++) {
            send(exports[i].name);
        }
    """)
    script.on('message', lambda message, data: print(message["payload"] + ": " + cxxfilt.demangle(message["payload"])))
    script.load()

