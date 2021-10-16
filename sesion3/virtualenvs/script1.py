from PIL import Image

imagen_gato = Image.open("gato.jpg")

imagen_rotada = imagen_gato.rotate(45)

# imagen_rotada.save("gato.png")

imagen_gato.thumbnail((150, 150))

imagen_gato.show()
