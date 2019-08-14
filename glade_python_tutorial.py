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

    # defined actions of menu items
    def on_push_status_activate(self, menuitem, data=None):
        self.status_count += 1
        self.statusbar.push(self.context_id, "Message number %s" % str(self.status_count))

    def on_pop_status_activate(self, menuitem, data=None):
        self.status_count -= 1
        self.statusbar.pop(self.context_id)

    def on_clear_status_activate(self, menuitem, data=None):
        while (self.status_count > 0):
            self.statusbar.pop(self.context_id)
            self.status_count -= 1

    # added an activatable methon connected to Help->About
    # connection is built in glade file using the following statement
    # <signal name="activate" handler="on_gtk_about_activate" swapped="no"/>
    def on_gtk_about_activate(self, menuitem, data=None):
        print("Help about selected")
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def __init__(self):
        self.gladefile = "glade_python_tutorial.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        # added a new about dialog
        self.aboutdialog = self.builder.get_object("aboutdialog1")
        # added status bar
        self.statusbar = self.builder.get_object("statusbar1")
        self.context_id = self.statusbar.get_context_id("status")
        self.status_count = 0
        self.window.show()

        # suppose this if a change from branch gtk_note


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
