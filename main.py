
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import registry, declarative_base

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base = declarative_base()

def modbus_auto_connect_on_first():#(host="localhost", port=502, unit_id=1, auto_open=True):
    # TCP auto connect on first modbus request
    c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)
    return c

def modbus_auto_connect_close_after():
    # TCP auto connect on modbus request, close after it
    c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)
    return c

def modbus_read_hold(c, args):
    regs = c.read_holding_registers(*args)#(0, 2)
    if regs:
        print(regs)
    else:
        print("read error")

def modbus_write(c, args):
    if c.write_multiple_registers(*args):#(10, [44,  55])
        print("write ok")
    else:
        print("write error")