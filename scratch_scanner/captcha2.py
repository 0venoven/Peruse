from captcha.audio import AudioCaptcha

# Create an audio instance
audio = AudioCaptcha()

# Generate audio captcha with text '1234'
data = audio.generate('1234')

# Save audio to a file
audio.write('1234', '1234.wav')