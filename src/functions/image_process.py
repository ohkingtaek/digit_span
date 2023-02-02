import cv2


def image_save_yolo():
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    sample_num = 0    
    captured_num = 0

    while webcam.isOpened():
        status, frame = webcam.read()
        sample_num = sample_num + 1
        if not status:
            break
        if sample_num == 1:
            captured_num = captured_num + 1
            cv2.imwrite('./assets/img/img'+str(captured_num)+'.jpg', frame)
            sample_num = 0
        if cv2.waitKey(1) or 0xFF == ord('q') or captured_num == 1:
            break

    webcam.release()
    cv2.destroyAllWindows()
    return captured_num