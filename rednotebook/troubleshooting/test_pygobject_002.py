import threading
import time

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import GLib


def app_main():
    window = Gtk.Window(default_height=50, default_width=50)
    window.connect("destroy", Gtk.main_quit)

    # progress = Gtk.ProgressBar(show_text=True)
    progress = Gtk.ProgressBar()
    progress.set_show_text(True)
    window.add(progress)

    def update_progress(i):
        progress.pulse()
        progress.set_text(str(i))
        return False

    def example_target():
        for i in range(50):
            GLib.idle_add(update_progress, i)
            time.sleep(0.5)

    window.show_all()

    thread = threading.Thread(target=example_target)
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
    app_main()
    Gtk.main()
