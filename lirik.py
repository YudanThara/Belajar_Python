import time

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

RED     = rgb(255, 60, 60)
BLUE    = rgb(80, 150, 255)
YELLOW  = rgb(255, 230, 50)
GREEN   = rgb(60, 200, 100)
CYAN    = rgb(0, 220, 255)
RESET   = "\033[0m"

def lprint(text, delay=0.05, pause=0.1, color=RESET):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()
    if pause > 0:
        time.sleep(pause)

lirik_lagu = [
    ("Kita hampir mati", 0.1, 0.7, RED),
    ("Dan kau selamatkan aku", 0.1, 0.7, GREEN),
    ("Dan ku menyelamatkanmu", 0.1, 0.7, GREEN),
    ("Dan sekarang aku tahu", 0.1, 0.6, BLUE),
    ("", 0.1, 1.2, YELLOW),
    ("Ceeeeriiiitaaaa kita tak jauh berbeda", 0.18, 0.8, YELLOW),
    ("Got beat down by the world", 0.08, 0.4, CYAN),
    ("Sometimes i wanna fold", 0.08, 0.3, CYAN),
    ("Namun, suratmu 'kan kuceritakan", 0.08, 0.4, BLUE),
    ("Ke anak-anakku nanti", 0.09, 0.6, YELLOW),
    ("", 0.1, 0.1, YELLOW),
    ("Bahwa aku pernah dicintai", 0.12, 2, RED),
    ("With everything you are", 0.1, 2, CYAN),
]

for text, delay, pause, color in lirik_lagu:
    lprint(text, delay, pause, color)