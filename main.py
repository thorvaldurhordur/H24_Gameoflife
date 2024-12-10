from  machine import Pin, PWM, I2C, SoftI2C
from time import sleep_ms, time
from I2C_LCD import I2cLcd
from random import*
led_a= Pin(9, Pin.OUT)
led_b= Pin(11, Pin.OUT)
led_c= Pin(13, Pin.OUT)
led_d= Pin(8, Pin.OUT)
takki_a = Pin(10, Pin.IN, Pin.PULL_UP)
takki_b = Pin(12, Pin.IN, Pin.PULL_UP)
takki_c = Pin(17, Pin.IN, Pin.PULL_UP)
takki_d = Pin(18, Pin.IN, Pin.PULL_UP)
bang = PWM(Pin(7), freq=1000, duty=1000)

i2c = SoftI2C(scl=Pin(16), sda=Pin(15), freq=400000)

lcd = I2cLcd(i2c, 39, 2, 16)
bang.duty(0)
led_a.value(0)
led_b.value(0)
led_c.value(0)
led_d.value(0)
takki_a_adur= 0
takki_b_adur= 0
takki_c_adur= 0
takki_d_adur= 0
st_a= takki_a.value()
st_b= takki_b.value()
st_c= takki_c.value()
st_d= takki_d.value()
while True:
    st_a= takki_a.value()
    st_b= takki_b.value()
    st_c= takki_c.value()
    st_d= takki_d.value()
    if takki_c_adur==1 and st_c==0:
      
        lcd.move_to(0, 0)
        lcd.putstr("MONEY TIME!! :D")
        led_c.value(1)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        
        sleep_ms(1500)
        lcd.clear()
        led_c.value(0)
        
        
        
        
    if takki_a_adur==1 and st_a==0:
        led_a.value(1)
        bang.duty(500)
        sleep_ms(200)
        bang.duty(400)
        sleep_ms(200)
        bang.duty(300)
        sleep_ms(200)
        bang.duty(200)
        sleep_ms(200)
        bang.duty(100)
        sleep_ms(200)
        bang.duty(0)
        lcd.move_to(0, 0)
        tala= randint(1,6)
        tala = str(tala)
        lcd.putstr(tala)
        sleep_ms(1000)
        led_a.value(0)
        lcd.clear()
        
        
        
    if takki_d_adur==1 and st_d==0:
      
        lcd.move_to(0, 0)
        lcd.putstr("MONEY TIME!! :D")
        led_d.value(1)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        sleep_ms(1500)
        lcd.clear()
        led_d.value(0)
       
        
        
    if  takki_b_adur==1 and st_b==0:
      
        lcd.move_to(0, 0)
        lcd.putstr("WINNER WINNER   CHICKEN DINNER!!")
        led_b.value(1)
        bang.duty(800)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(300)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(0)
        bang.duty(150)
        sleep_ms(250)
        bang.duty(0)
        sleep_ms(100)
        bang.duty(100)
        sleep_ms(500)
        bang.duty(0)
        sleep_ms(2000)
        lcd.clear()
        led_b.value(0)
        
        
    takki_a_adur=st_a
    takki_b_adur=st_b
    takki_c_adur=st_c
    takki_d_adur=st_d

    