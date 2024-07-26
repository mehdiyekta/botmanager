import sys,os,subprocess,sqlite3,asyncio,configparser,aiofiles,random,csv
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication , QMainWindow ,QFileDialog,QTableWidgetItem,QMessageBox
from ui.botmanagerui import Ui_MainWindow
from telegram.ext import Application
from ftplib import FTP

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listpreview.setAcceptDrops(True)
        self.listfileid.setAcceptDrops(True)
        self.pushButton_5.clicked.connect(self.openpreviewfile)
        self.pushButton_7.clicked.connect(self.openforfileid)
        self.pushButton_6.clicked.connect(self.removefileidpreview)
        self.pushButton_8.clicked.connect(self.removefileidfile)
        self.pushButton_3.clicked.connect(self.close)
        self.action_8.triggered.connect(self.opensetting)
        self.action_4.triggered.connect(self.openpreviewfile)
        self.action_5.triggered.connect(self.openforfileid)
        self.action_7.triggered.connect(self.close)
        self.action_3.triggered.connect(self.pushButton_2.click)
        self.pushButton_11.clicked.connect(self.addtotable)
        self.lineEdit_3.textChanged.connect(self.changetokentorial)
        self.lineEdit_4.textChanged.connect(self.changerialtotoken)
        self.pushButton_4.clicked.connect(self.randomnumber)
        self.pushButton_9.clicked.connect(self.submitdata)
        self.pushButton_10.clicked.connect(self.ftpdb)
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
    def ftpdb(self):
        # Create an FTP object and connect to the server
        ftp = FTP(ftp_server)
        ftp.set_pasv(True)  # Enable passive mode
        try:
            ftp.login(username, password)
        except Exception as e:
            print(e)
        local_file_name = 'item.db'
        local_file = pathitemdb +'/'+'item.db'
        remote_file = '/'+local_file_name
        with open(local_file, 'rb') as file:
            ftp.storbinary('STOR ' + remote_file, file)
            print('Done!')
        ftp.quit()
        QMessageBox.information(None,"موفق","آپلود به سرور موفقیت آمیز بود.")
    def senddataserver(self):
        ftp = FTP(ftp_server)
        ftp.set_pasv(True)  # Enable passive mode
        try:
            ftp.login(username, password)
        except Exception as e:
            print(e)
        local_file_name = 'item.db'
        local_file = pathitemdb+'item.db'
        remote_file = '/'+local_file_name
        with open(local_file, 'wb') as file:
            ftp.retrbinary('RETR ' + remote_file, file.write)
            print('Done!')
        ftp.quit()


    def submitdata(self):
        filename = self.lineEdit.text()
        filecode = self.lineEdit_2.text()
        token = self.lineEdit_3.text()
        token = round(float(token))
        price = self.lineEdit_4.text()
        description = self.textEdit.toPlainText()
        folder_name = savedirpath+'/'+filename+'- '+str(token)+' توکن'
        os.mkdir(folder_name)
        previewpath = folder_name+'/preview'
        os.mkdir(previewpath)
        if self.listfileid.count()==0:
            QMessageBox.critical(None,"خطای فایل اصلی","فایل اصلی جهت ارسال به بات یافت نشد")
        else:
            listfileid = [self.listfileid.item(i).text() for i in range(self.listfileid.count())]
            listfileid.append(token)
            listfileid.append(filecode)
            with open (folder_name+'/'+'productinfo.csv','w',newline='', encoding='utf-8') as productfile:
                    writer = csv.writer(productfile)
                    writer.writerow(listfileid)
        listphotoid = [self.listpreview.item(i).text() for i in range(self.listpreview.count())]
        with open(previewpath+'/'+'preview.txt','w',encoding='utf-8') as previewfile:
            for photoid in listphotoid:
                previewfile.writelines(photoid)
                previewfile.writelines('\n')


    def randomnumber(self):
        rnd=[]
        rndnumber = random.randint(100, 999)
        rnd.append(rndnumber)
        cursor.execute('''SELECT itemcode FROM item''')
        itemcodes = cursor.fetchall()
        if itemcodes in rnd:
            rndnumber=random.randint(100,999)
        else:
            self.lineEdit_2.setText(str(rndnumber))
    def changetokentorial(Self):
        try:
            Self.lineEdit_4.blockSignals(True)
            token = Self.lineEdit_3.text()
            rial = int(token)*100
            Self.lineEdit_4.setText(str(rial))
            Self.lineEdit_4.blockSignals(False)
        except Exception as e:
            print(e)
            pass
    def changerialtotoken(self):
        try:
            self.lineEdit_3.blockSignals(True)
            rial = self.lineEdit_4.text()
            token = int(rial)/100
            token = str(round(float(token)))
            self.lineEdit_3.setText(str(token))
            self.lineEdit_3.blockSignals(False)
        except Exception:
            pass

    def openpreviewfile(self):
        file_name, _ = QFileDialog.getOpenFileName()
        photo_id = asyncio.run(self.send_photo(file_name))
        self.listpreview.addItem(photo_id)
    def openforfileid(self):
        file_name, _ = QFileDialog.getOpenFileName()
        file_id = asyncio.run(self.send_file(file_name))
        self.listfileid.addItem(file_id)
    def removefileidpreview(self):
        selected_items = self.listpreview.selectedItems()
        if selected_items:
            for item in selected_items:
                self.listpreview.takeItem(self.listpreview.row(item))
    def removefileidfile(self):
        selected_items = self.listfileid.selectedItems()
        if selected_items:
            for item in selected_items:
                self.listfileid.takeItem(self.listfileid.row(item))
    def addtotable(self):
        datas=[]
        #code
        datas.append(self.lineEdit_2.text())
        #filename
        datas.append(self.lineEdit.text())
        #price(token)/price(toman)
        datas.append(self.lineEdit_3.text())
        datas.append(self.lineEdit_4.text())
        if self.listpreview.count()==0:
            have_preview='❌'
        else:
            have_preview='✅'
        datas.append(have_preview)
        datas.append(self.textEdit.toPlainText())
        datatoshow.append(datas)
        self.tableWidget.setRowCount(len(datatoshow))
        for row,data in enumerate(datatoshow):
            for column ,item in enumerate(data):
                self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
        itemcode = self.lineEdit_2.text()
        itemname = self.lineEdit.text()
        itemdescrib = self.textEdit.toPlainText()
        cursor.execute('''INSERT OR IGNORE INTO item (itemcode,itemname,itemdesctiption) VALUES(?,?,?) ''',(itemcode,itemname,itemdescrib))
        conn.commit()
    async def send_file(self,file_path)->str:
        # Open the photo file in binary mode
        async with aiofiles.open(file_path, "rb") as f:
            # Read the file contents
            file_data = await f.read()
        try:
            # Send the photo to the bot
            message = await application.bot.send_document(chat_id=chatid, document=open(file_path,'rb'))
            # Get the file ID from the message
            file_id = message.document.file_id
            print(f"File ID: {file_id}")
            return file_id
        except Exception as e:
            print(f"Error sending file: {e}")
            print("ReTrying...")
            await self.send_file()
    async def send_photo(self,photo_path)->str:
        async with aiofiles.open(photo_path, "rb") as f:
            photo_data = await f.read()
        try:
            # ersal ax be robot
            message = await application.bot.send_photo(chat_id=chatid, photo=photo_data)
            # daryaft file_id
            file_id = message.photo[-1].file_id
            print(f"File ID: {file_id}")
            return file_id
        except Exception as e:
            print(f"Error sending photo: {e}")
            print("ReTrying...")
            await self.send_photo()
    def opensetting(self):

        subprocess.run(["python", settingpath])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                filePath = str(url.toLocalFile())
                # Check which list widget the file was dropped onto
                if self.listpreview.underMouse():
                    try:
                        file_id=asyncio.run(self.send_photo(filePath))
                        self.listpreview.addItem(file_id)
                    except Exception as e:
                        file_id=asyncio.run(self.send_photo(filePath))
                        self.listpreview.addItem(file_id)
                elif self.listfileid.underMouse():
                    try:
                        file_id=asyncio.run(self.send_file(filePath))
                        self.listfileid.addItem(file_id)
                    except Exception as e:
                        file_id=asyncio.run(self.send_file(filePath))
                        self.listfileid.addItem(file_id)
        else:
            event.ignore()

if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    theme = config.getint('bot_settings', 'theme')
    apitoken = config.get('bot_settings', 'Apitoken')
    chatid = config.get('bot_settings', 'ChatId')
    savedirpath = config.get('bot_settings','path')
    proxyadd = config.get('bot_settings','proxyaddress')
    proxytype = config.get('bot_settings','proxytype')
    timeout = config.getint('bot_settings','timeout')
    pathitemdb = config.get('bot_settings','itemdbpath')
    username = config.get('bot_settings','ftpusername')
    password = config.get('bot_settings','ftppassword')
    ftp_server = config.get('bot_settings','ftpserver')
    application = Application.builder().token(apitoken).connect_timeout(6000).read_timeout(6000).write_timeout(6000).build()
    apppath =os.path.dirname(os.path.abspath(__file__))
    settingpath = apppath+'/'+'settingbotmanager.py'
    datatoshow = []
    conn = sqlite3.connect(pathitemdb+'/'+'item.db')
    cursor= conn.cursor()
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
