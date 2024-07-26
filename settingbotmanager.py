from PyQt5.QtWidgets import QApplication, QMainWindow ,QFileDialog,QMessageBox
from ui.settingbotmanagerui import Ui_MainWindow
import sys,configparser
from ftplib import FTP

class SettingWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.savesetting)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.openpathproduct)
        self.pushButton_3.clicked.connect(self.openpathdatabase)
        self.pushButton_5.clicked.connect(self.restoredb)
        self.loadsetting()
    def openpathproduct(self):
        pathproduct = QFileDialog.getExistingDirectory(None, "محل ذخیره ی محصولات")
        self.lineEdit_4.setText(pathproduct)
    def openpathdatabase(self):
        pathdb = QFileDialog.getExistingDirectory(None, "محل ذخیره ی دیتابیس")
        self.lineEdit_5.setText(pathdb)
    def restoredb(self):
        reply = QMessageBox.question(self, 'مطمئنید؟', 'با اینکار در صورت وجود دیتابیس، قبلی پاک میشه.',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                ftp = FTP(ftp_server)
                ftp.set_pasv(True)  # Enable passive mode
                try:
                    ftp.login(ftpusername, ftppassword)
                except Exception as e:
                    print(e)
                local_file_name = itemdbpath+'/''item.db'
                remote_file = '/'+local_file_name
                with open(local_file_name, 'wb') as file:
                    ftp.retrbinary('RETR ' + remote_file, file.write)
                    print('Done!')
                QMessageBox.information(None,"موفق","بازنشانی فایل با موفقیت انجام شد.")
                ftp.quit()
            except Exception:
                QMessageBox.critical(None,"خطا","لطفا اطلاعات ftp یا دسترسی به اینترنت را چک کنید.")
        else:
            pass
    def loadsetting(self):
        global ftpusername,ftppassword,ftp_server,itemdbpath
        config = configparser.ConfigParser()
        config.read('config.ini')
        theme = config.getint('bot_settings', 'theme')
        apitoken = config.get('bot_settings', 'Apitoken')
        chatid = config.get('bot_settings', 'ChatId')
        savedirpath = config.get('bot_settings','path')
        proxyadd = config.get('bot_settings','proxyaddress')
        proxytype = config.get('bot_settings','proxytype')
        itemdbpath = config.get('bot_settings','itemdbpath')
        ftpusername = config.get('bot_settings','ftpusername')
        ftppassword = config.get('bot_settings','ftppassword')
        ftp_server = config.get('bot_settings','ftpserver')
        self.comboBox.setCurrentIndex(int(theme))
        self.lineEdit_2.setText(apitoken)
        self.lineEdit_3.setText(chatid)
        self.lineEdit_4.setText(savedirpath)
        self.lineEdit.setText(proxyadd)
        self.comboBox_2.setCurrentIndex(int(proxytype))
        self.lineEdit_5.setText(itemdbpath)
        self.lineEdit_6.setText(ftpusername)
        self.lineEdit_7.setText(ftppassword)
        self.lineEdit_8.setText(ftp_server)

    def savesetting(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('bot_settings','theme',str(self.comboBox.currentIndex()))
        config.set('bot_settings','Apitoken',self.lineEdit_2.text())
        config.set('bot_settings','ChatId',self.lineEdit_3.text())
        config.set('bot_settings','path',self.lineEdit_4.text())
        config.set('bot_settings','proxytype',str(self.comboBox_2.currentIndex()))
        config.set('bot_settings','proxyaddress',self.lineEdit.text())
        config.set('bot_settings','itemdbpath',self.lineEdit_5.text())
        config.set('bot_settings','ftpusername',self.lineEdit_6.text())
        config.set('bot_settings','ftppassword',self.lineEdit_7.text())
        config.set('bot_settings','ftpserver',self.lineEdit_8.text())
        with open('config.ini','w') as f:
            config.write(f)
        QMessageBox.information(None,"موفق","تنظیمات با موفقیت ثبت شد، یک بار برنامه را ریست کنید.")
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SettingWindow()
    window.show()
    sys.exit(app.exec_())
    '''
#apitoken = 7205860012:AAF2myp11Rxm9jLIXZlFwzHX_cb78V_Zfxs
#chatid = 1979998539
'''
