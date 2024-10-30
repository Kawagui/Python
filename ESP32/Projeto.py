from libdis import HCSR04
from time import sleep_ms
import machine
import neopixel

# Configuração do pino e quantidade de LEDs
pino_led = 13  # Altere para o pino que você conectou o DATA IN
num_leds = 1   # Número de LEDs na sequência

# Inicializa o controle dos LEDs
np = neopixel.NeoPixel(machine.Pin(pino_led), num_leds)

# Função para acender o LED em uma cor específica (RGB)
def acender_led(r, g, b):
    np[0] = (r, g, b)
    np.write()

# ESP32
sensor = HCSR04(trigger_pin=5, echo_pin=4, echo_timeout_us=10000)
buzzer = machine.PWM(machine.Pin(15))

delay = 10
duty = 300
# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_mm()
    distanc = sensor.distance_cm()
    print('Distance:', distance, 'mm', distanc, 'cm')
    if distanc < 20 and distanc > 0:
        buzzer.init(freq=440, duty=0)
        acender_led(255, 0, 0)  # Vermelho
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(2093)
        sleep_ms(delay*10)
        buzzer.deinit()
        acender_led(0, 0, 0)
    elif distanc < 40 and distanc >= 20:
        buzzer.init(freq=440, duty=0)
        acender_led(255, 165, 0)  # Laranja
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(3126)
        sleep_ms(delay*25)
        buzzer.deinit()
        acender_led(0, 0, 0)
    elif distanc < 60 and distanc >= 40:
        buzzer.init(freq=440, duty=0)
        acender_led(255, 255, 0)  # Amarelo
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(1397)
        sleep_ms(delay*20)
        buzzer.deinit()
        acender_led(0, 0, 0)
    elif distanc < 80 and distanc >= 60:
        buzzer.init(freq=440, duty=0)
        acender_led(0, 0, 255)  # Azul
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(880)
        sleep_ms(delay*50)
        buzzer.deinit()
        acender_led(0, 0, 0)
    elif distanc < 100 and distanc >= 80:
        buzzer.init(freq=440, duty=0)
        acender_led(0, 255, 0)  # Verde
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(330)
        sleep_ms(delay*75)
        buzzer.deinit()
        acender_led(0, 0, 0)
    else:
        buzzer.init(freq=440, duty=0)
        acender_led(255, 255, 255) # Branco
        print('Distance:', distance, 'mm', distanc, 'cm')
        buzzer.duty(duty)
        buzzer.freq(1319)
        sleep_ms(delay*100)
        buzzer.deinit()
        acender_led(0, 0, 0)
# Importar a classe e inserir o código
