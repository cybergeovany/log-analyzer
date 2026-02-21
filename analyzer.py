file = open("auth.log", "r")

ips = {}

with open("auth.log", "r") as file:
    for line in file:
        parts = line.split()

        if "from" in parts:
            idx = parts.index("from")
            ip = parts[idx + 1]

            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1

print("Resumo de tentativas:\n")

for ip, count in ips.items():
    print("IP:", ip, "→", count, "tentativas")


maior_ip = None
maior_count = 0

for ip, count in ips.items():
    if count > maior_count:
        maior_count = count
        maior_ip = ip

print("\nIP mais sus:")
print(maior_ip, "com", maior_count, "tentativas")

with open("resultado.txt", "w") as output:
	for ip, count in ips.items():
		linha = f"IP: {ip} -> {count} tentativas\n"
		output.write(linha)

file.close()
