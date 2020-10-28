import sys, time
from multiprocessing import Process, Queue, Value
from threading import Thread
import RasberryController
import DataController

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
    ↓ Header Widget
'''
class HeaderWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.init_widget()

    def init_widget(self):
        # define layout
        self.header_layout = QHBoxLayout() # Header 부분을 이룰 QHBoxLayout 이다.
        self.setLayout(self.header_layout)

        # define label
        self.header_label = QLabel("SSU CORONA PROJECT")

        # add components
        self.header_layout.addWidget(self.header_label) #header 레이아웃에 라벨을 달아준다.

        # set styles
        self.color1 = QColor(0,0,255)
        self.color2 = QColor(0,0,255)
        self.header_label_style = 'font-size:28px; font-family:Arial; font-weight:bold; color: white; margin-top: 20px; margin-bottom:20px; padding: 10px 0px;'
        self.header_label.setStyleSheet(self.header_label_style)
        self.header_label.setAlignment(Qt.AlignRight)

        #set animation
        self.animation = QVariantAnimation(self, valueChanged=self.animate, startValue=0.00001, endValue=1.0, duration=1000)
        
        # set background color
        self.setBackgroundColor()

    def animate(self, value):
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        self.header_label.setStyleSheet(self.header_label_style + grad)

    # do animation effect
    def animationStart(self):
        self.animation.setDirection(QAbstractAnimation.Forward)
        self.animation.start()

    #color must be QColor(r,g,b) type
    def setBackgroundColor(self,color1=None, color2=None):
        if(color1 != None):
            self.color1 = color1
        if(color2 != None):
            self.color2 = color2
        self.animationStart()

'''
    ↓ Initial Widget
'''
class InitialWidget(QGroupBox):
    def __init__(self, eventHandler):
        super().__init__()
        self.eventHandler = eventHandler

        self.init_widget()
    
    def init_widget(self):
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.box = QHBoxLayout()
        self.layout.addRow(self.box)

        # style
        self_style = 'background:white;'
        self.setStyleSheet(self_style)
        self.box.setAlignment(Qt.AlignCenter)
        label_style = 'border'

        # define label
        self.label = QLabel()
        pixmap = QPixmap('./resources/logo_black.png').scaled(400, 400)
        self.label.setPixmap(pixmap)
        self.mousePressEvent = lambda e : self.eventHandler('init')

        # add Component
        self.box.addWidget(self.label)

'''
    ↓ Menu Widget
'''
class MenuWidget(QGroupBox):
    def __init__(self, menus, eventHandler):
        super().__init__()

        self.menus = menus
        self.eventHandler = eventHandler

        self.init_widget()

    def init_widget(self):
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.box = QHBoxLayout()
        self.header = HeaderWidget()

        self.layout.addRow(self.header)
        self.layout.addRow(self.box)
        
        buttonStyle = "height : 300px; \
            border-width:5px; border-color:blue; border-radius: 10px; border-style:solid; \
            background: white; \
            font-size: 30px; font-weight: bold; font-family: 맑은 고딕;"

        #define button
        for menu in (self.menus):
            btn = QPushButton(menu['menu_name'])
            btn.setStyleSheet(buttonStyle)
            handler_name = menu['menu_event_name']
            btn.clicked.connect(lambda ch, handler_name=handler_name: self.eventHandler(handler_name))
            self.box.addWidget(btn)

        #style
        self.setStyleSheet("background: white;")
        self.header.setBackgroundColor(QColor(0,0,255), QColor(0,0,255))


'''
    ↓ NFC Wating Widget
'''
class NFCWatingWidget(QGroupBox):
    def __init__(self, menus, eventHandler):
        super().__init__()
        self.menus = menus
        self.eventHandler = eventHandler

        self.init_widget()
    
    def init_widget(self):
        # define layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.gif_box = QVBoxLayout()
        self.button_box = QHBoxLayout()
        self.header = HeaderWidget()

        # add sub-layout to layout
        self.layout.addRow(self.header)
        self.layout.addRow(self.gif_box)
        self.layout.addRow(self.button_box)

        # style
        self_style = 'background: white;'
        self.setStyleSheet(self_style)
        button_style = 'font-size: 20px; font-family:맑은 고딕; font-weight: bold; border-width:2px; border-style:solid; border-color:blue; padding: 5px 0;'

        # define components
        self.label = QLabel('하단의 리더기에 카드를 접촉해주십시오')
        self.gif_box.addWidget(self.label)

        for menu in (self.menus):
            btn = QPushButton(menu['menu_name'])
            btn.setStyleSheet(button_style)
            handler_name = menu['menu_event_name']
            btn.clicked.connect(lambda ch, handler_name=handler_name: self.eventHandler(handler_name))
            self.button_box.addWidget(btn)

    # set status message
    def setStatus(self, status=None):
        if(status == None):
            self.label.setText('하단의 리더기에 카드를 접촉해주십시오')
        else:    
            self.label.setText(status)

'''
    ↓ TempWidget
