import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import serial_asyncio
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

# Grafica altitud
def al_ti():
    df = pd.read_csv('data_Sat.csv')
    plt.figure()
    plt.plot(df['Tiempo'], df['Altitud'])
    plt.xlabel('Tiempo')
    plt.ylabel('Altitud')
    plt.title('Altitud con respecto al Tiempo')
    plt.grid(True)
    plt.savefig('static/Img/grafica_altitud.png',dpi=40)
    return plt.gcf()

# Grafica presion
def pr_ti():
    df = pd.read_csv('data_Sat.csv')
    plt.figure()
    plt.plot(df['Tiempo'],df['Presion'])
    plt.xlabel('Tiempo')
    plt.ylabel('Presion')
    plt.title('Presion con respecto al Tiempo')
    plt.grid(True)
    plt.savefig('static/Img/grafica_presion.png',dpi=40)
    return plt.gcf()

# Grafica temperatura
def te_ti():
    df = pd.read_csv('data_Sat.csv')
    plt.figure()
    plt.plot(df['Tiempo'], df['Temperatura'])
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Temperatura con respecto al Tiempo')
    plt.grid(True)
    plt.savefig('static/Img/grafica_temperatura.png',dpi=40)
    return plt.gcf()

# Grafica velocidad
def ve_ti():
    df = pd.read_csv('data_Sat.csv')
    plt.figure()
    plt.plot(df['Tiempo'], df['Velocidad'])
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title('Velocidad con respecto al Tiempo')
    plt.grid(True)
    plt.savefig('static/Img/grafica_velocidad.png',dpi=40)
    return plt.gcf()

# Grafica aceleracion
def ac_ti():
    df = pd.read_csv('data_Sat.csv')
    plt.figure()
    plt.plot(df['Tiempo'], df['Aceleracion'])
    plt.xlabel('Tiempo')
    plt.ylabel('Aceleracion')
    plt.title('Aceleracion con respecto al Tiempo')
    plt.grid(True)
    plt.savefig('static/Img/grafica_aceleracion.png',dpi=40)
    return plt.gcf()



