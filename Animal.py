class Animal :
    def __init__(self, Nama, Makanan, Hidup, Berkembang_Biak):
        self.Nama = Nama
        self.Makanan = Makanan
        self.Hidup = Hidup
        self.Berkembang_Biak = Berkembang_Biak 

    def cetak(self):
        print("Nama \t\t\t: ", self.Nama, 
                "\nMakanan \t\t: ", self.Makanan,
                "\nHidup \t\t\t: ", self.Hidup,
                "\nBerkembang_Biak \t: ", self.Berkembang_Biak
                )

object = Animal("Buaya", "Daging", "Amphibi", "Bertelur")
object.cetak()
