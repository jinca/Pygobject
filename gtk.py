from gi.repository import Gtk

class Saludo:
	def __init__(self):
		self.window = Gtk.Window()
		self.window.set_default_size(640,480)
		self.window.connect('destroy',self.window_on_destroy)
		self.label = Gtk.Label()
		self.label.set_text("Ola k hace")
		self.window.add(self.label)
		self.window.show_all()
     
	def window_on_destroy(widget, data):
		Gtk.main_quit()

if __name__ == '__main__':
	Saludo()
	Gtk.main()
       
