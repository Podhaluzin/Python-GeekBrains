from time import sleep
class TrafficLight:
    color = ['КРАСНЫЙ', 'ЖЕЛТНЫЙ', 'ЗЕЛЕНЫЙ']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается, подождите... \n '
                  f'{TrafficLight.color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(2)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()