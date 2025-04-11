from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import json, socket

hostname = socket.gethostname()
config_path = f"/etc/phenix/injects/{hostname}.json"

try:
    with open(config_path, "r") as f:
        inject_data = json.load(f)
except FileNotFoundError:
    inject_data = {}

# Separate into holding registers and coils
holding_registers = []
coils = []

for k, v in inject_data.items():
    if isinstance(v, bool) or v in [0, 1]:
        coils.append(int(v))
    else:
        holding_registers.append(int(v))

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*10),
    co=ModbusSequentialDataBlock(0, coils or [0]*10),
    hr=ModbusSequentialDataBlock(0, holding_registers or [0]*10),
    ir=ModbusSequentialDataBlock(0, [0]*10),
    zero_mode=True
)

context = ModbusServerContext(slaves=store, single=True)
identity = ModbusDeviceIdentification()
identity.VendorName = 'SCEPTRE'
identity.ProductCode = 'SC'
identity.VendorUrl = 'http://sandia.gov'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'ModSim'
identity.MajorMinorRevision = '1.0'

print("[+] Modbus TCP server starting on 0.0.0.0:502")
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
