
import platform
import subprocess
import struct
import sys
import os


class Instalador:

    def __init__(self):

        print('\n--------------------------------------\n Instalador Geosis v1.0 para Windows\n--------------------------------------\n')

        if platform.system() != 'Windows':
    
            print('\n ERRO: Esse instalador é para a plataforma Windows\n')
            input('\n Pressione qualquer tecla para sair...\n')

        else:

            input('\n Serao instalados os seguintes pacotes Python:\n\n Numpy 1.9.2, Future 0.15.0, Scipy 0.16.0, Six 1.9.0, Dateuitl 2.4.2, Pytz 2015.4, Pyparsing 2.0.3, Setuptools 17.1.1, Matplotlib 1.4.3, Lxml 3.4.4, Sqlalchemy 1.0.8 e Obspy 0.10.2.\n\n Pressione qualquer tecla para iniciar a instalaçao...\n')
        
            if not os.path.exists('%s/Bibliotecas'%os.getcwd()):

                print("\n ERRO: Pasta 'Bibliotecas' nao encontrada\n")
                input('\n Pressione qualquer tecla para sair...\n')

            else:

                self.checkSys()

    def checkSys(self):         

        if struct.calcsize("P")*8 == 32:

            try:

                print(' Instalaçao iniciada. Aguarde, isso pode levar alguns minutos.\n')
                print("\n Instalando biblioteca - Numpy...\n")
                output1 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/numpy-1.9.2+unoptimized-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output1)
                print("\n Numpy instalado!\n\n Instalando biblioteca - Six...\n")
                output2 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/six-1.9.0-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output2)
                print("\n Six instalado!\n\n Instalando biblioteca - Dateutil...\n")
                output3 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/python_dateutil-2.4.2-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output3)
                print("\n Dateutil instalado!\n\n Instalando biblioteca - Pytz...\n")
                output4 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/pytz-2015.4-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output4)
                print("\n Pytz instalado!\n\n Instalando biblioteca - Pyparsing...\n")
                output5 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/pyparsing-2.0.3-py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output5)
                print("\n Pyparsing instalado!\n\n Instalando biblioteca - Setutools...\n")
                output6 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/setuptools-17.1.1-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output6)
                print("\n Setuptools instalado!\n\n Instalando biblioteca - Lxml...\n")
                output7 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/lxml-3.4.4-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output7)
                print("\n Setuptools instalado!\n\n Instalando biblioteca - Matplotlib...\n")
                output8 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/matplotlib-1.4.3-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output8)
                print("\n Matplotlib instalado!\n\n Instalando biblioteca - Scipy...\n")
                output9 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/scipy-0.16.0-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output9)
                print("\n Scipy instalado!\n\n Instalando biblioteca - SQLAlchemy...\n")
                output10 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/SQLAlchemy-1.0.8-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output10)
                print("\n SQLAlchemy instalado!\n\n Instalando biblioteca - Future...\n")
                output11 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/future-0.15.0-py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output11)
                print("\nFuture instalado!\n\n Instalando biblioteca - Obspy...\n")
                output12 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/obspy-0.10.2-cp34-none-win32.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output12)
                print("\n Obspy instalado!\n\n Instalaçao concluída! Geosis está pronto para ser executado.\n")
                input('\n Pressione qualquer tecla para sair...\n')

            except:

                print('\n ERRO: estao faltando arquivos na pasta Bibliotecas\n')
                input('\n Pressione qualquer tecla para sair...\n')

        else:

            try:

                print(' Instalaçao iniciada. Aguarde, isso pode levar alguns minutos.\n')
                print(" Instalando biblioteca - Numpy...\n")
                output1 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/numpy-1.9.2+mkl-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output1)
                print("\n Numpy instalado!\n\n Instalando biblioteca - Six...\n")
                output2 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/six-1.9.0-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output2)
                print("\n Six instalado!\n\n Instalando biblioteca - Dateutil...\n")
                output3 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/python_dateutil-2.4.2-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output3)
                print("\n Dateutil instalado!\n\n Instalando biblioteca - Pytz...\n")
                output4 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/pytz-2015.4-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output4)
                print("\n Pytz instalado!\n\n Instalando biblioteca - Pyparsing...\n")
                output5 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/pyparsing-2.0.3-py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output5)
                print("\n Pyparsing instalado!\n\n Instalando biblioteca - Setutools...\n")
                output6 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/setuptools-17.1.1-py2.py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output6)
                print("\n Setuptools instalado!\n\n Instalando biblioteca - Lxml...\n")
                output7 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/lxml-3.4.4-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output7)
                print("\n Lxml instalado!\n\n Instalando biblioteca - Matplotlib...\n")
                output8 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/matplotlib-1.4.3-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output8)
                print("\n Matplotlib instalado!\n\n Instalando biblioteca - Scipy...\n")
                output9 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/scipy-0.16.0rc1-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output9)
                print("\n Scipy instalado!\n\n Instalando biblioteca - SQLAlchemy...\n")
                output10 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/SQLAlchemy-1.0.8-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output10)
                print("\n SQLAlchemy instalado!\n\n Instalando biblioteca - Future...\n")
                output11 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/future-0.15.0-py3-none-any.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output11)
                print("\n Future instalado!\n\n Instalando biblioteca - Obspy...\n")
                output12 = subprocess.check_output('"%s\Scripts\pip.exe" install "%s/Bibliotecas/obspy-0.10.2-cp34-none-win_amd64.whl"'%(sys.exec_prefix,
                                                    os.getcwd()),shell=True)
                print(output12)
                print("\n Obspy instalado!\n\n Instalaçao concluída! Geosis está pronto para ser executado.\n")
                input('\n Pressione qualquer tecla para sair...\n')

            except:

                print('\n ERRO: estao faltando arquivos na pasta Bibliotecas\n')
                input('\n Pressione qualquer tecla para sair...\n')

Instalador()
            
