import sys
import csv
from PyQt6.QtWidgets import QApplication,QMainWindow,QTableWidget,QTableWidgetItem,QLabel,QLineEdit,QVBoxLayout
from PyQt6.QtGui import QPixmap

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