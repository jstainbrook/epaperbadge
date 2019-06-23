#!/usr/bin/env python

import sys
import buttonshim
import qrcode
import inkyphat

print("""Inky pHAT: QR Code

Display a QR Code on Inky pHAT!

Usage: {} <colour> <your message>""".format(sys.argv[0]))

# Max length is 152
text = """In the old #BILGETANK we'll keep you in the know,
In the old #BILGETANK we'll fix your techie woes.

https://www.youtube.com/pimoroniltd"""

if len(sys.argv) < 2:
    print("""Valid colours for v2 are: red, yellow or black
Inky pHAT v1 is only available in red.""".format(sys.argv[0]))
    sys.exit(1)

colour = sys.argv[1]

try:
    inkyphat.set_colour(colour)
except ValueError:
    print('Invalid colour "{}" for V{}\n'.format(colour, inkyphat.get_version()))
    if inkyphat.get_version() == 2:
        sys.exit(1)
    print('Defaulting to "red"')

if len(sys.argv) > 2:
    text = sys.argv[2]


class InkyQR(qrcode.image.base.BaseImage):
    def new_image(self, **kwargs):
        self.offset_x = kwargs.get("offset_x", None)
        self.offset_y = kwargs.get("offset_y", None)

        if self.pixel_size - (self.border * 2) > min(inkyphat.WIDTH, inkyphat.HEIGHT):
            print("QR code is too large for Inky pHAT, it probably wont scan! Try `box_size=1`")

        if self.offset_x is None:
            self.offset_x = (inkyphat.WIDTH // 2) - (self.pixel_size // 2)
        if self.offset_y is None:
            self.offset_y = (inkyphat.HEIGHT // 2) - (self.pixel_size // 2)

        box = (self.offset_x, self.offset_y, self.offset_x + self.pixel_size - 1, self.offset_y + self.pixel_size - 1)
        inkyphat.rectangle(box, fill=inkyphat.WHITE)

    def pixel_box(self, row, col):
        x = (col + self.border) * self.box_size
        y = (row + self.border) * self.box_size
        x += self.offset_x
        y += self.offset_y
        return [(x, y), (x + self.box_size - 1, y + self.box_size - 1)]

    def drawrect(self, row, col):
        box = self.pixel_box(row, col)
        inkyphat.rectangle(box, fill=inkyphat.BLACK)


inkyphat.set_image("/home/pi/scripts/resources/empty-backdrop.png")

qr = qrcode.QRCode(
    version=1,
    box_size=2,
    border=2,
    image_factory=InkyQR
)

qr.add_data(text)
qr.make(fit=True)
qr.make_image()

inkyphat.show()

buttonshim.set_pixel(0x00,0x00,0x00)
