import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "4.0")

from gi.repository import Gtk, WebKit


def on_destroy(window):
    Gtk.main_quit()


window = Gtk.Window()
window.set_title("Kahawa West")

window.show()
window.connect("destroy", on_destroy)
Gtk.main()
