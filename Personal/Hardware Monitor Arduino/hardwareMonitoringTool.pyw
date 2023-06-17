import serial
import time
import wmi

arduino = serial.Serial(port="COM5", baudrate=115200, timeout=.1)

def writeRead(x):
    arduino.write(x.encode('utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
sensors = w.Sensor()

def getSensorValue(sensor_type, sensor_name):
    sensors = w.Sensor()
    for sensor in sensors:
        if sensor.SensorType == sensor_type and sensor.Name == sensor_name:
            return sensor.Value
    return None

def getCPUTemp():
	cpuTemp = getSensorValue('Temperature', 'CPU Package')
	return cpuTemp

def getCPULoad():
	cpuLoad = getSensorValue('Load', 'CPU Total')
	return cpuLoad

def getMemLoad():
	memLoad = getSensorValue('Load', 'Memory')
	return memLoad

def getMoboTemp():
	moboTemp = getSensorValue('Temperature', 'Temperature #6')
	return moboTemp

def getGPUTemp():
	gpuTemp = getSensorValue('Temperature', 'GPU Core')
	return gpuTemp

def getGPULoad():
	gpuLoad = getSensorValue('Load', 'GPU Core')
	return gpuLoad

def getCaseTemp():	
	caseTemp = getSensorValue('Temperature', 'Temperature #1')
	return caseTemp

def main():
	while True:
		cpuTemp = getCPUTemp()
		A = " " + str(int(cpuTemp))		
		
		cpuLoad = getCPULoad()
		if(cpuLoad < 100):
			B = " " + str(int(cpuLoad))
		else:
			B = str(int(cpuLoad))

		memLoad = getMemLoad()
		if(memLoad < 100):
			C = " " + str(int(memLoad))
		else:
			C = str(memLoad)

		moboTemp = getMoboTemp()
		D = " " + str(int(moboTemp))

		gpuTemp = getGPUTemp()
		E = " " + str(int(gpuTemp))

		gpuLoad = getGPULoad()
		if(gpuLoad < 10):
			F = "  " + str(int(gpuLoad))
		elif(gpuLoad < 100):
			F = " " + str(int(gpuLoad))
		else:
			F = str(gpuLoad)

		caseTemp = getCaseTemp()
		H = " " + str(int(caseTemp))
		      
		finalString1 = "1:" + A + "," + B + "," + C + "," + D + ",;"
		finalString2 = "2:" + E + "," + F + "," + "N/A" + "," + H + ",;"
		finalString3 = "3:;" 

		writeRead(finalString1)
		writeRead(finalString2)
		writeRead(finalString3)
		
		time.sleep(0.5)
                
                
if __name__ == '__main__':
	main()