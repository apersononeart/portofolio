# # number = []
# # while number != 0:
# # 	number = int(input("Enter a number: "))

# # 	factor = []

# # 	for bil_bulat in range(1, number + 1) :
# # 		if number % bil_bulat == 0:
# # 			factor.append(bil_bulat)


# # 	print(f"The numbers of {number} are {factor}")

# # else:
# # 	exit()


# def recur_factorial(n):
# 	if (n==1 or n==0):
# 		return 1
# 	else: 
# 		return n*recur_factorial(n-2)

# angka = int(input("Ente a number: "))

# if angka < 0:
# 	print("Angka harus bernilai bulat positif")
# else:
# 	print(f"Faktorial dari {angka} adalah {recur_factorial(angka)}")
