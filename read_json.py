import json

try:
    caminho = input()
    ficheiro = open(caminho, "rt", encoding="utf-8")
    json_file = ficheiro.read()
    data = json.loads(json_file)
    print(data)
    ficheiro.close()

except:
    print("Ocorreu erro!")

finally:
    print("Processo concluído!")
