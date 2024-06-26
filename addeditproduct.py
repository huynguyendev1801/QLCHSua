# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addeditproduct.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditProduct(object):
    def setupUi(self, AddEditProduct):
        AddEditProduct.setObjectName("AddEditProduct")
        AddEditProduct.resize(1000, 550)
        AddEditProduct.setStyleSheet("QLineEdit{\n"
"border-radius: 15px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(40, 42, 48);\n"
"height: 30px;\n"
"}\n"
"QLabel{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 100px;\n"
"}\n"
"QWidget#AddEditProduct{\n"
"background-color: rgb(242, 242, 248);\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(AddEditProduct)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 181, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.QVBLQL = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.QVBLQL.setContentsMargins(0, 0, 0, 0)
        self.QVBLQL.setSpacing(50)
        self.QVBLQL.setObjectName("QVBLQL")
        self.QLProductId = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductId.setObjectName("QLProductId")
        self.QVBLQL.addWidget(self.QLProductId)
        self.QLProductName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductName.setObjectName("QLProductName")
        self.QVBLQL.addWidget(self.QLProductName)
        self.QLProductProducer = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductProducer.setObjectName("QLProductProducer")
        self.QVBLQL.addWidget(self.QLProductProducer)
        self.QLProductCS = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductCS.setObjectName("QLProductCS")
        self.QVBLQL.addWidget(self.QLProductCS)
        self.QLProductPrice = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductPrice.setObjectName("QLProductPrice")
        self.QVBLQL.addWidget(self.QLProductPrice)
        self.QLProductNumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QLProductNumber.setObjectName("QLProductNumber")
        self.QVBLQL.addWidget(self.QLProductNumber)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(AddEditProduct)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 371, 444))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.QVBLQLE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.QVBLQLE.setContentsMargins(0, 0, 0, 0)
        self.QVBLQLE.setSpacing(50)
        self.QVBLQLE.setObjectName("QVBLQLE")
        self.QLEProductId = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.QLEProductId.setObjectName("QLEProductId")
        self.QVBLQLE.addWidget(self.QLEProductId)
        self.QLEProductName = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.QLEProductName.setObjectName("QLEProductName")
        self.QVBLQLE.addWidget(self.QLEProductName)
        self.QLEProductProducer = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.QLEProductProducer.setObjectName("QLEProductProducer")
        self.QVBLQLE.addWidget(self.QLEProductProducer)
        self.QLEProductCS = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.QLEProductCS.setObjectName("QLEProductCS")
        self.QVBLQLE.addWidget(self.QLEProductCS)
        self.QLEProductPrice = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.QLEProductPrice.setObjectName("QLEProductPrice")
        self.QVBLQLE.addWidget(self.QLEProductPrice)
        self.QSBProductNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.QSBProductNumber.setStyleSheet("border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(40, 42, 48);\n"
"height: 30px;")
        self.QSBProductNumber.setMinimum(1)
        self.QSBProductNumber.setMaximum(1000)
        self.QSBProductNumber.setProperty("value", 1)
        self.QSBProductNumber.setObjectName("QSBProductNumber")
        self.QVBLQLE.addWidget(self.QSBProductNumber)
        self.QLProduct = QtWidgets.QLabel(AddEditProduct)
        self.QLProduct.setGeometry(QtCore.QRect(0, 30, 181, 31))
        self.QLProduct.setObjectName("QLProduct")
        self.QLProductImage = QtWidgets.QLabel(AddEditProduct)
        self.QLProductImage.setGeometry(QtCore.QRect(650, 80, 300, 300))
        self.QLProductImage.setScaledContents(True)
        self.QLProductImage.setAlignment(QtCore.Qt.AlignCenter)
        self.QLProductImage.setOpenExternalLinks(False)
        self.QLProductImage.setObjectName("QLProductImage")
        self.QPBUpLoadProductImage = QtWidgets.QPushButton(AddEditProduct)
        self.QPBUpLoadProductImage.setGeometry(QtCore.QRect(725, 420, 150, 40))
        self.QPBUpLoadProductImage.setMinimumSize(QtCore.QSize(110, 0))
        self.QPBUpLoadProductImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.QPBUpLoadProductImage.setStyleSheet("height: 40px;\n"
"border-radius: 20px;\n"
"background-color: rgb(139, 233, 253);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon/addemployeeimage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPBUpLoadProductImage.setIcon(icon)
        self.QPBUpLoadProductImage.setIconSize(QtCore.QSize(25, 25))
        self.QPBUpLoadProductImage.setObjectName("QPBUpLoadProductImage")
        self.QPBSaveProduct = QtWidgets.QPushButton(AddEditProduct)
        self.QPBSaveProduct.setGeometry(QtCore.QRect(725, 480, 150, 40))
        self.QPBSaveProduct.setMinimumSize(QtCore.QSize(110, 0))
        self.QPBSaveProduct.setFocusPolicy(QtCore.Qt.TabFocus)
        self.QPBSaveProduct.setStyleSheet("height: 40px;\n"
"border-radius: 20px;\n"
"background-color: rgb(80, 250, 123);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon/saveemployee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPBSaveProduct.setIcon(icon1)
        self.QPBSaveProduct.setIconSize(QtCore.QSize(20, 20))
        self.QPBSaveProduct.setObjectName("QPBSaveProduct")

        self.retranslateUi(AddEditProduct)
        QtCore.QMetaObject.connectSlotsByName(AddEditProduct)

    def retranslateUi(self, AddEditProduct):
        _translate = QtCore.QCoreApplication.translate
        AddEditProduct.setWindowTitle(_translate("AddEditProduct", "Form"))
        self.QLProductId.setText(_translate("AddEditProduct", "Mã sữa:"))
        self.QLProductName.setText(_translate("AddEditProduct", "Tên sữa:"))
        self.QLProductProducer.setText(_translate("AddEditProduct", "Tên công ty sản xuất:"))
        self.QLProductCS.setText(_translate("AddEditProduct", "Quy cách hàng hóa"))
        self.QLProductPrice.setText(_translate("AddEditProduct", "Đơn giá"))
        self.QLProductNumber.setText(_translate("AddEditProduct", "Số lượng:"))
        self.QLProduct.setText(_translate("AddEditProduct", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sản phẩm</span></p></body></html>"))
        self.QLProductImage.setText(_translate("AddEditProduct", "<html><head/><body><p><span style=\" font-size:18pt;\">Ảnh</span></p></body></html>"))
        self.QPBUpLoadProductImage.setText(_translate("AddEditProduct", "Tải ảnh lên"))
        self.QPBSaveProduct.setText(_translate("AddEditProduct", "Lưu"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEditProduct = QtWidgets.QWidget()
    ui = Ui_AddEditProduct()
    ui.setupUi(AddEditProduct)
    AddEditProduct.show()
    sys.exit(app.exec_())
