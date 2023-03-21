import requests
import shutil

def main():
    URL = 'https://www.muratkoklu.com/datasets/vtdhnd07.php'
    PATH = '../Dados/Bruto/data.zip'
    
    #  Fazendo o Download dos Dados
    with requests.get(URL, stream=True) as response:
        with open(PATH, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
            
    #  Descompactando os Dados e removendo o arquivo .zip
    shutil.unpack_archive(PATH, '../Dados/Bruto/')
    shutil.os.remove(PATH)
    
    #  Movendo todos os arquivos para a pasta raiz
    for file in shutil.os.listdir('../Dados/Bruto/Acoustic_Extinguisher_Fire_Dataset'):
        shutil.move(f'../Dados/Bruto/Acoustic_Extinguisher_Fire_Dataset/{file}', '../Dados/Bruto/')
        
    #  Removendo a pasta vazia
    shutil.os.rmdir('../Dados/Bruto/Acoustic_Extinguisher_Fire_Dataset')
    
if __name__ == '__main__':
    main()
    