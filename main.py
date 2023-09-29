import cv2
from pyzbar.pyzbar import decode
import time
from classes.VLCPlayer import VLCPlayer
from classes.QRCode import QRCode

cap = cv2.VideoCapture(0)
player = VLCPlayer()
currentPage = ""
QRCode.generate_codes()

sleepTime = 0.5  # Change this for the webcam's refresh rate
showOutput = True  # if you don't want to see the webcam's output
inverted = True


while True:
    try:
        detector = cv2.QRCodeDetector()
        _, frame = cap.read()

        if inverted:
            img = cv2.bitwise_not(frame)
        else:
            img = frame

        data, bbox, _ = detector.detectAndDecode(img)

        # Don't play if the same media is being detected
        if data != currentPage and data != "":
            print(data)
            currentPage = data
            # Play Video
            player.play_media("./videos/" + data)
        else:
            time.sleep(sleepTime)

        if showOutput:
            cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    except Exception as e:
        print(e)

cap.release()
cv2.destroyAllWindows()
