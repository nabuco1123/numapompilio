from PIL import Image
import os
"""comprimir fotos y reubicarlas en su carpeta lo mismo para la musica y videos
o cualquier tipo de archivo"""

downloadsFolder = "/Users/Jhonnyfive/Downloads/"
picturesFolder  = "/Users/Jhonnyfive/Pictures/"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/Jhonnyfive/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)

        if extension in [".mp4"]:
            videosFolder = "/Users/Jhonnyfive/Desktop/videos_youtube/"
            os.rename(downloadsFolder + filename, videosFolder + filename)

        if extension in [".pdf"]:
            pdfFolder = "/Users/Jhonnyfive/Desktop/archivosPdf/"
            os.rename(downloadsFolder + filename, pdfFolder + filename)