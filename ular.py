from Animal import*

class Ular(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_Biak, Design, Racun):
        super().__init__(Nama, Makanan, Hidup, Berkembang_Biak)
        self.Design = Design
        self.Racun = Racun
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t: ", self.Design,
              "\nRacun \t\t\t: ", self.Racun)
        
Ular_Piton = Ular("Ular Piton", "Tikus", "Asia Tenggara", "Bertelur", "Batik Solo", "Berbisa")
Ular_Piton.cetak_ular()
