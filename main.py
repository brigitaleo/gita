meme_dict = {
  "HAJITHORIQ": "thoriq 2 bulan haji",
  "SIGMA": "keren/mantap"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
  print(meme_dict[word])
else:
  # Apa yang harus kita lakukan jika kata itu ditemukan?
  print("Kata kunci tidak di temukan")
