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

def main():
	while True:
		cpuTemp = getSensorValue('Temperature', 'CPU Package')
		A = " " + str(int(cpuTemp))		
		
		cpuLoad = getSensorValue('Load', 'CPU Total')
		if(cpuLoad < 10):
			B = "  " + str(int(cpuLoad))
		elif(cpuLoad > 100 and cpuLoad > 10):
			B = " " + str(int(cpuLoad))
		else:
			B = str(int(cpuLoad))

		memLoad = getSensorValue('Load', 'Memory')
		if(memLoad < 10):
			C = "  " + str(int(memLoad))
		elif(memLoad < 100 and memLoad > 10):
			C = " " + str(int(memLoad))
		else:
			C = str(int(memLoad))

		moboTemp = getSensorValue('Temperature', 'Temperature #1')
		D = " " + str(int(moboTemp))

		gpuTemp = getSensorValue('Temperature', 'GPU Core')
		E = " " + str(int(gpuTemp))

		gpuLoad = getSensorValue('Load', 'GPU Core')
		if(gpuLoad < 10):
			F = "  " + str(int(gpuLoad))
		elif(gpuLoad < 100 and gpuLoad > 10):
			F = " " + str(int(gpuLoad))
		else:
			F = str(int(gpuLoad))

		caseTemp = getSensorValue('Temperature', 'Temperature #2')
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