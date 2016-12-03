# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import proxybook 
import db_operator as db
  
class MyProxyBook(QMainWindow, proxybook.Ui_ProxyBook):  
    def __init__(self, parent=None):  
        super(MyProxyBook, self).__init__(parent)  
        self.setupUi(self)
        self.__db = db.db_em('test.db')
        self.bt_get.clicked.connect(self.myPrint)
        self.bt_add.clicked.connect(self.addItem)
        self.addPic("test.png")  
        
    def set_content(self, his_name, his_id):
        self.edit_name.setText(his_name)
        self.edit_id.setText(his_id)
        
    def addPic(self, pic_dir):
        pixmap=QtGui.QPixmap()
        pixmap.load(pic_dir)
        item=QGraphicsPixmapItem(pixmap)
        scene=QGraphicsScene()
        scene.addItem(item)
        self.view_id.setScene(scene)
        
    def myPrint(self):
        tmp_str = self.edit_name.text()
        self.edit_id.setText(tmp_str)

    def addItem(self):
        """姓名"""
        e_name = self.edit_name.text()
        e_id = self.edit_id.text() 
        #print e_name 
        if e_name != '':
            value = {db.VD['NAME']:e_name, db.VD['EID']:e_id, db.VD['AGE']:29, db.VD['ADDR']:'hefei', db.VD['SAL']:0.0}
            self.__db.insert_value(value)  
        

if '__main__' == __name__:
    app = QtGui.QApplication(sys.argv)
    qb = MyProxyBook()
    qb.show()
    sys.exit(app.exec_())    
