import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Python!!!!",
            message = "Done.....!!!!!",
            timeout =12
        )
        time.sleep(3600)