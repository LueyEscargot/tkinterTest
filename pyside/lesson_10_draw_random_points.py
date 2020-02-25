#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial 

In the example, we draw randomly 1000 red points 
on the window.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys, random
from PySide2 import QtGui, QtCore
from PySide2.QtCore import  qApp
from PySide2.QtWidgets import (QHBoxLayout,
                               QHeaderView,
                               QSizePolicy,
                               QTableView,
                               QWidget)

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.9, geometry.height() * 0.9)

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
        
    def drawPoints(self, qp):
      
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)     
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()