'''
class TempWidget(QGroupBox):
    def __init__(self, eventHandler):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)

        # define label
        self.name = QLabel('이름과 소속')
        self.temp = QLabel('체온')
        self.status = QLabel('확인중입니다')
        self.cancelButton = QPushButton('뒤로가기')

        # event 
        self.cancelButton.clicked.connect(lambda : eventHandler('userMenu_cancel'))

        # alignment
        self.name.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.status.setAlignment(Qt.AlignCenter)

        # style
        labelStyle = "background: white; font-size: 25px; font-family: 맑은 고딕; border-width:3px; border-style:solid; border-color:black;"
        self.name.setStyleSheet(labelStyle)
        self.temp.setStyleSheet(labelStyle)
        self.status.setStyleSheet(labelStyle)

        # add labels to box
        self.box.addWidget(self.name)
        self.box.addWidget(self.temp)
        self.box.addWidget(self.status)
        self.box.addWidget(self.cancelButton)

    def setName(self, name):
        self.name.setText(name)
    
    def setTemp(self, temperature):
        self.temp.setText(temperature)
    
    def setStatus(self, status):
        self.status.setText(status)

    def clear(self):
        self.setName('')
        self.setTemp('')
        self.setStatus('')

'''
    ↓ AdminAdd Widget
'''
class AdminAddWidget(QGroupBox):
    def __init__(self, eventHandler):
        QGroupBox.__init__(self)
        self.box = QFormLayout()
        self.setLayout(self.box)
        self.setTitle("멤버 추가")

        # define widgets
        self.nfcIdLabel = QLabel('NFC ID : ')
        self.nfcIdEditor = QLineEdit()
        self.nameLabel = QLabel('이름 : ')
        self.nameEditor = QLineEdit()
        self.belongLabel = QLabel('소속 : ')
        self.belongEditor = QLineEdit()
        self.statusLabel = QLabel('')

        self.cancelButton = QPushButton('뒤로가기')
        self.addButton = QPushButton('추가하기')
        horizonLayout = QHBoxLayout()
        horizonLayout.addWidget(self.cancelButton)
        horizonLayout.addWidget(self.addButton)

        # event handle
        self.cancelButton.clicked.connect(lambda :eventHandler('adminAdd_cancel'))
        self.addButton.clicked.connect(lambda : eventHandler('adminAdd_add', self.getElements()))

        # define style
        self.box.setContentsMargins(40, 100, 40, 0)
        labelStyle = "font-size:20px;font-family: 맑은 고딕;"
        statusLabelStyle = labelStyle + "height:30px;"
        editorStyle = "font-size:20px;font-family: 맑은 고딕;"
        buttonStyle = "margin-top:90px; height: 50px; font-size:20px; font-family: 맑은 고딕;"

        # label style
        self.nfcIdLabel.setStyleSheet(labelStyle)
        self.nameLabel.setStyleSheet(labelStyle)
        self.belongLabel.setStyleSheet(labelStyle)

        # status label style
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet(statusLabelStyle)

        # editor style
        self.nfcIdEditor.setStyleSheet(editorStyle)
        self.nameEditor.setStyleSheet(editorStyle)
        self.belongEditor.setStyleSheet(editorStyle)
        
        #button style
        self.cancelButton.setStyleSheet(buttonStyle)
        self.addButton.setStyleSheet(buttonStyle)

        # add widgets to box
        self.box.addRow(self.nfcIdLabel, self.nfcIdEditor)
        self.box.addRow(self.nameLabel, self.nameEditor)
        self.box.addRow(self.belongLabel, self.belongEditor)
        self.box.addRow(horizonLayout)
        self.box.addRow(self.statusLabel)

    # set nfc id
    def setNFCID(self, id):
        self.nfcIdEditor.setText(str(id))

    # set name
    def setName(self, name):
        self.nameEditor.setText(str(name))

    # set belong
    def setBelong(self, belong):
        self.belongEditor.setText(str(belong))

    # set status label
    def setStatus(self, text):
        self.statusLabel.setText(str(text))

    # get text of all line editor
    def getElements(self):
        target = {}
        target['nfcId'] = self.nfcIdEditor.text()
        target['name'] = self.nameEditor.text()
        target['belong'] = self.belongEditor.text()
        return target

    # clear all label and lineEditor
    def clear(self):
        self.setNFCID('')
        self.setName('')
        self.setBelong('')
        self.setStatus('')
    

'''
    ↓ Thread Worker Class
