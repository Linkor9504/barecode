# from PyQt5 import uic
# from PyQt5.QtWidgets import QMainWindow
#
# class MainWindow(QMainWindow):
#    def __init__(self):
#       super(MainWindow, self).__init__()
#       uic.loadUi('mainwindow.ui', self)

# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import uic
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QSizeF, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QFont, QKeySequence
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QToolTip, QShortcut, QDialog, QPushButton, QTextEdit


items = ["ЭТИЗ 6(0306050Б)",
         "ЭТИЗ 8(0308050Б)",
         "ЭТИЗ 10(0310050Б)",
         "ЭТИЗ 12(0312050Б)"]

# class Articul():
#     def __init__(self):
#         self.artikul = None
#         self.background_image = QImage("scene6-N.bmp")
#         self.sm = "03"
#         self.diameter = "06"
#         self.dlinna = "050"
#         self.type_a = "Б"
#         self.nom_length = "50 метров"
#         self.reference = 30
#         self.build_art()
#
#     def change_reference(self, int):
#         self.reference = int
#
#     def change_background_img(self, img):
#         self.background_image = img
#
#     def change_nom_length(self, str):
#         self.nom_length = str
#
#     def build_art(self):
#         self.artikul = "{}{}{}{}".format(self.sm, self.diameter, self.dlinna, self.type_a)
#
#     def change_sm(self, str):
#         self.sm = str
#         self.build_art()
#
#     def change_diameter(self, str):
#         self.diameter = str
#         self.build_art()
#
#     def change_dlinna(self, str):
#         self.dlinna = str
#         self.build_art()
#
#     def change_type_a(self, str):
#         self.type_a = str
#         self.build_art()
#


class MyWin(QtWidgets.QMainWindow):
   def __init__(self):
      super(MyWin, self).__init__()
      uic.loadUi('gui.ui', self)

      QToolTip.setFont(QFont("Tahoma", 15))
      self.shortcut = QShortcut(QKeySequence("Ctrl+Space"), self)
      self.shortcut2 = QShortcut(QKeySequence("Ctrl+Enter"), self)
      self.comboBox.addItems(items)
      self.label.setScaledContents(True)
      self.background_image = QImage("shab.bmp")
      self.image_with_text = self.background_image
      # self.shortcut2.activated.connect(self.count_weight)
      # self.shortcut.activated.connect(self.handle_print)
