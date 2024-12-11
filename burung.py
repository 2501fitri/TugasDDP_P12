from Animal import*

class Burung(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_Biak, Jenis, Warna):
        super().__init__(Nama, Makanan, Hidup, Berkembang_Biak)
        self.Jenis = Jenis
        self.Warna = Warna
    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t: ", self.Jenis,
              "\nWarna \t\t\t: ", self.Warna )
Burung = Burung("Cendrawasih", "Serangga", "Papua", "Bertelur", "Birds-of-paradise ", "kuning, merah, hijau, biru, dan hitam")
Burung.cetak_burung()