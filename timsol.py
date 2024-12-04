# Grammatika sinfini yaratamiz
class Grammatika:
    def __init__(self):
        # Grammatika qoidalarini lug'atda belgilaymiz
        self.grammatika = {
            'S': ['B', 'A1'],
            'A1': ['e', 'A2'],
            'A2': ['h', 'A3'],
            'A3': ['r', 'A4'],
            'A4': ['u', 'A5'],
            'A5': ['z', 'A6'],
            'A6': ['A', 'A7'],
            'A7': ['b', 'A8'],
            'A8': ['d', 'A9'],
            'A9': ['u', 'A10'],
            'A10': ['r', 'A11'],
            'A11': ['a', 'A12'],
            'A12': ['x', 'A13'],
            'A13': ['m', 'A14'],
            'A14': ['o', 'A15'],
            'A15': ['n', 'A16'],
            'A16': ['o', 'A17'],
            'A17': ['v']
        }

    # No-terminalni rekursiv kengaytirish uchun funksiya
    def kengaytirish(self, no_terminal):
        if no_terminal not in self.grammatika:
            return no_terminal
        else:
            natija = ''
            for belgi in self.grammatika[no_terminal]:
                natija += self.kengaytirish(belgi)
            return natija


grammatika = Grammatika()

hosil_qilingan_qator = grammatika.kengaytirish('S')

print(f"Hosil qilingan qator: {hosil_qilingan_qator}")
