import csv
from datetime import datetime
import os
import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QTableWidget,QHBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QTableWidgetItem
from clases.usuario import Usuario
from clases.contraseña import Contraseña
import time

cwd=os.getcwd()
ruta=cwd + "/segundo/lab4/archivos/registro_usuario.csv" 

#pide la cantidad de usuario que hay para guardarlos
def pide_ent_pos (que):
    n=-1
    while n < 1:
        print ("\n\n", que, "(>0) ", end= "")
        n=int (input( ))
    return n

#registra el usuario
def registrar_usuario():
    print("\nEsta es la funcion de registro")
    n=pide_ent_pos("ingrese la cantidad de usuarios")
    usuarios=[]
    for i in range(0,n):
        usuario=Usuario()
        usuario.nombre=input("\nIngrese el nombre: ")
        contrase=Contraseña
        contrase.contraseña=input("\nIngrese su contraseña: ")
        lista=[usuario.nombre,contrase.contraseña,datetime.now()]
        usuarios.append(lista)
    
    with open(ruta,"w",newline="") as file:
        writer=csv.writer(file,delimiter=';')
        writer.writerow(["Nombre","Contraseña"]) 
        writer.writerows(usuarios)

def acceso(a):
    class LoginWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            self.setWindowTitle('Ingreso al sistema DABM')
            self.setGeometry(100,100,300,200)
        
            layout = QVBoxLayout()

            label_username = QLabel('Usuario:')
            layout.addWidget(label_username)

            self.edit_username = QLineEdit()#elemento que me permite adicionaral texto
            layout.addWidget(self.edit_username)

            label_password = QLabel('Contraseña:')
            layout.addWidget(label_password)

            self.edit_password = QLineEdit()
            self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)#enmascara tomarlo como oculto
            layout.addWidget(self.edit_password)

            btn_ingresar = QPushButton('Ingresar:')
            btn_ingresar.clicked.connect(self.auth)#boton para ingresar y darle un metodo para validar
            layout.addWidget(btn_ingresar)

            self.setLayout(layout)
    
        def auth(self):
            #print("Boton pulsado")
            username = self.edit_username.text()
            password = self.edit_password.text()

            if self.validate_credentials(username, password):
                print('Acesso concedido')
                a=1
                return (a)
            else:
                print('Acesso denegado')

        def validate_credentials(self,username,password):
            with open(ruta,'r') as file:
                reader = csv.reader(file,delimiter=';')
                for row in reader:
                    print(row[0],row[1])
                    if username == row[0] and password == row[1]:
                        return username and password

    def load_stylesheet():
        return """
            QWidget {
                background-color: #FFFACD;
                box-shadow: 5px 5px 5px #FFFFFF;
            }
            QLabel {
                font-size = 14px;
                color: #FF4500;
            }
            QLineEdit{
                background-color: #FFFFFF;
                border: 1px solid #000000;
                padding: 3px;
                font-size: 14px;
            }
            QPushButton{
                background-color: #40E0D0;
                color: #FFFFFF;
                border: 1px solid #1E90FF;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton:hover{
                background-color: #008080;
                border: 1px solird #4179E1;
            }
        """

    if __name__=='__main__':
        app = QApplication(sys.argv)

        stylesheet = load_stylesheet()
        app.setStyleSheet(stylesheet)


        LoginWindow=LoginWindow()
        LoginWindow.show()

        sys.exit(app.exec())
    

def valor_sensor():
    ##print(os.listdir("Rsegundo\lab4\archivos\Valores.csv"))
    rut=cwd + "/segundo/lab4/archivos/Valores.csv"
    class UserTable(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Tabla de usuarios")
            self.setGeometry(100,100,500,500)

            #crear tabla
            self.table = QTableWidget(self)
            self.table.setGeometry(50,50,400,400)

            self.label_valor = QLabel("Elegir entre valores para pasarlo al arduino",self)
            self.label_valor.setGeometry(200,50,330,20)

            self.texto = QLineEdit(self)   
            self.layout= QVBoxLayout()
            self.layout.addWidget(self.texto)
            self.texto.setGeometry(200,70,100,20)
    
            #leer achivo csv
            with open("segundo/lab4/archivos/Valores.csv", newline="") as csvfile:
                reader = csv.reader(csvfile,delimiter=",")
                data = [row for row in reader]

                #agregar los datos a la tabla
                headers = ["Valores"]
                self.table.setColumnCount(len(headers))
                self.table.setHorizontalHeaderLabels(headers)
                self.table.setRowCount(len(data))

                for i,row in enumerate(data):
                    for j, item in enumerate(row):
                        self.table.setItem(i,j,QTableWidgetItem(item))
    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        user_table = UserTable()
        user_table.show()
        sys.exit(app.exec())     


def salir():
    print("\nGracias por usar nuestra aplicacion")

def menu():
    sel=0
    a=0
    while sel!=3:
        print("Bienvinidos a la aplicacion")
        print("elige una de las opciones:")
        print("1. Registrar usuarios")
        print("2. login")
        print("3. Salir")
        sel=int(input("Elige una opcion: "))
        if sel==1:
            registrar_usuario()
        if sel==2:
            a=acceso(a)
        if a==1:
            valor_sensor()
        if sel==3:
            salir()
menu()
