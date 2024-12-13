"""
A simple QR code generator using the `qrcode` library.

Dependencies to install: qrcode, Pillow

This script defines a class `GenerateQR` that can generate and save QR codes based on user input.
Users can specify QR code size, padding, and color settings.
"""
import qrcode

class GecnerateQR:
    def __init__(self, size: int, padding: int):
        """Initialize the QR code generator with size and padding."""
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, foreground: str, background: str):
        """Generate a QR code from user input and save it to a file.

        Args:
            file_name (str): The name of the file to save the QR code.
            foreground (str): The color of the QR code.
            background (str): The background color of the QR code.
        """
        user_input: str = input("Enter text: ")

        try:
            self.qr.add_data(user_input)
            self.qr.make(fit=True)  # Ensure the data fits the QR code size
            qr_image = self.qr.make_image(fill_color=foreground, back_color=background)
            qr_image.save(file_name)

            print(f"Successfully created! ({file_name})")
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Run the QR code generator with preset parameters."""
    myqr = GenerateQR(size=30, padding=3)
    myqr.create_qr(file_name="sample.png", foreground="blue", background="white")

if __name__ == "__main__":
    main()
