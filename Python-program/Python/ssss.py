import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_lyrics():
    lyrics = [
        "I promis mai poori zindagi tumhari hard disk mai sirf aur sirf acchi memories store karunga",
        "512 GB Ram ki kasam tumhe kabhi hang nhi hone denge",
        "pyaar to duniya karti hai mai to tumse pair karunga wo bhi bluetooth ke sath",
        "aur tumhari zindagi me koi bhi musibat aa jay mere pyar ke antivirus se gujrna padega",
        "kya tum poori zindagi apna password banna chahti ho?"
    ]
    delays = [0.5, 0.9, 0.8, 0.7, 0.3]
    print("Will I send to her 🩷 😘...........:\n")
    time.sleep(1.4)
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush ()
            time.sleep(0.08)
        print()
        time.sleep(delays[i])
print_lyrics()
