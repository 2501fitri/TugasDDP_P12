from Animal import*

class Ikan(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_Biak, Warna, Ciri_Khas):
        super().__init__(Nama, Makanan, Hidup, Berkembang_Biak)
        self.Warna = Warna
        self.Ciri_Khas = Ciri_Khas
    def cetak_ikan(self):
        super().cetak()
        print("Warna \t\t\t: ", self.Warna,
              "\nCiri_Khas \t\t: ", self.Ciri_Khas )
Ikan = Ikan("Mujair", "kangkung", "perairan tawar", "Bertelur", "hitam, keabu-abuan, kecoklatan dan kuning", "memiliki mata berwarna merah, agak kehitaman atau agak kecoklatan")
Ikan.cetak_ikan()