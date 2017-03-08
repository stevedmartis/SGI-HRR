#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid as wxgrid
 
class Rejilla(wxgrid.Grid):
    def __init__(self, parent):
        wxgrid.Grid.__init__(self, parent)
        self.CreateGrid(5, 4)
        self.crearColumnas()
 
    def columnas(self):
    """
    Define los atributos de las columnas
    Etiqueta, Tamaño, Tipo lectura, Presentador
    """
    return [
            ('Codigo experto', 65, True, wxgrid.GridCellNumberRenderer()),
            ('Nombre', 65, False, wxgrid.GridCellStringRenderer()),
            ('Descripcion',300, False, wxgrid.GridCellStringRenderer()),
            ('Cantidad',70, False, wxgrid.GridCellFloatRenderer(10,2))
            ('Stock',70, False, wxgrid.GridCellFloatRenderer(10,2))
           ]
 
    def crearColumnas(self):
    """ Establece atributos de las columnas de la rejilla """
        for ind, col in enumerate(self.columnas()):
            self.SetColLabelValue(ind, col[0])
            self.SetColSize(ind, col[1])
            atrib = wxgrid.GridCellAttr()
            atrib.SetReadOnly(col[2])
            atrib.SetRenderer(col[3])
            self.SetColAttr(ind, atrib)
 
class Ventana(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None,
        title = "Control rejilla y base de datos",
        size=(600,200))
        panel = wx.Panel(self)
        self.grilla = Rejilla(panel)
        # Guardan el número de filas y columnas iniciales de la rejilla
        self.numFilas = self.grilla.GetNumberRows()
        self.numCols = self.grilla.GetNumberCollumns()
 
        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerV.Add(self.grilla, 1, wx.EXPAND)
 
        self.crearBotones(panel,sizerH)
        sizerV.Add(sizerH, 0, wx.EXPAND)
        panel.SetSizer(sizerV)
        self.Center()
 
    def datosBotones(self):
    """ Define el rótulo y el manejador de evento del botón """
        return (
                ('', ''), # un espaciador
                ('Guardar', self.guardarRegistro),
                ('Eliminar', self.eliminarRegistro),
                ('Mostrar todos', self.mostrarRegistros),
                ('Limpiar', self.limpiarRejilla),
                ('',''),
                ('Cerrar', self.cerrar),
                ('', '')
               )
 
    def crearBotones(self,panel,sizer):
    """ Crea y posiciona los botones de la interfaz """
        for etiqueta, manejador in self.datosBotones():
            # Si no existe etiqueta, añadir un espaciador
            # y continuar con la siguiente tupla
            if not etiqueta:
                sizer.Add((20, 20), 1, wx.EXPAND)
                continue
            boton = wx.Button(panel, -1, etiqueta)
            self.Bind(wx.EVT_BUTTON, manejador, boton)
            sizer.Add(boton, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.BOTTOM, 3)
 
    # Plantilla para los manejadores de evento de los botones
    def guardarRegistro(self, event):
        pass
 
    def eliminarRegistro(self, event):
        pass
 
    def mostrarRegistros(self, event):
        pass
 
    def limpiarRejilla(self, event):
        pass
 
    def cerrar(self, event):
        pass
 
if __name__ == "__main__":
    app = wx.App()
    frame = Ventana().Show()
    app.MainLoop()