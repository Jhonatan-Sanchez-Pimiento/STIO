from tkinter import *
from tkinter import ttk
from concretos import *

class Ventana(Frame):
    
    concretos = concretos ()
    
    def __init__(self, master=None):
        super().__init__(master,width=1535,height=900)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenadatos()
        
    def habilitarcajas(self,estado):  
        self.txtCodigo.configure(state=estado)
        self.txtDescripcionelemento.configure(state=estado)
        self.txtUbicación.configure(state=estado)
        self.txtProcedencia.configure(state=estado)
        self.txtResistencia.configure(state=estado)
        self.txtFechavaciado.configure(state=estado)
        self.txtLaboratorio.configure(state=estado)
        self.txtEdad.configure(state=estado)
        self.txtFechafallo.configure(state=estado)
        self.txtResultados1.configure(state=estado)
        self.txtResultados2.configure(state=estado)
        self.txtResultados3.configure(state=estado)
        self.txtPromedio.configure(state=estado)
        self.txtPorcentaje.configure(state=estado)
        self.txtEstado.configure(state=estado)
        self.txtLiberacion.configure(state=estado)
        self.txtObservacion.configure(state=estado)
        pass
    
    def habilitarbtnOper(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        
        
    def habilitarbtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)    
        self.btnCancelar.configure(state=estado)  
        
    def limpiarcajas(self):
        self.txtCodigo.delete(0,END)
        self.txtDescripcionelemento.delete(0,END)
        self.txtUbicación.delete(0,END)
        self.txtProcedencia.delete(0,END)
        self.txtResistencia.delete(0,END)
        self.txtFechavaciado.delete(0,END)
        self.txtLaboratorio.delete(0,END)
        self.txtEdad.delete(0,END)
        self.txtFechafallo.delete(0,END)
        self.txtResultados1.delete(0,END)
        self.txtResultados2.delete(0,END)
        self.txtResultados3.delete(0,END)
        self.txtPromedio.delete(0,END)
        self.txtPorcentaje.delete(0,END)
        self.txtEstado.delete(0,END)
        self.txtLiberacion.delete(0,END)
        self.txtObservacion.delete(0,END)
        
        pass
            
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenadatos(self):
        datos= self.concretos.consulta_concretos()
        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        

    def fNuevo(self):
        self.habilitarcajas("normal")
        self.habilitarbtnOper("normal")
        self.habilitarbtnGuardar("normal")
        self.limpiarcajas()
        self.txtCodigo.focus()
        
        pass
       
    def fModificar(self):
        print(self.txtModificar.get())
        valores = self.concretos.buscar_concretos(self.txtModificar.get())
        self.limpiarcajas()
        for row in valores:
            self.txtCodigo.insert(0,values=row[1])
            self.txtDescripcionelemento.insert(0,values=row[1])
            self.txtUbicación.insert(0,values=row[2])
            self.txtProcedencia.insert(0,row[3])
            self.txtResistencia.insert(0,row[4])
            self.txtFechavaciado.insert(0,END)
            self.txtLaboratorio.insert(0,END)
            self.txtEdad.insert(0,END)
            self.txtFechafallo.insert(0,END)
            self.txtResultados1.insert(0,END)
            self.txtResultados2.insert(0,END)
            self.txtResultados3.insert(0,END)
            self.txtPromedio.insert(0,END)
            self.txtPorcentaje.insert(0,END)
            self.txtEstado.insert(0,END)
            self.txtLiberacion.insert(0,END)
            self.txtObservacion.insert(0,END)


        pass
         
    def fGuardar(self):
        self.concretos.inserta_concretos(self.txtCodigo.get(),self.txtDescripcionelemento.get(),self.txtUbicación.get(),self.txtProcedencia.get(), self.txtResistencia.get(),self.txtFechavaciado.get(),self.txtLaboratorio.get(),self.txtEdad.get(),self.txtFechafallo.get(),self.txtResultados1.get(),self.txtResultados2.get(),self.txtResultados3.get(),self.txtPromedio.get(),self.txtPorcentaje.get(),self.txtEstado.get(),self.txtLiberacion.get(),self.txtObservacion.get())
        self.limpiaGrid()
        self.llenadatos()
        self.limpiarcajas()
        pass
     
    def fCancelar(self):
         pass
     
     
    def create_widgets(self):
        frame1 = Frame(self, bg= "#bfdaff")
        frame1.place(x=0,y=0, width=1435, height =100)
        
        self.btnNuevo=Button(frame1,text = "Nuevo", command = self.fNuevo, bg="blue",fg= "white")
        self.btnNuevo.place(x=0, y=48, width=80, height=30)
        
        self.btnModificar=Button(frame1,text = "Modificar", command = self.fModificar, bg="blue",fg= "white",)
        self.btnModificar.place(x=700, y=25, width=65, height=30)
        
        self.txtModificar=Entry(frame1)
        self.txtModificar.place(x=700,y=60, width =65, height=30)
        
    
        frame2 = Frame(self, bg= "#d3dde3")
        frame2.place(x=0,y=100, width=1440, height =190)
        
        self.btnGuardar=Button(frame2,text = "Guardar", command = self.fGuardar, bg="green",fg= "white")
        self.btnGuardar.place(x=700, y=139, width=80, height=30)
        
        self.btnCancelar=Button(frame2,text = "Cancelar", command = self.fCancelar, bg="red",fg= "white")
        self.btnCancelar.place(x=800, y=139, width=80, height=30)
        
        
        lbl1 = Label (frame2, text = "Codigo")
        lbl1.place(x=5,y=30,width =50, height=40)
        self.txtCodigo=Entry(frame2)
        self.txtCodigo.place(x=5,y=70, width =50, height=54)
        
        lbl2 = Label (frame2, text = "Descripción Elemento")
        lbl2.place(x=50,y=30,width =300, height=40)
        self.txtDescripcionelemento=Entry(frame2)
        self.txtDescripcionelemento.place(x=50,y=70, width =300, height=54)
        
        lbl3 = Label (frame2, text = "Ubicación")
        lbl3.place(x=350,y=30,width =70, height=40)
        self.txtUbicación=Entry(frame2)
        self.txtUbicación.place(x=350,y=70, width =70, height=54)
        
        lbl4 = Label (frame2, text = "Procedencia")
        lbl4.place(x=420,y=30,width =80, height=40)
        self.txtProcedencia=Entry(frame2)
        self.txtProcedencia.place(x=420,y=70, width =80, height=54)
        
        lbl4 = Label (frame2, text = "Resistencia")
        lbl4.place(x=500,y=30,width =80, height=40)
        self.txtResistencia=Entry(frame2)
        self.txtResistencia.place(x=500,y=70, width =80, height=54)
        
        lbl4 = Label (frame2, text = "Fecha de Vaciado")
        lbl4.place(x=580,y=30,width =105, height=40)
        self.txtFechavaciado=Entry(frame2)
        self.txtFechavaciado.place(x=580,y=70, width =105, height=54)
        
        lbl5 = Label (frame2, text = "Laboratorio")
        lbl5.place(x=685,y=30,width =80, height=40)
        self.txtLaboratorio=Entry(frame2)
        self.txtLaboratorio.place(x=685,y=70, width =80, height=54)
        
        lbl6 = Label (frame2, text = "Edad")
        lbl6.place(x=765,y=30,width =50, height=40)
        self.txtEdad=Entry(frame2)
        self.txtEdad.place(x=765,y=70, width =50, height=54)
        
        lbl7 = Label (frame2, text = "Fecha de fallo")
        lbl7.place(x=815,y=30,width =50, height=40)
        self.txtFechafallo=Entry(frame2)
        self.txtFechafallo.place(x=815,y=70, width =50, height=54)
        
        lbl8 = Label (frame2, text = "Resultados")
        lbl8.place(x=865,y=30,width =90, height=40)
        self.txtResultados1=Entry(frame2)
        self.txtResultados1.place(x=865,y=70, width =90, height=18)
        self.txtResultados2=Entry(frame2)
        self.txtResultados2.place(x=865,y=88, width =90, height=18)
        self.txtResultados3=Entry(frame2)
        self.txtResultados3.place(x=865,y=106, width =90, height=18)
        
        lbl9 = Label (frame2, text = "Promedio")
        lbl9.place(x=955,y=30,width =90, height=40)
        self.txtPromedio=Entry(frame2)
        self.txtPromedio.place(x=955,y=70, width =90, height=54)
        
        lbl10 = Label (frame2, text = "Porcentaje %")
        lbl10.place(x=1045,y=30,width =85, height=40)
        self.txtPorcentaje=Entry(frame2)
        self.txtPorcentaje.place(x=1045,y=70, width =85, height=54)
        
        lbl11 = Label (frame2, text = "Estado")
        lbl11.place(x=1130,y=30,width =100, height=40)
        self.txtEstado=Entry(frame2)
        self.txtEstado.place(x=1130,y=70, width =100, height=54)
        
        lbl12 = Label (frame2, text = "Liberación")
        lbl12.place(x=1230,y=30,width =80, height=40)
        self.txtLiberacion=Entry(frame2)
        self.txtLiberacion.place(x=1230,y=70, width =80, height=54)
        
        lbl13 = Label (frame2, text = "Observación")
        lbl13.place(x=1310,y=30,width =80, height=40)
        self.txtObservacion=Entry(frame2)
        self.txtObservacion.place(x=1310,y=70, width =80, height=54)
        
        
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13","col14", "col15", "col16"))
        
        self.grid.column("#0", width =20)
        self.grid.column("col1",width =60, anchor= CENTER )
        self.grid.column("col2", width =60, anchor= CENTER)
        self.grid.column("col3", width =60,anchor= CENTER)
        self.grid.column("col4", width =60,anchor= CENTER)
        self.grid.column("col5", width =60, anchor= CENTER) 
        self.grid.column("col6", width =60,anchor= CENTER )
        self.grid.column("col7", width =60, anchor= CENTER)
        self.grid.column("col8", width =60, anchor= CENTER)
        self.grid.column("col9", width =60, anchor= CENTER)
        self.grid.column("col10", width =60,anchor= CENTER )
        self.grid.column("col11", width =60,anchor= CENTER)
        self.grid.column("col12", width =60,anchor= CENTER)
        self.grid.column("col14", width =60,anchor= CENTER )
        self.grid.column("col15", width =60,anchor= CENTER )
        self.grid.column("col16", width =60, anchor= CENTER)
        
        self.grid.heading("#0", text = "N°", anchor= CENTER )
        self.grid.heading("col1", text= "Codigo", anchor= CENTER)
        self.grid.heading("col2", text= "Descipción Elemento", anchor= CENTER)
        self.grid.heading("col3", text= "Procedencia", anchor= CENTER)
        self.grid.heading("col4", text= "Resistencia", anchor= CENTER)
        self.grid.heading("col5", text= "Fecha de Vaciado", anchor= CENTER)
        self.grid.heading("col6", text= "Laboratorio", anchor= CENTER)
        self.grid.heading("col7", text= "Edad", anchor= CENTER)
        self.grid.heading("col8", text= "Fecha de fallo", anchor= CENTER)
        self.grid.heading("col9", text= "Resultados Mpa", anchor= CENTER)
        self.grid.heading("col10", text= "Promedio", anchor= CENTER)
        self.grid.heading("col11", text= "Porcentaje %", anchor= CENTER)
        self.grid.heading("col12", text= "Estado", anchor= CENTER)
        self.grid.heading("col13", text= "Liberación", anchor= CENTER)
        self.grid.heading("col14", text= "Observación", anchor= CENTER)

        self.grid.place(x=1,y=290, width=1434, height = 500)