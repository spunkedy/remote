from flask import Flask

app = Flask(__name__)
from app import onkyo
from app import roku
from app import default
import ConfigParser


Config = ConfigParser.ConfigParser()
Config.read("/etc/remote.conf")
Receiver = onkyo.setupOnkyo(Config)