# The Project Code ↓↓
import time
from multiprocessing import Value
import MLX90614
import RPi.GPIO as GPIO
from mfrc522 import MyMFRC522


class RaspberryController():
    def __init__(self, interrupt):
        GPIO.setmode(GPIO.BCM)
        self.nfc_reader = MyMFRC522(interrupt)
        self.interrupt = interrupt

    def __del__(self):
        GPIO.cleanup()

    def getNFCId(self):
        try:
            id = self.nfc_reader.read_id()
        finally:
            pass
        return id

    def getTemp(self):
        temp_sensor = MLX90614.MLX90614()
        total = 0
        n = 4
        while(self.getDistance() >= 8.0):
            time.sleep(0.2)
        for i in range(n):
            total += float(temp_sensor.get_obj_temp())
            if(self.interrupt.value):
                return 'INTERRUPTED'
            time.sleep(0.5)
        return round(total / n, 2)

    def getDistance(self):
        trig = 5
        echo = 6
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

        time.sleep(0.2)
        GPIO.output(trig, 1)
        time.sleep(0.00001)
        GPIO.output(trig, 0)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        return distance

# For Test Code ↓↓
# import time
# import random
# from multiprocessing import Value

# class RaspberryController():
#     def __init__(self, interrupt):
#         self.interrupt = interrupt

#     def getNFCId(self):
#         nfc_numbers = [584187407785, 584186083456, 584184898698, 584183666907]
#         return random.choice(nfc_numbers)

#     def getTemp(self):
#         total = 0
#         n = 4
#         while(self.getDistance() >= 8.0):
#             time.sleep(0.2)
#         for i in range(n):
#             total += float(random.uniform(36.0, 38.5))
#             if(self.interrupt.value):
#                 return 'INTERRUPTED'
#             time.sleep(0.5)
#         return round(total / n, 2)

#     def getDistance(self):
#         return 2.0


if __name__ == '__main__':
    v = Value('b', False)
    con = RaspberryController(v)
    print(con.getNFCId())
    print(con.getTemp())
    print(con.getDistance())
