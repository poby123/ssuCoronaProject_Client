# ssuCoronaProject_Client
## Dependencies
```
~$ sudo apt-get update
~$ sudo apt-get upgrade
```
- GTTS (https://pypi.org/project/gTTS/)
```
~$ sudo apt-get install -y python3-gtts
```
- PyQt5 (https://pypi.org/project/PyQt5/)
```
~$ sudo apt-get install -y python3-pyqt5
```
- PyQt5.QtMultimedia
```
~$ sudo apt-get install -y python3-pyqt5.qtmultimedia
```

## Usage
- Install
```
~$ git clone https://github.com/poby123/ssuCoronaProject_Client
```

- Execute
```
~$ cd ssuCoronaProject_Client
~/ssuCoronaProject_Client$ python3 main.py
```
## spoon -bfly
- Note<br>
SPI통신과 일반 setmode의 차이로 2020.12.09 현재, RaspberryController.py의 11번째 줄 GPIO.setmode(GPIO.BCM) 이 부분을 주석처리하고 python3 RaspberryController.py를 실행했다가, 다시 주석을 풀고 python3 main.py를 실행해야한다.
이 과정은 라즈베리파이 부팅 후 한번만 거치면 되지만, 한 번도 하지 않을 경우, 아무런 경고메시지 없이 NFC 인식이 안되는 오류가 발생한다.
```
        GPIO.setmode(GPIO.BCM) # 이 부분
        self.nfc_reader = MyMFRC522(interrupt)
        self.interrupt = interrupt
```

## Software Structure
![설계도](https://user-images.githubusercontent.com/50279318/101590450-c819b780-3a2d-11eb-97af-759155aa3cef.png)

## Circuit
![회로도](https://user-images.githubusercontent.com/50279318/101590586-1464f780-3a2e-11eb-8bcc-bc56e32a3bf1.png)
## Frame Modeling
