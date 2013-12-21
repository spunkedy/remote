from app import app

if __name__ == "__main__":
    # Turn the receiver on, select PC input

    app.debug = True
    app.run(host='0.0.0.0')
