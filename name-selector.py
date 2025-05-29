import random
import sys
import os

def getch():
    """Get a single character from standard input without echoing, cross-platform."""
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8', 'ignore')
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def main():
    try:
        with open('Affini Name Reference.md', 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("Error: The file 'Affini Name Reference.md' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    if not lines:
        print("The file 'Affini Name Reference.md' is empty.")
        return

    available = lines.copy()
    selected = random.choice(available)
    print(selected)
    available.remove(selected)

    print("Press Enter or Space to display another line, or 'q' to quit...")

    while available:
        key = getch()
        if key in ('\r', '\n', ' '):
            selected = random.choice(available)
            print(selected)
            available.remove(selected)
        elif key.lower() == 'q':
            break

    if not available:
        print("All lines have been displayed.")

if __name__ == "__main__":
    main()
