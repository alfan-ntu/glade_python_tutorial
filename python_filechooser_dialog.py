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
        self.fcd.set_default_size(300, 200)
        self.create_filechooser_filter()
        self.response = self.fcd.run()
        if self.response == Gtk.ResponseType.OK:
            print("Selected filepath: %s" % self.fcd.get_filename())
            self.fcd.destroy()
        else:
            self.fcd.destroy()

    # added a file filter to the file chooser dialog
    def create_filechooser_filter(self):
        pdf_filter = Gtk.FileFilter()
        pdf_filter.add_mime_type("application/pdf")
        pdf_filter.set_name("*.pdf 檔案")
        self.fcd.add_filter(pdf_filter)

        txt_filter = Gtk.FileFilter()
        txt_filter.add_mime_type("text/plain")
        txt_filter.set_name("*.txt 文字檔案")
        self.fcd.add_filter(txt_filter)

        excel_filter = Gtk.FileFilter()
        excel_filter.add_mime_type("application/vnd.ms-excel")
        excel_filter.add_mime_type("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        excel_filter.set_name("*.xlsx Excel 檔案")
        self.fcd.add_filter(excel_filter)

        any_filter = Gtk.FileFilter()
        any_filter.add_pattern("*.*")
        any_filter.set_name("所有檔案")
        self.fcd.add_filter(any_filter)

    def on_file_save_activate(self, menuitem, data=None):
        pass

    def on_file_save_as_activate(self, menuitem, data=None):
        pass

    def on_file_quit_activate(self, menuitem, data=None):
        print("Quit with cancel")
        Gtk.main_quit()

    def on_window1_destroy(self, object, data=None):
        print("Quit with cancel")
        Gtk.main_quit()


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
