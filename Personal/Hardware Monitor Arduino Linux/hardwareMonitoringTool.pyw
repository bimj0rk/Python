import serial
import time
import psutil
import py3nvml

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=.1)

def writeRead(x):
    arduino.write(x.encode('utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def initializeNVML():
	py3nvml.nvmlInit()

def handle():
	handle = py3nvml.nvmlDeviceGetHandleByIndex(0)
	return handle

def main():
	while True:
		cpuTemp = psutil.sensors_temperatures()['coretemp'][0].current
		A = " " + str(int(cpuTemp))		
		
		cpuLoad = psutil.cpu_percent()
		if(cpuLoad < 10):
			B = "  " + str(int(cpuLoad))
		elif(cpuLoad < 100 and cpuLoad > 10):
			B = " " + str(int(cpuLoad))
		else:
			B = str(int(cpuLoad))

		memLoad = psutil.virtual_memory().percent
		if(memLoad < 10):
			C = "  " + str(int(memLoad))
		elif(memLoad < 100 and memLoad > 10):
			C = " " + str(int(memLoad))
		else:
			C = str(int(memLoad))

		moboTemp = 'N/A'
		D = moboTemp

		gpuTemp = py3nvml.nvmlDeviceGetTemperature(handle, 0)
		E = " " + str(int(gpuTemp))

		gpuLoad = py3nvml.nvmlDeviceGetUtilizationRates(handle).gpu
		if(gpuLoad < 10):
			F = "  " + str(int(gpuLoad))
		elif(gpuLoad < 100 and gpuLoad > 10):
			F = " " + str(int(gpuLoad))
		else:
			F = str(int(gpuLoad))

		caseTemp = "N/A"
		H = caseTemp
		      
		finalString1 = "1:" + A + "," + B + "," + C + "," + D + ",;"
		finalString2 = "2:" + E + "," + F + "," + "N/A" + "," + H + ",;"
		finalString3 = "3:;" 

		writeRead(finalString1)
		writeRead(finalString2)
		writeRead(finalString3)
		
		time.sleep(0.5)
                
                
if __name__ == '__main__':
	initializeNVML()
	handle = handle()
	main()