'''
class Worker(QThread):
    new_signal = pyqtSignal(dict)

    def __init__(self, responseQ):
        super().__init__()
        self.responseQ = responseQ

    def run(self):
        while(True):
            time.sleep(1)
            if(self.responseQ.qsize()>0):
                item = self.responseQ.get()
                self.new_signal.emit(item)

'''
    ↓ Widgets Controller
'''
class View(QWidget):
    def __init__(self, requestQ, responseQ, interrupt, isReady):
        QWidget.__init__(self, flags=Qt.Widget)

        # props initialize
        self.requestQ = requestQ
        self.responseQ = responseQ
        self.interrupt = interrupt
        self.isReady = isReady

        # window initialize
        self.resize(700,450)
        self.widgetsList = {}
        self.widgetStack = QStackedWidget(self)
        self.init_widget()
        self.toCenter()
        self.show()

        # thread
        self.worker = Worker(self.responseQ)
        self.worker.new_signal.connect(self.responseHandler)
        self.worker.start()
    
    @pyqtSlot(dict)
    def responseHandler(self, item):
        if(item['type'] == 'GET_NAME'):
            if(item['name'] == None):
                self.nfcWaitingWidget.setStatus('저장돼있지 않은 카드입니다')
                self.nfcWaitingWidget.header.setBackgroundColor(QColor(255,0,0), QColor(0,0,255))
            elif(item['name'] == 'INTERRUPTED'):
                self.interrupt.value = False # set interrupt as False
                return
            else:
                self.tempWidget.setName(item['name'])
                self.tempWidget.setStatus('손목을 온도센서에 가까이 대주세요')
                self.requestQ.put({'type':'GET_TEMP'})

        elif(item['type'] == 'GET_TEMP'):
                if(item['temp'] == 'INTERRUPTED'):
                    self.interrupt.value = False # set interrupt as False
                    return
                self.tempWidget.setTemp(str(item['temp']))
                if(item['temp'] > 37.5):
                    self.tempWidget.setStatus('체온이 높습니다. 보건실에 방문해주세요.')
                else:
                    self.tempWidget.setStatus('정상 체온입니다.')
        
        elif(item['type'] == 'USER_RE_INIT'):
            self.nfcWaitingWidget.setStatus()
            self.nfcWaitingWidget.header.setBackgroundColor(QColor(0,0,255),QColor(0,0,255))
            self.changeWidget('nfcWaitingWidget')
            # self.tempWidget.clear()
            # self.tempWidget.setStatus('NFC 카드를 대주세요.')
            self.requestQ.put({'type':'GET_NAME'})

        elif(item['type']=='GET_NFCID'):
            id = item['nfcId']
            if(id == None):
                self.adminAddWidget.setStatus('NFC 카드를 인식하지 못했습니다.')
            elif(id == 'INTERRUPTED'):
                self.interrupt.value = False # set interrupt as False
                return
            else:
                self.adminAddWidget.setNFCID(id)
                self.adminAddWidget.setStatus('NFC 카드 인식에 성공했습니다.')

        elif(item['type']=='ADD_USER'):
            if(item['result']):
                self.adminAddWidget.setStatus('저장에 성공했습니다')
            else:
                self.adminAddWidget.setStatus('저장에 실패했습니다')
            self.interrupt.value = False # set interrupt as False

        elif(item['type']=='GET_USER_LIST'):
            data = item['result']
            self.adminDeleteWidget.setData(data)
            self.adminDeleteWidget.setStatus('표를 가져왔습니다.')
            self.interrupt.value = False # set interrupt as False
        

    # init widget
    def init_widget(self):
        self.setWindowTitle("IoT 체온 스캐너")
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(widget_laytout)

        self.initialWidget = InitialWidget(self.eventHandler)
        self.menuWidget = MenuWidget([{'menu_name': '디스플레이 모드', 'menu_event_name':'userMenu'},{'menu_name':'관리 모드', 'menu_event_name':'adminMenu'}], self.eventHandler)
        self.tempWidget = TempWidget(self.eventHandler)
        self.adminMenuWidget = MenuWidget([{'menu_name':'멤버 추가', 'menu_event_name':'adminAdd'}], self.eventHandler)
        self.adminAddWidget = AdminAddWidget(self.eventHandler)
        self.nfcWaitingWidget = NFCWatingWidget([{'menu_name':'뒤로가기', 'menu_event_name':'userMenu_cancel'}], self.eventHandler)

        self.widgetStack.addWidget(self.initialWidget)
        self.widgetsList['initialWidget'] = 0

        self.widgetStack.addWidget(self.menuWidget)
        self.widgetsList['menuWidget'] = 1
        
        self.widgetStack.addWidget(self.tempWidget)
        self.widgetsList['tempWidget'] = 2
        
        self.widgetStack.addWidget(self.adminMenuWidget)
        self.widgetsList['adminMenuWidget'] = 3

        self.widgetStack.addWidget(self.adminAddWidget)
        self.widgetsList['adminAddWidget'] = 4

        self.widgetStack.addWidget(self.nfcWaitingWidget)
        self.widgetsList['nfcWaitingWidget'] = 5

        widget_laytout.addWidget(self.widgetStack)
        # self.changeWidget('menuWidget')
        self.changeWidget('initialWidget')

    # move window to center point of display
    def toCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # change displayed widget
    def changeWidget(self, target):
        self.widgetStack.setCurrentIndex(self.widgetsList[target])

    # event handle that causes widgets
    def eventHandler(self, kind, params=None):
        if(kind == 'init'):
            self.changeWidget('menuWidget')

        elif(kind == 'userMenu'):
            self.nfcWaitingWidget.header.setBackgroundColor(QColor(0,0,255), QColor(0,0,255))
            self.changeWidget('nfcWaitingWidget')
            self.requestQ.put({'type':'GET_NAME'})

            # self.tempWidget.clear()
            # self.tempWidget.setStatus('NFC 카드를 대주세요.')
            # self.changeWidget('tempWidget')
            # self.requestQ.put({'type':'GET_NAME'})

        elif(kind == 'userMenu_cancel'):
            if(self.isReady.value == False): # if background is running
                self.interrupt.value = True # interrupt signal
                while(self.isReady.value == False): # wait
                    time.sleep(0.2)
            self.changeWidget('menuWidget')

        elif(kind == 'adminMenu'):
            self.changeWidget('adminMenuWidget')
        
        elif(kind == 'adminAdd'):
            self.adminAddWidget.clear()
            self.adminAddWidget.setStatus('NFC 카드를 대주세요.')
            self.changeWidget('adminAddWidget')
            self.requestQ.put({'type':'GET_NFCID'})
        
        elif(kind == 'adminAdd_cancel'):
            if(self.isReady.value == False): # if background is running
                self.interrupt.value = True # interrupt signal
                while(self.isReady.value == False): # wait
                    time.sleep(0.2)
            self.adminAddWidget.clear()
            self.adminAddWidget.setStatus('')
            self.changeWidget('adminMenuWidget')
        
        elif(kind == 'adminAdd_add'):
            self.adminAddWidget.setStatus('처리중입니다.')
            self.requestQ.put({'type':'ADD_USER', 'nfcId':params['nfcId'], 'name':params['name'], 'belong':params['belong']})

'''
    ↓ Handler Function for Background Process
