from modelo.periodo import Periodo
import os
import re

class PeriodoRepo:
    FILE_REGEX = r'encuesta-dc-([0-9]{4})-([12])C.csv'

    def get_all(self):
        return [self.periodo(file_name) for file_name in os.listdir('data')
                    if self.archivo_valido(file_name)]

    def periodo(self, file_name):
        match = re.match(self.FILE_REGEX, file_name)
        return Periodo(int(match.group(1)), int(match.group(2)))

    def archivo_valido(self, file_name):
        return re.match(self.FILE_REGEX, file_name)
