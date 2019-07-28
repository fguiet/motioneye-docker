import datetime
import RPi.GPIO as GPIO
from astral import Astral
import pytz

a = Astral()
city = a['Paris']

tz = pytz.timezone('Europe/Paris')

sun = city.sun(date=datetime.datetime.now(tz), local=True)

if (datetime.datetime.now(tz) > sun['dusk'] or datetime.datetime.now(tz) < sun['dawn']):
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(18, GPIO.OUT)
   GPIO.output(18, GPIO.LOW)
   print " Night mode"

if (datetime.datetime.now(tz) > sun['dawn'] and datetime.datetime.now(tz) < sun['dusk']):
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(18, GPIO.OUT)
   GPIO.output(18, GPIO.HIGH)
   print " Day mode" 
   

print('Datetime now: %s' % str(datetime.datetime.now(tz)))
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))
