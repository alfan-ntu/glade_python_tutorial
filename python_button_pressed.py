import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Buglump:
    def __init__(self):
        self.gladefile = "glade_button_pressed.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.num_display = self.builder.get_object("label1")
        self.window.show()

    def on_button_clicked(self, widget, data=None):
        # did not exactly understand the difference between get_label() and get_text()
        # self.current = self.num_display.get_text()
        # self.current = self.current + widget.get_label()
        self.current = widget.get_label()
        self.num_display.set_label(self.current)

    def on_window1_destroy(self, object, data=None):
        print("Quit with cancel")
        Gtk.main_quit()


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
