"""Genera qr.png (verde sobre oscuro) y qr-light.png (oscuro sobre blanco, máxima compatibilidad) con la K de Koin al centro."""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont

URL = "https://404mqs.github.io/leandro-koin-card/"
DARK, GREEN, WHITE = (12, 17, 20), (20, 221, 62), (255, 255, 255)

def k_mark(size):
    """Dibuja la K de Koin (favicon de koin.com.br, viewBox 32x32) a `size` px, supersampleado."""
    ss = 4
    s = size * ss / 32
    k = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(k)
    d.rounded_rectangle([0, 0, size * ss - 1, size * ss - 1], radius=int(6.4 * s), fill=DARK, outline=GREEN, width=int(0.6 * s))
    pts = lambda p: [(x * s, y * s) for x, y in p]
    d.polygon(pts([(26, 25), (18.465, 15), (16.163, 18.8), (20.977, 25)]), fill=WHITE)
    d.rectangle([8 * s, 9 * s, 11.977 * s, 25 * s], fill=WHITE)
    d.polygon(pts([(19.93, 7), (8.837, 25), (13.442, 25), (24.535, 7)]), fill=GREEN)
    return k.resize((size, size), Image.LANCZOS)


def make(out, fg, bg, label):
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=3)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(front_color=fg, back_color=bg),
    ).convert("RGB")

    w, h = img.size
    logo = k_mark(int(w * 0.22))
    img.paste(logo, ((w - logo.width) // 2, (h - logo.height) // 2), logo)

    pad, label_h = 40, 52
    canvas = Image.new("RGB", (w + pad * 2, h + pad * 2 + label_h), bg)
    canvas.paste(img, (pad, pad))

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
    text = "koin · leandro montedonico"
    bbox = draw.textbbox((0, 0), text, font=font)
    draw.text(((canvas.width - (bbox[2] - bbox[0])) // 2, h + pad + 12), text, fill=label, font=font)

    canvas.save(out)
    print(out, canvas.size)


make("qr.png", GREEN, DARK, GREEN)
make("qr-light.png", DARK, WHITE, (12, 133, 37))
