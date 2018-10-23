from homework_02.main import monitor
import time

path = r'C:\Users\anton.romashko\PycharmProjects\StudyAdvanced\homework_02/'
folders = ['read', 'result', 'mistake']
while True:
    monitor(path + folders[0], path + folders[1], path + folders[2])
    time.sleep(5)
