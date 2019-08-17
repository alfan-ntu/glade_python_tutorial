import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Buglump:
    def __init__(self):
        # initializing the builder widget
        self.gladefile = "glade_combo_box.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)

        # build the liststore for the combobox
        self.liststore = Gtk.ListStore(int, str)
        self.liststore.append([0, "Select and item:"])
        self.liststore.append([1, "Row 1"])
        self.liststore.append([2, "Row 2"])
        self.liststore.append([3, "Row 3"])
        self.liststore.append([4, "Row 4"])
        self.liststore.append([5, "Row 5"])

        # build the combobox and associate this combobox with the liststore
        self.combobox = self.builder.get_object("combobox1")
        self.combobox.set_model(self.liststore)

        # build a renderer context to display content of the liststore
        self.cell = Gtk.CellRendererText()
        self.combobox.pack_start(self.cell, True)
        self.combobox.add_attribute(self.cell, 'text', 1)
        self.combobox.set_active(0)

        self.window = self.builder.get_object("window1")
        self.window.show()

    def on_combobox1_changed(self, widget, data=None):
        self.index = widget.get_active()
        self.model = widget.get_model()
        self.item = self.model[self.index][1]
        print("ComboBox Active Text is:", self.item)
        print("ComboBox Active Index is:", self.index)
        self.builder.get_object("label1").set_text(self.item)

    def on_window1_destroy(self, object, data=None):
        print("Quit with cancel")
        Gtk.main_quit()


if __name__ == "__main__":
    main = Buglump()
    Gtk.main()
