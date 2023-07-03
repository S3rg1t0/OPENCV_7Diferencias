import cv2


class FindDifference:

    def __init__(self, imagen1, imagen2):
        self.imagen1 = cv2.imread(imagen1)
        self.imagen2 = cv2.imread(imagen2)

    def find(self):
        imagen = cv2.absdiff(self.imagen1, self.imagen2)
        if self.imagen1 is None:
            print(f"No se pudo cargar la imagen1")
            return None
        if self.imagen2 is None:
            print(f"No se pudo cargar la imagen2")
            return None
        print("Se han hecho las fotos bien")
        imagen_bin = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen_blur = cv2.blur(imagen_bin, (10, 10))
        _, imagen_umbral = cv2.threshold(imagen_blur, 30, 255, cv2.THRESH_BINARY)
        cont, _ = cv2.findContours(imagen_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        imagen_tratada = self.imagen1

        for c in cont:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(imagen_tratada,
                          (x, y),
                          (x + w, y + h),
                          (255, 0, 0),
                          2)
        return imagen_tratada
