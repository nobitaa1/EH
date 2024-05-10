####pip install pynput


from pynput import keyboard
import time

# Create a list to store the keystrokes
keystrokes = []

# Define the on_press function to record the keystrokes
def on_press(key):
    keystrokes.append(key)
    print(f'{key} pressed')

# Define the on_release function to record the keystrokes
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the 'esc' key is pressed
        return False
    keystrokes.append(key)
    print(f'{key} released')

# Start the listener to record the keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Run the listener for 10 seconds
    listener.join(timeout=10)

# Print the recorded keystrokes
print(keystrokes)

