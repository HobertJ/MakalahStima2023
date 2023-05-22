from bnb import *


food_list = [
    #Food (kalori, karbohidrat, protein, lemak, nama makanan)
    Food(100, 25, 10, 8, "nasi putih"),                      # nasi putih : Kalori = 100, Carbs = 25, Protein = 10, Fat = 8
    Food(300, 50, 3, 25, "roti brazil"),                     # roti brazil : Kalori = 300, Carbs = 50, Protein = 3, Fat = 25
    Food(250, 23, 14, 21, "eskrim aice"),                    # eskrim aice : Kalori = 250, Carbs = 23, Protein = 14, Fat = 21
    Food(320, 40, 20, 4, "ayam goreng paha"),                # ayam goreng paha : Kalori = 320, Carbs = 40, Protein = 20, Fat = 4 
    Food(225, 14, 31, 5, "kucing bakar"),                    # kucing bakar : Kalori = 225, Carbs = 14, Protein = 31, Fat = 5
    Food(415, 23, 3, 45, "nasi goreng"),                     # nasi goreng : Kalori = 415, Carbs = 23, Protein = 3, Fat = 45
    Food(500, 23, 41, 15, "ikan bakar"),                     # ikan bakar : Kalori = 500, Carbs = 23, Protein = 41, Fat = 15
    Food(175, 5, 1, 15, "ayam bakar")                        # ayam bakar : Kalori = 175, Carbs = 5, Protein = 1, Fat = 15
]

# batas kalori
calories = 1500

# Panggil fungsi optimize_nutrition untuk kategori yang diinginkan
# pada contoh code yang sudah siap, category yang dipilih adalah fat atau lemak
best_value, best_food = optimize_nutrition(food_list, calories, "fat")

# Tampilkan hasil
print()
print()
print("=============================================")
print("Item yang dipilih:")
idx = 0
cals = 0
for food in best_food:
    idx+=1
    cals+=food.calories
    print(str(idx) + "." + str(food.nama_makanan) + ", lemak: " + str(food.protein) + ", kalori: " + str(food.calories))

print("Nilai maksimum lemak yang dapat dicapai:", best_value)
print("Jumlah kalori:", cals)
print()
print()

# code dapat diubah untuk menampilkan hasil sesuai yang diinginkan (untuk karbohidrat, protein, serta penggunaan test case sendiri)