from random import choice, shuffle


# ---------------------------------------------------------------------------- #
def pick_status():
    status_options = [
        "Let's learn how to make a VM and Compiler in JavaScript! - https://github.com/EliteDaMyth/JS-VM-Compiler #javascript #code #100daysofcode #tech",
         "If you were a triangle you'd be acute one.",
        "eBay is so useless. I tried to look up lighters and all they had was 13,749 matches.",
        "(┛ಠ_ಠ)┛彡┻━┻"   ]
    shuffle(status_options)
    return choice(status_options)


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    pick_status()
