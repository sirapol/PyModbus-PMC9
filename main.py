import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time


def getDataPowerMeter(iSID):
    lData = getData(iSID, 1000, 10).registers
    lData = lData + getData(iSID, 1010, 10).registers
    lData = lData + getData(iSID, 1020, 10).registers
    lData = lData + getData(iSID, 1030, 10).registers
    lData = lData + getData(iSID, 1040, 10).registers
    lData = lData + getData(iSID, 1050, 6).registers
    return lData


def getData(iSID, iAddr, iOffset):
    pass
    while True:
        try:
            d1 = client.read_holding_registers(iAddr, iOffset, unit=iSID)
            # print(d1.registers)
            if hasattr(d1, 'registers'):
                # print('Read complete')
                break
            else:
                # print('\nIncorrect input, try again')
                time.sleep(0.5)
                pass
        except:
            pass
            print('\nIncorrect input, try again')
    return d1


baudrate = 19200
client = ModbusClient(
    method='rtu', port='COM11', baudrate=baudrate, parity='N', timeout=1000
)
connection = client.connect()
print('Modbus connect : ', connection)

lMeter = getDataPowerMeter(8)
# print(lMeter)
print('Meter6:',(lMeter[38]*65536)+lMeter[39],'kWh')
print('Amp P1:',lMeter[1]*0.001,'A')
print('Amp P2:',lMeter[3]*0.001,'A')
print('Amp P3:',lMeter[5]*0.001,'A')
print('V12:',(((lMeter[8]*65536)+lMeter[9])*0.001),'V')
print('V23:',(((lMeter[10]*65536)+lMeter[11])*0.001),'V')
print('V31:',(((lMeter[12]*65536)+lMeter[13])*0.001),'V')
print('V P1:',(((lMeter[14]*65536)+lMeter[15])*0.001),'V')
print('V P2:',(((lMeter[16]*65536)+lMeter[17])*0.001),'V')
print('V P3:',(((lMeter[18]*65536)+lMeter[19])*0.001),'V')
print('Frequency:',lMeter[21]/100,'Hz')

client.close()