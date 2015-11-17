__author__ = 'aferreiradominguez'
from gi.repository import Gtk

class Parrilla (Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo de grid")

        grid=Gtk.Grid()
        self.add(grid)

        boton1=Gtk.Button(label="boton 1")
        boton2=Gtk.Button(label="boton 2")
        boton3=Gtk.Button(label="boton 3")
        boton4=Gtk.Button(label="boton 4")
        boton5=Gtk.Button(label="boton 5")
        boton6=Gtk.Button(label="boton 6")

        grid.add(boton1)
        #atach (control,ncol,nfil,ancho,alto"""
        grid.attach(boton2,1,0,2,1)
        grid.attach_next_to(boton3,boton1,Gtk.PositionType.BOTTOM,1,2)
        grid.attach_next_to(boton4,boton3,Gtk.PositionType.RIGHT,2,1)
        grid.attach(boton5,1,2,1,1)
        grid.attach_next_to(boton6,boton5,Gtk.PositionType.RIGHT,1,1)


fiestra=Parrilla()
fiestra.connect("delete-event",Gtk.main_quit)
fiestra.show_all()
Gtk.main()
