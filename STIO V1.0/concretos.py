import mysql.connector

class concretos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="123456", database="stio@002dconcretos")

    def __str__(self):
        datos=self.consulta_concretos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_concretos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM concretos ")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_concretos(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM concretos WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_concretos(self,Codigo, Descripción_elemento, Ubicación,Procedencia, Resistencia, Fechadevaciado, Laboratorio, Edad, Fechadefallo, Resultado1, Resultado2, Resultado3, Promedio, Porcentaje, Estado, Liberación, Observación):
        cur = self.cnn.cursor()
        sql='''INSERT INTO concretos (Codigo, Descripción_elemento, Ubicación,Procedencia, Resistencia, fechadevaciado, laboratorio, edad, fechadefallo,resultado1, resultado2, resultado3, promedio, porcentaje, estado, liberación, observación) 
        VALUES('{}', '{}', '{}', '{}','{}','{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')'''.format(Codigo, Descripción_elemento, Ubicación, Procedencia, Resistencia, Fechadevaciado, Laboratorio, Edad, Fechadefallo, Resultado1, Resultado2, Resultado3, Promedio, Porcentaje, Estado, Liberación, Observación)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_concretos(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM concretos WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_concretos(self,Id, Codigo, Descripción_elemento, Ubicación,Procedencia, Resistencia, Fechadevaciado, Laboratorio, Edad, Fechadefallo,Resultado1, Resultado2, Resultado3, Promedio, Porcentaje, Estado, Liberación, Observación):
        cur = self.cnn.cursor()
        sql='''UPDATE concretos SET Codigo='{}', Descripción_elemento='{}', ubicaciónl='{}',procedencia='{}',resistencia='{}',fechavaciado='{}',laboratorio='{}',edad='{}',fechadefallo='{}',resultado1='{}',resultado2='{}',resultado3='{}',estado='{}',liberación='{}',observación='{}', 
        WHERE Id={}'''.format(Codigo, Descripción_elemento, Ubicación,Procedencia, Resistencia, Fechadevaciado, Laboratorio, Edad, Fechadefallo,Resultado1, Resultado2, Resultado3, Promedio, Porcentaje, Estado, Liberación, Observación)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
