"Program Perhitungan BMI"

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("---------------------------------")

berat_badan = input("Masukkan berat badan anda (kg): ")
berat_badan = float(berat_badan)

tinggi_badan = input("Masukkan tinggi badan anda (cm): ")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print(f"Berat badan ideal anda adalah dalam rentang "
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:2f} kg")