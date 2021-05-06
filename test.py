def raise_selected(event=None):
text.tag_configure('raise', offset=5)
selection = text.tag_ranges("sel")
text.tag_add('raise', selection[0], selection[1])
return "break"


def underline_selected(event=None):
text.tag_configure('underline', underline=1)selection = text.tag_ranges("sel")
text.tag_add('underline', selection[0], selection[1])
return "break"


def on_find(self):
self.master.find(self.text_to_find.get())
def on_replace(self):
self.master.replace(self.text_to_find.get(), self.text_to_replace_with.get())

if __name__ == '__main__':
mw = tk.Tk()
fw = FindWindow(mw)
mw.mainloop()
