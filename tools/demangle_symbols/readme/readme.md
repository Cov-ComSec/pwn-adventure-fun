# Derange Symbols

Frida uses the actual symbols stored in the binary. These are kinda hard to read, so this script is basically parses the running application to grab all the symbols and then demangle them.

I'd suggest piping the output to a file

```bash
python3 demangle.py > readable_syms.txt
```

Then its pretty easy to just grep the symbol you want


```bash
grep -i "canjump" readable_syms.txt
_ZN6Player7CanJumpEv: Player::CanJump()
_ZThn168_N6Player7CanJumpEv: non-virtual thunk to Player::CanJump()
```