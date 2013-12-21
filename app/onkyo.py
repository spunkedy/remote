__author__ = 'ebond'
import eiscp
from app import app
import default

Receiver = None
Config = None

@app.route("/onkyo")
def onkyo():
    return default.index()

@app.route("/onkyo/powerOn")
def onkyoPowerOn():
    Receiver.command('system-power on')
    return default.index()

@app.route("/onkyo/powerOff")
def onkyoPowerOff():
    Receiver.command('system-power standby')
    return default.index()

@app.route("/onkyo/volUp10")
def onkyoVolUp10():
    volume = Receiver.command('volume query')
    val = int(volume[1],16)
    val = val + 10
    Receiver.command('Volume ' + str(val))
    return default.index()

@app.route("/onkyo/volDown10")
def onkyoVolDown10():
    volume = Receiver.command('volume query')
    val = int(volume[1],16)
    val = val - 10
    Receiver.command('Volume ' + str(val))
    return default.index()

@app.route("/onkyo/volUp")
def onkyoVolUp():
    Receiver.command('volume level-up')
    return default.index()

@app.route("/onkyo/volDown")
def onkyoVolDown():
    Receiver.command('volume level-down')
    return default.index()

@app.route("/onkyo/airplay")
def onkyoAirplay():
    Receiver.command('input-selector VIDEO6')
    return default.index()

@app.route("/onkyo/roku")
def onkyoRoku():
    Receiver.command('input-selector VIDEO1')
    return default.index()


@app.route("/onkyo/chrome")
def onkyoChrome():
    Receiver.command('input-selector dvd')
    return default.index()


@app.route("/onkyo/ps3")
def onkyoPs3():
    Receiver.command('input-selector game')
    return default.index()



def setupOnkyo(ConfigToUse):
    global Config
    Config = ConfigToUse
    global Receiver
    Receiver = eiscp.eISCP(Config.get("onkyo","host"))