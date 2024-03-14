import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import serial_asyncio
from matplotlib.animation import FuncAnimation
import asyncio
import csv

lora_band = "915000000"
lora_networkid = "6"
lora_address = "0"

async def main():
    reader, writer = await serial_asyncio.open_serial_connection(url='COM3', baudrate=115200)

    writer.write(("AT+BAND="+lora_band+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+NETWORKID="+lora_networkid+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+ADDRESS="+lora_address+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+PARAMETER=7,7,1,4\r\n").encode())
    await writer.drain()

    while True:
        data = await reader.read(100)
        if data:
            print(data.decode())

# asyncio.run(main())

df = pd.read_csv('data_Sat.csv')
print(df)

def ani_al_ti(i):
    plt.cla()
    df = pd.read_csv('data_Sat.csv')
    x = df['Tiempo']
    y = df['Altitud']
    plt.plot(x[:i+1], y[:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Altitud')
    plt.title('Altitud con respecto al Tiempo')
    
def ani_pr_ti(i):
    plt.cla()
    df = pd.read_csv('data_Sat.csv')
    x = df['Tiempo']
    y = df['Presion']
    plt.plot(x[:i+1], y[:i+1])
    plt.xlabel('Tiempo')
    plt.ylabel('Presion')
    plt.title('Presion con respecto al Tiempo')
    
def ani_te_ti(i):
    plt.cla()
    df = pd.read_csv('data_Sat.csv')
    x = df['Tiempo']
    y = df['Temperatura']
    plt.plot(x[:i+1], y[:i+1])
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Temperatura con respecto al Tiempo')

def ani_ve_ti(i):
    plt.cla()
    df = pd.read_csv('data_Sat.csv')
    x = df['Tiempo']
    y = df['Velocidad']
    plt.plot(x[:i+1], y[:i+1])
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title('Velocidad con respecto al Tiempo')

def ani_ac_ti(i):
    plt.cla()
    df = pd.read_csv('data_Sat.csv')
    x = df['Tiempo']
    y = df['Aceleracion']
    plt.plot(x[:i+1], y[:i+1])
    plt.xlabel('Tiempo')
    plt.ylabel('Aceleracion')
    plt.title('Aceleracion con respecto al Tiempo')
    

    
aniAlTi = FuncAnimation(plt.gcf(), ani_al_ti, frames=len(df), interval=1000, repeat=False)
# aniPrTi = FuncAnimation(plt.gcf(), ani_pr_ti, frames=len(df), interval=1000, repeat=False)
# aniTeTi = FuncAnimation(plt.gcf(), ani_te_ti, frames=len(df), interval=1000, repeat=False)
# aniVeTi = FuncAnimation(plt.gcf(), ani_ve_ti, frames=len(df), interval=1000, repeat=False)
# aniAcTi = FuncAnimation(plt.gcf(), ani_ac_ti, frames=len(df), interval=1000, repeat=False)

plt.show()

