import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Buglump:
    def on_window1_destroy(self, object, data=None):
        print("quit with cancel")
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print("quit from menu")
        Gtk.main_quit()

    def __init__(self):
        self.gladefile = "tutorial-1.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.window.show()


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