#         #inits
#       self.new_art = Articul()
#       self.background_image = QImage("scene6-N.bmp")
#       self.length = "50 метров"
#       self.nom_diameter = "6.0 мм"
#       self.part = "№005"
#
#
#
#       self.set_label_image()
#
#         #actions style
#       self.ui.print.setStyleSheet("QPushButton:pressed { background-color: #DE7C02 }")
#       self.ui.print.setStyleSheet("QPushButton:pressed { background-color: #DE7C02 }")
#       self.ui.save_par.setStyleSheet("QPushButton:pressed { background-color: #DE7C02 }")
#       self.ui.btn_brak.setStyleSheet("QPushButton:pressed { background-color: #DE7C02 }")
#
#         #actions
#       self.ui.comboBox.activated.connect(self.change_dim)
#       self.ui.edit_weight.setToolTip("Проверка веса Ctrl+Enter")
#       self.ui.comboBox.setToolTip("Изменение диаметра арматуры")
#       self.ui.btn_brak.setToolTip("Отметка как брак")
#       self.ui.save_par.setToolTip("Сохранить изменения")
#       self.ui.print.setToolTip("Печать Этикетки (Ctrl+Space)")
#       self.ui.print.clicked.connect(self.handle_print)
#       self.ui.save_par.clicked.connect(self.save_param_to_img)
#       self.ui.btn_brak.clicked.connect(self.make_brak)
#
#    def count_weight(self):
#       try:
#             x = int(self.ui.edit_weight.toPlainText())
#         except ValueError:
#             x = 0
#             QMessageBox.critical(self, "Ошибка", "Это не число!", QMessageBox.Yes )
#         error = self.new_art.reference*50*0.05
#         ost = self.new_art.reference*50 - x
#         min = self.new_art.reference*50 - error
#         max = self.new_art.reference*50 + error
#
#         print("Номинальный вес эталона = {} \n"
#           "Номинальный вес бухты = {} \n"
#           "Текущий вес бухты = {}".format(self.new_art.reference, self.new_art.reference*50, x))
#         print("Коррекция = {}гр./{}м.\n ".format(self.new_art.reference*50-x, ost//self.new_art.reference))
#         if x > max:
#             print("Брак!!! Вес больше чем нужно\n \n")
#         elif x < min:
#             print("Брак!!! Вес меньше чем нужно\n \n")
#         else:
#             print("В допуске")
#
#
#     def make_brak(self):
#
#         buttonReply = QMessageBox.information(self, 'Отметка брака!', "Отметить этикетку как брак ?",
#             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#
#         if buttonReply == QMessageBox.Yes:
#             print('Yes clicked.')
#             if self.new_art.background_image == QImage("scene6-N.bmp"):
#                 self.new_art.change_background_img("scene6-B.bmp")
#                 self.make_image_with_text()
#                 self.handle_print()
#                 self.new_art.change_background_img("scene6-N.bmp")
#                 self.make_image_with_text()
#
#             elif self.new_art.background_image == QImage("scene8-N.bmp"):
#                 self.new_art.change_background_img("scene8-B.bmp")
#                 self.make_image_with_text()
#                 self.handle_print()
#                 self.new_art.change_background_img("scene8-N.bmp")
#                 self.make_image_with_text()
#
#             elif self.new_art.background_image == QImage("scene8-N.bmp"):
#                 self.new_art.change_background_img("scene10-B.bmp")
#                 self.make_image_with_text()
#                 self.handle_print()
#                 self.new_art.change_background_img("scene10-N.bmp")
#                 self.make_image_with_text()
#             else:
#                 pass
#         else:
#             print('No clicked.')
#
#
#     def save_param_to_img(self):
#         part = str(self.ui.edit_numb.toPlainText())
#         if part == "":
#             print("Номер партии нет изменений")
#         elif part != "":
#             self.part = part
#             self.ui.edit_numb.setText("")
#         else:
#             pass
#         self.make_image_with_text()
#         self.set_label_image()
#
#     def change_dim(self, index):
#         if index == 0:
#             self.new_art.change_background_img(QImage("scene6-N.bmp"))
#             self.nom_diameter = "6.0 мм"
#             self.new_art.change_reference(38)
#             self.new_art.change_diameter("06")
#             self.make_image_with_text()
#
#         elif index == 1:
#             self.new_art.change_background_img(QImage("scene8-N.bmp"))
#             self.nom_diameter = "8.0 мм"
#             self.new_art.change_reference(60)
#             self.new_art.change_diameter("08")
#             self.make_image_with_text()
#
#         elif index == 2:
#             self.new_art.change_background_img(QImage("scene10-N.bmp"))
#             self.nom_diameter = "10.0 мм"
#             self.new_art.change_reference(98)
#             self.new_art.change_diameter("10")
#             self.make_image_with_text()
#
#         elif index == 3:
#             self.new_art.change_background_img(QImage("scene12-N.bmp"))
#             self.nom_diameter = "12.0 мм"
#             self.new_art.change_reference(98)
#             self.new_art.change_diameter("12")
#             self.make_image_with_text()
#
#         else:
#             pass
#
      def set_label_image(self):
         self.ui.label.setPixmap(QPixmap.fromImage(self.image_with_text))

   def make_image_with_text(self):
      result_img = QImage(1000, 600, QImage.Format_ARGB32)
      painter = QPainter()
      painter.begin(result_img)
      img = QImage(self.new_art.background_image)
      painter.drawImage(0, 0, img)
      painter.setFont(QFont("Calibri", 28))

      painter.drawText(235, 315, '{:<11}'.format(self.part))
      painter.drawText(235, 375, '{:<11}'.format(self.get_data()))
      painter.drawText(235, 440, '{:<11}'.format(self.nom_diameter))
      painter.drawText(235, 500, '{:<11}'.format(self.new_art.nom_length))
      painter.drawText(235, 563, '{:<11}'.format(self.new_art.artikul))
      painter.end()
      self.image_with_text = result_img
      self.ui.label.setPixmap(QPixmap.fromImage(result_img))
      return result_img

   def handle_print(self):
      self.save_param_to_img()
      self.print_image()
        #buttonReply = QMessageBox.information(self, 'Выпуск продукции.', "Печатать этикетку?",
         #                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
       # if buttonReply == QMessageBox.Yes:
           # self.print_image()
           # print('Yes clicked.')
      #  else:
            #print('No clicked.')
           # pass

   def show_print_dialog(self):
      dlg = QPrintDialog()
      dlg.show()

   def print_image(self):
      printer = QPrinter()
      self.setup_printer(printer)
      self.paint_printer(printer)

   def setup_printer(self, printer):
      printer.setOrientation(QPrinter.Portrait)
      printer.setFullPage(True)
      printer.setPaperSize(QSizeF(100, 60), QPrinter.Millimeter)

   def paint_printer(self, printer):
      painter = QPainter()
      painter.begin(printer)
      painter_rect = painter.viewport()
      image_size = self.image_with_text.size()
      image_size.scale(painter_rect.size(), Qt.KeepAspectRatio)
      painter.setViewport(painter_rect.x(), painter_rect.y(), image_size.width(), image_size.height())
      painter.setWindow(self.image_with_text.rect())
      painter.drawImage(0, 0, self.image_with_text)
      painter.end()

   def print_image_to_pdf(self):
      printer = QPrinter()
      self.setup_printer_pdf(printer)
      self.paint_printer(printer)

   def setup_printer_pdf(self, printer):
      printer.setOutputFormat(QPrinter.PdfFormat)
      printer.setOutputFileName("output.pdf")
      printer.setOrientation(QPrinter.Portrait)
      printer.setFullPage(True)
      printer.setPaperSize(QSizeF(100, 60), QPrinter.Millimeter)

   def get_data(self):
      x = time.strftime("%d.%m.%y")
      return x

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
