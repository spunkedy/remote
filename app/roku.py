__author__ = 'ebond'
import pyroku
from app import app

Config = None

@app.route("/roku")
def roku():
    return "Roku Mapping"

def setupRoku(ConfigToUse):
    global Config
    Config = ConfigToUse