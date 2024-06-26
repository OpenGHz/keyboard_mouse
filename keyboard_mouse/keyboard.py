from __future__ import print_function

from .pyxhook import HookManager, pyxhookkeyevent

import subprocess


class Monitor(object):

    def __init__(self, kdevent=None, parameters=None, hookman=None):
        if hookman is None:
            hookman = HookManager(parameters=True)
        self.hookman = hookman
        self.parameters = {"running": True} if parameters is None else parameters
        # Define our callback to fire when a key is pressed down
        if kdevent is not None:
            self.kdevent = kdevent
        self.hookman.KeyDown = self.kdevent
        # Define our parameters for callback function
        self.hookman.KeyDownParameters = self.parameters
        # Hook the keyboard
        self.hookman.HookKeyboard()
        self._last_key = None

    def start(self, daemon=None):
        if daemon is not None:
            self.hookman.daemon = daemon
        self.hookman.start()

    def stop(self):
        if self.hookman.is_alive():
            self.hookman.cancel()

    def is_running(self):
        return self.hookman.is_alive()

    @classmethod
    def is_caps_lock_on():
        """Check if caps lock is on or off. Return True if on, False if off."""
        result = subprocess.run(["xset", "-q"], capture_output=True, text=True)
        lines = result.stdout.split("\n")
        for line in lines:
            if "Caps Lock" in line:
                state = "on" in line.split(":")[2].strip()
                return state

    # This function is called every time a key is presssed
    def kdevent(self, event: pyxhookkeyevent, params):
        # print key info
        print(event)
        # If the ascii value matches spacebar, terminate the while loop
        # ascii = ord('a')  # 32 means space
        self._last_key = event.Key
        if event.Key == "Escape":  # ESC键
            self.stop()

    def get_last_key(self):
        return self._last_key

    def clear_last_key(self):
        self._last_key = None


if __name__ == "__main__":
    import time

    monitor = Monitor()
    monitor.start()
    while monitor.is_running():
        time.sleep(1)