'''
def Handler(requestQ, responseQ, interrupt, isReady):
    dataController = DataController.DataController(interrupt)
    id = None
    temp = None

    while(True):
        time.sleep(1)
        print('running')
        if(requestQ.qsize() > 0):
            item = requestQ.get()
            isReady.value = False #set flag false when working...

            # Get nfc id and name
            if(item['type'] == 'GET_NAME'):
                id = RasberryController.getNFCId(interrupt) # for propagation interrupt signal
                if(id == 'INTERRUPTED'):
                    responseQ.put({'type':'GET_NAME', 'name':id})
                else:
                    name = dataController.getNameByNFC(id)
                    responseQ.put({'type':'GET_NAME', 'name':name})
                    if(name == None):
                        time.sleep(3)
                        responseQ.put({'type':'USER_RE_INIT'})
            
            # Get temperature And Re init
            elif(item['type'] == 'GET_TEMP'):
                temp = RasberryController.getTemp(interrupt) # for propagation interrupt signal
                if(id != 'INTERRUPTED' and temp != 'INTERRUPTED'):
                    result = dataController.addTempData(id, temp)
                responseQ.put({'type':'GET_TEMP', 'temp':temp})
                time.sleep(2)
                responseQ.put({'type':'USER_RE_INIT'})

            elif(item['type']=='GET_NFCID'):
                id = RasberryController.getNFCId(interrupt) # for propagation interrupt signal
                responseQ.put({'type':'GET_NFCID', 'nfcId':id})

            elif(item['type']=='ADD_USER'):
                result = dataController.addUser(item['nfcId'], item['name'], item['belong'])
                responseQ.put({'type':'ADD_USER', 'result':result})

            elif(item['type']=='GET_USER_LIST'):
                result = dataController.getUserData()
                responseQ.put({'type':'GET_USER_LIST', 'result':result})
        
            isReady.value = True # set flag true when ready


if __name__ == "__main__":
    app = QApplication(sys.argv)
    requestQ = Queue()
    responseQ = Queue()
    interrupt = Value('b', False)
    isReady = Value('b', True)
    view = View(requestQ, responseQ, interrupt, isReady)

    background = Process(target=Handler, args=(requestQ, responseQ, interrupt, isReady), daemon=True)
    background.start()

    exit(app.exec_())