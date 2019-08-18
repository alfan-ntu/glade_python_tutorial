import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Buglump():
    def __init__(self):
        self.gladefile = "glade_filechooser_dialog.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")

        # Get the user's home directory
        self.current_folder = os.path.expanduser("~")
        self.window.show()

    def on_file_new_activate(self, menuitem, data=None):
        pass

    def on_file_open_activate(self, menuitem, data=None):
        # file chooser action constants:
        # https://developer.gnome.org/pygtk/stable/class-gtkfilechooser.html#method-gtkfilechooser--set-action
        # Gtk constants of various types can be found from
        # https://developer.gnome.org/pygtk/stable/gtk-constants.html

        # NOTE: Positional parameters of FileChooserDialog have been deprecated
        """
        self.fcd = Gtk.FileChooserDialog(title="Open....",
                   parent=None,
                   action=Gtk.FileChooserAction.OPEN,
                   bottons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        """
        self.fcd = Gtk.FileChooserDialog(title="Open...",
                   parent=None,
                   action=Gtk.FileChooserAction.OPEN)
        self.fcd.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.fcd.add_button(Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        self.response = self.fcd.run()
        if self.response == Gtk.ResponseType.OK:
            print("Selected filepath: %s" % self.fcd.get_filename())
            self.fcd.destroy()

    def on_file_save_activate(self, menuitem, data=None):
        pass

    def on_file_save_as_activate(self, menuitem, data=None):
        pass

    def on_file_quit_activate(self, menuitem, data=None):
        pass

    def on_window1_destroy(self, object, data=None):
        print("Quit with cancel")
        Gtk.main_quit()


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
