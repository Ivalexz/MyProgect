with open ("C:\\Users\\TEXHORAY\\Desktop\\information.txt", "w") as file1 :
    file1.write('Привіт! Я Саша Іванчук, мені 15 років. Я навчаюся у IT Step')
file1.close()

with open("C:\\Users\\TEXHORAY\\Desktop\\information.txt", "r") as file1 :
    print(file1.read())
file1.close()