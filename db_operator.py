#!/usr/bin/python
import sqlite3
#value define
VD = {'NAME':'name', 'EID':'employee_id', 'AGE':'age', 'ADDR':'address','SAL':'salary'}

class db_em:
    def __init__(self, db_name):
        self.__db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.__create_tab('EMPLOYEE')

    def __create_tab(self,tab_name): 
        self.__tab_name = tab_name
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS %s
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT  NOT  NULL,
       NAME           TEXT    NOT NULL,
       E_ID           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''' % tab_name) 

    def insert_value(self, value):
        if type(value) == type({}):
            #sql_i = "insert into EMPLOYEE values(%s,%s,%d,%s,%f)"
            params = [('xx','123',11,'anhui',1000.2),('xx','123',11,'anhui',1000.2)]
            self.cursor.execute('''insert into %s (NAME, E_ID, AGE, ADDRESS, SALARY)  \
                 values("%s","%s",%d,"%s",%d)''' % (self.__tab_name, value[VD["NAME"]],value[VD["EID"]],value[VD["AGE"]],  \
                 value[VD["ADDR"]], value[VD["SAL"]]))         
        else:
            print 'value: error input!'

    def select_by_id(self, user_id):
         self.cursor.execute('''select id,name,e_id,age from %s where id = %d''' % (self.__tab_name, user_id))
         rst = self.cursor.fetchall()
         print rst

    def del_by_username(self, user_name):
        self.cursor.execute('''delete from %s where name = "%s"''' % (self.__tab_name, user_name))
        

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        
        
    

if '__main__'==__name__:
    db_operator = db_em('test.db')
    value = {VD['NAME']:'michael', VD['EID']:'01234', VD['AGE']:29, VD['ADDR']:'anhui', VD['SAL']:10000.0}
    db_operator.insert_value(value)
    db_operator.select_by_id(15)
    db_operator.del_by_username('michael')
    db_operator.del_by_username('chenjing')
    
