# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:57:35 2021

@author: Luna Pérez José Luis
"""
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class GUI_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.pgb_garage.setValue(0)
        self.pgb_cocina.setValue(0)
        self.pgb_pasillo.setValue(0)
    def Cambio_cocina(self,x):
        self.pgb_cocina.setValue(x)
        
    def Cambio_garage(self,x):
        self.pgb_garage.setValue(x)
    
    def Cambio_pasillo(self,x):
        self.pgb_pasillo.setValue(x)
        
    def mouseReleaseEvent(self, *args, **kwargs):
        for widget in QApplication.topLevelWidgets():
            if type(widget) == GUI_Main:
                widget.close()

def GUI_show(dic):
    app = QApplication(sys.argv)
    GUI = GUI_Main()
    print("Valor de cocina: " + GUI.pgb_cocina)
    aux=dic.get('cocina')
    GUI.Cambio_cocina(int(aux))
    aux=dic.get('garage')
    GUI.Cambio_garage(int(aux))
    aux=dic.get('pasillo')
    GUI.Cambio_pasillo(int(aux))
    GUI.show()
    sys.exit(app.exec_())

def desploy(dic,GUI):
    aux=dic.get('cocina')
    GUI.Cambio_cocina(int(aux))
    aux=dic.get('garage')
    GUI.Cambio_garage(int(aux))
    aux=dic.get('pasillo')
    GUI.Cambio_pasillo(int(aux))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = GUI_Main()
    GUI.show()
    sys.exit(app.exec_())