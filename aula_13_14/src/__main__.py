import time

import schedule
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource


# Função para verificar novos arquivos
def check_for_new_files():
    # Chama o método check_for_new_files da instância
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()


# Agenda a execução da função a cada 10 segundos
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()

# Executa o loop principal
while True:
    schedule.run_pending()
    time.sleep(1)
