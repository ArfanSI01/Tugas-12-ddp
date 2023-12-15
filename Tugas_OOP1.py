class Gempa:
    lokasi = ""
    skala = ""

    def __init__(self, daerah, skala):
        self.lokasi = daerah
        self.skala = skala
    
    def dampak (self):
        lokasi = self.lokasi
        print(lokasi)
        if self.skala <=2 :
            print("Maka dampak tidak terasa")
        elif 3<= self.skala <= 4 :
            print("Maka dampak gempa bangunan retak-retak")
        elif 4<= self.skala <= 6 :
            print("Maka dampak bangunan roboh")
        elif self.skala > 6 :
            print("Maka dampak bangunan roboh dan berpotensi tsunami")