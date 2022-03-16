from threading import Thread, Event
from typing import Callable
from pynput.mouse import Listener


class ClickCounter(Thread):
    """Click counter, counting clicks / interval"""
    click_count = 0
    stopped = Event()

    def __init__(self, callback: Callable, interval: float = 1.0) -> None:
        super().__init__()
        self.interval = interval
        self.callback = callback
        self.listener = Listener(on_click=self.click_counter)

    def run(self) -> None:
        """Start mouse click listener and timer"""
        self.listener.start()

        while not self.stopped.wait(self.interval):
            # Call callback with click counter value, after interval expires
            self.callback(self.click_count)
            # Reset counter
            self.click_count = 0

    def click_counter(self, x: float, y: float, button: int, pressed: bool) -> None:
        """Count clicks"""
        if pressed:
            # Count when mouse button is pressed
            self.click_count += 1

    def cancel(self) -> None:
        """Cancel counter timer"""
        # Stop timer
        self.stopped.set()
        # Stop listener
        self.listener.stop()

import tkinter as tk
from tkinter import *

from click_counter import ClickCounter


class Window(tk.Frame):

    def __init__(self, master=None):
        """Create label and StringVar holding its text"""
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        self.cps_text = tk.StringVar(value="0 cps")
        self.cps_label = tk.Label(self, textvariable=self.cps_text)
        self.cps_label.place(relx=0.5, rely=0.5, anchor='center')

    def print_counter(self, count):
        """Thread safe variable set"""
        self.after(0, self.cps_text.set, f"{count} cps")

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.wm_title("CPS counter")
    root.geometry("30x30")
    #root.attributes('-toolwindow', True)
    root.attributes('-topmost', True)


    # Create and start counter
    click_counter = ClickCounter(app.print_counter)
    click_counter.start()

    # Start tkinter app
    root.mainloop()
    # tkinter app is over, cancel click_counter
    click_counter.cancel()
