import io

from PIL import Image, ImageDraw, ImageFont


def generate_image_file(
    image_format: str,
) -> tuple[io.BytesIO, str]:
    """
    Create an image and return it as a BytesIO object with default settings.
    Args:
        image_format (str): The format of the image (e.g., 'JPEG', 'PNG').
    Returns:
        image_bytes (BytesIO): The image in memory as a BytesIO object.
        file_name: (str): The name of the image file.
    """
    file_name: str = f"test_{image_format}.{image_format}".lower()
    img = Image.new("RGB", (100, 50), color="red")
    bio = io.BytesIO()
    img.save(bio, format=image_format)
    bio.seek(0)
    return bio, file_name

