import GPUtil
import serial
import time
import psutil
import wmi

arduino = serial.Serial(port="COM5", baudrate=115200, timeout=.1)

def writeRead(x):
    arduino.write(x.encode('utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
sensors = w.Sensor()

wM = wmi.WMI(namespace="root\wmi")
moboTemp = (w.MSAcpi_ThermalZoneTemperature()[0].currentTemperature/10) - 273.15

def getSensorValue(sensor_type, sensor_name):
    sensors = w.Sensor()
    for sensor in sensors:
        if sensor.SensorType == sensor_type and sensor.Name == sensor_name:
            return sensor.Value
    return None

def getCPUTemp():
	cpuTemp = getSensorValue('Temperature', 'CPU Package')
	return cpuTemp
            

def main():
	while True:
		cpuTemp = getCPUTemp()
		A = " " + str(int(cpuTemp))		
		
		cpuLoad = int(round(psutil.cpu_percent(),1))
		if(cpuLoad < 100):
			B = " " + str(cpuLoad)
		else:
			B = str(cpuLoad)

		memLoad = int(round(psutil.virtual_memory()[2],1))
		if(memLoad < 100):
			C = " " + str(memLoad)
		else:
			C = str(memLoad)

		D = " " + str(int(moboTemp))

		gpu = GPUtil.getGPUs()[0]
		E = " " + str(int(round(gpu.temperature,1)))

		gpuLoad = int(round(gpu.load*100,1))
		if(gpuLoad < 100):
			F = " " + str(gpuLoad)
		else:
			F = str(gpuLoad)
		      
		finalString1 = "1:" + A + "," + B + "," + C + "," + D + ",;"
		finalString2 = "2:" + E + "," + F + "," + "N/A" + "," + "N/A" + ",;"
		finalString3 = "3:;" 

		writeRead(finalString1)
		writeRead(finalString2)
		writeRead(finalString3)
		
		time.sleep(0.5)
                
                
if __name__ == '__main__':
	main()