import qrcode
import os


class QRCode:
    # Creates qr codes on all videos under videos folder
    @staticmethod
    def generate_codes():
        videos_directory = "./videos"
        files_in_directory = os.listdir(videos_directory)

        # If no files under videos
        if not files_in_directory:
            raise Exception("No files found under videos!")
        else:
            # Create a qr code for all videos
            for file in files_in_directory:
                file_path = os.path.join(videos_directory, file)
                if os.path.isfile(file_path):
                    base_name = os.path.splitext(file)[0]
                    QRCode.create_code(base_name)

    # Method for creating qr codes
    @staticmethod
    def create_code(data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data + ".mp4")

        qr.make(fit=True)

        img = qr.make_image(fill_color="white", back_color="black")
        img.save("./codes/" + data + ".png")
