
print("\"csv2js\" 0.1 август 2019 (ДКХ)")

print("Открытие файла \"input.csv\"")
f = open("input.csv")

lines = []
for i in f:
	lines.append(i.replace("\n", ""))
f.close()

print("Считано объектов: "+str(len(lines)))

div = str(input("Какой символ разделения ячеек? "))
print("Создание базы данных")
obj = []
for i in range(0, len(lines)-1):
	obj.append([])
	for j in range(0, len(str(lines[i]).split(div))):
		obj[i].append( str(lines[i]).split(div)[j] )

print("Сохранение в \"output.js\"")
f = open("output.js", "w")
nObj = -1
lObj = -1
i = 0
while i < len(obj):
	lObj = nObj
	nObj = int(obj[i][0])
	if lObj != nObj:
		if lObj >= 0:
			f.write("\n];\n");
		f.write("var "+obj[i][1]+" = [\n");
		f.write("  {\n");
		f.write("    arrayName: \""+obj[i][1]+"\"\n");
		f.write("  },\n");
	else:
		f.write(",\n");
	f.write("  {\n");
	f.write("    name:        \""+obj[i][2]+"\",\n");
	f.write("    model:       \""+obj[i][3]+"\",\n");
	f.write("    price:       "+obj[i][4]+",\n");
	f.write("    priceValute: \""+obj[i][5]+"\",\n");
	f.write("    kvt:         "+obj[i][6]+",\n");
	f.write("    article:     \""+obj[i][7]+"\"\n");
	f.write("  }");
	i += 1
f.write("\n];\n");
print("Программа выполнена.")
