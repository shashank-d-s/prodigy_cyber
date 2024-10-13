# The task 2 of the Prodigy Infotech Internship program--Pixel Manipulation for Image Encryption


from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    encrypted_pixels = [(pixel[0] + key, pixel[1] + key, pixel[2] + key) for pixel in pixels]
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    
    return encrypted_image

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    decrypted_pixels = [(pixel[0] - key, pixel[1] - key, pixel[2] - key) for pixel in pixels]
    
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    
    return decrypted_image

key = 50  
encrypted_img = encrypt_image('task2/input_image.jpg', key)
encrypted_img.save('task2/encrypted_image.jpg')
decrypted_img = decrypt_image('task2/encrypted_image.jpg', key)
decrypted_img.save('task2/decrypted_image.jpg')
