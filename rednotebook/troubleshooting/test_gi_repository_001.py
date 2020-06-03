import gi

gi.require_version('Gdk', '3.0')

from gi.repository import Gdk, GdkPixbuf

# from gi.repository import GdkPixbuf


# your application will tell you which formats your copy of GDKPixbuf can load.
print([loader.get_extensions() for loader in GdkPixbuf.Pixbuf.get_formats()])

icon = GdkPixbuf.Pixbuf.new_from_file("/Users/japheth.korir/git/rednotebook-mac/rednotebook/images/rednotebook-icon/rednotebook.svg")
