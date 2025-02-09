import random

class Juego:
    def __init__(self):
        print('----- Piedra Papel Tijera Lagarto Spock -----')

        # Diccionario con las reglas del juego
        self.reglas = {
            'piedra': ['tijeras', 'lagarto'],  # Piedra gana a tijeras y lagarto
            'papel': ['piedra', 'spock'],  # Papel gana a piedra y spock
            'tijeras': ['papel', 'lagarto'],  # Tijeras gana a papel y lagarto
            'lagarto': ['papel', 'spock'],  # Lagarto gana a papel y spock
            'spock': ['piedra', 'tijeras']  # Spock gana a piedra y tijeras
        }

        self.frases = {
            ('piedra', 'tijeras'): '¡Piedra aplasta tijeras!',
            ('piedra', 'lagarto'): '¡Piedra aplasta a lagarto!',
            ('papel', 'piedra'): '¡Papel envuelve a piedra!',
            ('papel', 'spock'): '¡Papel desaprueba a Spock!',
            ('tijeras', 'papel'): '¡Tijeras cortan papel!',
            ('tijeras', 'lagarto'): '¡Tijeras decapitan al lagarto!',
            ('lagarto', 'papel'): '¡Lagarto se come papel!',
            ('lagarto', 'spock'): '¡Lagarto envenena Spock!',
            ('spock', 'piedra'): '¡Spock desintegra piedra!',
            ('spock', 'tijeras'): '¡Spock aplasta tijeras!',
        }

        # Movimientos
        self.movimientos = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']
        self.sheldon = random.choice(self.movimientos)

    def ejecutar_juego(self):

        while True:
            jugador = input('Elige el movimiento: (piedra/papel/tijeras/lagarto/spock): ')

            # Comprobamos si el movimiento es válido
            if jugador not in self.movimientos:
                print("¡Movimiento no válido! Elige entre piedra, papel, tijeras, lagarto o spock.")
                continue  # Volver a pedir el movimiento si no es válido

            if self.sheldon in self.reglas[jugador]:
                print(f'Sheldon sacó {self.sheldon}')
                print(f"¡Ganaste! {self.frases[(jugador, self.sheldon)]}")
                break

            elif jugador in self.reglas[self.sheldon]:
                print(f'Sheldon sacó {self.sheldon}')
                print(f"Perdiste... {self.frases[(self.sheldon, jugador)]}")
                break

            else:
                print("Es un empate...")


