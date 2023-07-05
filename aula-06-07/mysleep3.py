import sys,time,os


def SavePidToFile():
    file = open('mypsleep3Pid.py', 'w')
    file.write(str(os.getpid()))
    file.close()

def getPidFromFile():
    file = open('mypsleep3Pid.py', 'r')
    conteudo = file.read()
    file.close()
    return int(conteudo)

if sys.argv[1] == "/start":
    SavePidToFile()
    time.sleep(1000)
else:
    arq = getPidFromFile()
    os.kill(arq, 9)
    print('matou o safado')

#Rodando no terminal "python sleep.py" em primeiro plano
#Rodando no terminal "pythonw sleep.py" em segundo plano
