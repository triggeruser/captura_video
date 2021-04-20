import cv2


def captura_video(camera):
    captura = cv2.VideoCapture(camera)
    return captura


def show_video(cap):
    while cap.isOpened():
        ret, imagen = cap.read()
        if ret:
            cv2.imshow('Video', imagen)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    cap = captura_video(0)
    show_video(cap)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
