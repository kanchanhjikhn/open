from django.shortcuts import render
import qrcode
from PIL import Image, ImageOps, ImageChops
from io import BytesIO
import base64

def generate_qr_code_with_logo(qr_text, logo_path,):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=5,
    )
    qr.add_data(qr_text)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")  # Transparent background

    # Load the logo image
    logo = Image.open(logo_path)

    # Calculate the position to center the logo on the QR code
    qr_width, qr_height = qr_image.size
    logo_width, logo_height = logo.size
    position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

    # Paste the logo on the QR code
    qr_image.paste(logo, position)

    return qr_image

def index(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        logo_path = '/home/kanchan.agarwal/download_image/logo.png'  # Replace with the actual path to your logo image
        qr_image = generate_qr_code_with_logo(qr_text, logo_path)

        stream = BytesIO()
        qr_image.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
    return render(request, 'index.html', context=context)