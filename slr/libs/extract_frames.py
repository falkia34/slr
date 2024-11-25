import cv2

def extract_frames(file_path):
    frames = []

    # Membaca video dari path yang diberikan
    cam = cv2.VideoCapture(file_path)

    while True:
        # Baca satu frame dari video
        ret, frame = cam.read()

        if ret:
            # Resize frame ke ukuran 256x256 px
            resized_frame = cv2.resize(frame, (256, 256))

            # Tambahkan frame ke list
            frames.append(resized_frame)
        else:
            break

    # Release sumber daya video
    cam.release()

    return frames
