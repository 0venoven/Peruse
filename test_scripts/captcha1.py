# Image captcha

from captcha.image import ImageCaptcha

# Create an image instance
image = ImageCaptcha()

# Generate image captcha with text '1234'
data = image.generate('1234')

# Save the image to a file
image.write('1234', '1234.png')