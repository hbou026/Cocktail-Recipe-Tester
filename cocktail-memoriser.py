# file: cocktail_memorizer.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QTabWidget, QSpacerItem, QSizePolicy

# Example cocktail data
cocktails = [
    {
        'name': 'Gin N Apple',
        'ingredients': ['Gin', 'Lime juice', 'Elderflower syrup', 'Apple juice'],
        'measurements': ['30', '15', '15', '60'],
        'topup': 'None',
        'garnish': ['Rosemary'],
        'glass': 'Cocktail'
    },
    {
        'name': 'U3Voli',
        'ingredients': ['Malibu rum', 'White rum', 'Baileys', 'Milk', 'Raspberry cordial'],
        'measurements': ['30', '15', '30', '30', '30'],
        'topup': 'None',
        'garnish': ['Raspberry', 'Mint'],
        'glass': 'Cocktail'
    },
    {
        'name': 'Thirsty Toby',
        'ingredients': ['Tequila', 'Elderflower Syrup', 'Lime Juice'],
        'measurements': ['30', '30', '30'],
        'topup': 'Lemonade',
        'garnish': ['Raspberry', 'Mint'],
        'glass': 'Short'
    },
    {
        'name': 'NZ Roulette',
        'ingredients': ['White rum', 'Aperol', 'Pineapple Juice', 'Sugar Syrup', 'Lime Juice'],
        'measurements': ['15', '45', '30', '15', '15'],
        'topup': 'None',
        'garnish': ['Mint'],
        'glass': 'Coupe'
    },
    {
        'name': 'Gin Blossom',
        'ingredients': ['Gin', 'Lime juice', 'Mint leaves', 'Pineapple Juice'],
        'measurements': ['30', '15', '4', '60'],
        'topup': 'None',
        'garnish': ['Lemon', 'Mint'],
        'glass': 'Coupe'
    },
    {
        'name': 'Lychee Bellini',
        'ingredients': ['Absolut vodka', 'Lychee syrup', 'Elderflower syrup'],
        'measurements': ['30', '15', '15'],
        'topup': 'Sparkling rose',
        'garnish': ['Lychees x2'],
        'glass': 'Margarita'
    },

    ## INTERNATIONAL COCKTAILS ### (item 7-13)
    {
        'name': 'Cosmopolitan',
        'ingredients': ['Absolut vodka', 'Lime juice', 'Triple sec', 'Cranberry juice', 'Sugar syrup'],
        'measurements': ['30','15','15','60','15'],
        'topup': 'None',
        'garnish': ['Lemon'],
        'glass': 'Cocktail'
    },
    {
        'name': 'Negroni',
        'ingredients': ['Bombay gin','Campari','Vermouth rosso'],
        'measurements': ['30','30','30'],
        'topup': 'None',
        'garnish': ['Orange'],
        'glass': 'Short'
    },
    {
        'name': 'Aperol Spritz',
        'ingredients': ['Aperol','Prosecco'],
        'measurements': ['45','150'],
        'topup': 'Soda water',
        'garnish': ['Orange'],
        'glass': 'Aperol'
    },
    {
        'name': 'Mojito',
        'ingredients': ['Rum','Mint leaves','Lime slice','Lime juice','Sugar syrup'],
        'measurements': ['30','4','1','15','15'],
        'topup': 'Soda water',
        'garnish': ['Lemon','Mint'],
        'glass': 'Tall'
    },
    {
        'name': 'Bloody Mary',
        'ingredients': ['Vodka','Worchestershire sauce','Lime juice','Pepper','Chilli sauce'],
        'measurements': ['30','4','15','dash','4'],
        'topup': 'Tomato juice',
        'garnish': ['Lemon/cucumber'],
        'glass': 'Tall'
    },
    {
        'name': 'Mimosa',
        'ingredients': ['Orange juice'],
        'measurements': ['60'],
        'topup': 'Prosecco',
        'garnish': ['Orange'],
        'glass': 'Sparkling flute'
    },
    {
        'name': 'Old Fashioned',
        'ingredients': ['Jim bean','Bitters','Sugar syrup'],
        'measurements': ['30','5','15'],
        'topup': 'None',
        'garnish': ['Orange','Cherry'],
        'glass': 'Short'
    },
    ### MARTINIS ### (item 14-16)
    {
        'name': 'Espresso Martini',
        'ingredients': ['Absolut vodka','Kahlua','Sugar syrup','Espresso'],
        'measurements': ['30','15','15','60'],
        'topup': 'None',
        'garnish': ['Coffee bean x3'],
        'glass': 'Cocktail'
    },
    {
        'name': 'French Martini',
        'ingredients': ['Absolut vodka','Chambord','Raspberry cordial','Pineapple juice'],
        'measurements': ['30','15','15','90'],
        'topup': 'None',
        'garnish': ['Raspberry'],
        'glass': 'Coupe'
    },
    {
        'name': 'Appletini',
        'ingredients': ['Absolut vodka','Sourz apple', 'Apple juice', 'Green food colour'],
        'measurements': ['30','30','60','1'],
        'topup': 'None',
        'garnish': ['Apple'],
        'glass': 'Cocktail'
    },
    ### MARGARITAS ### (item 17-19)
    {
        'name': 'Classic Margarita',
        'ingredients': ['Tequila','Lime juice','Triple sec','Sugar syrup'],
        'measurements': ['30','60','15','15'],
        'topup': 'None',
        'garnish': ['Salt','Lemon'],
        'glass': 'Margarita'
    },
    {
        'name': 'Spicy Margarita',
        'ingredients': ['Tequila','Lime juice','Triple sec','Sugar syrup','Chilli sauce'],
        'measurements': ['30','60','15','15','4'],
        'topup': 'None',
        'garnish': ['Salt','Chilli flakes','Lemon'],
        'glass': 'Margarita'
    },
    {
        'name': 'Coconut Margarita',
        'ingredients': ['Tequila','Lime juice','Triple sec','Sugar syrup','Coconut milk'],
        'measurements': ['30','30','15','15','30'],
        'topup': 'None',
        'garnish': ['Salt','Lemon'],
        'glass': 'Margarita'
    }

]

class CocktailMemorizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_cocktail_index = 0
        self.update_display()

    def initUI(self):
        self.setWindowTitle('Cocktail Memorizer')

        self.tabs = QTabWidget()
        
        # List tab setup
        listTab = QWidget()
        self.initListTab(listTab)
        
        # Test tab setup
        testTab = QWidget()
        self.initTestTab(testTab)
        
        self.tabs.addTab(listTab, 'Recipes')
        self.tabs.addTab(testTab, 'Test')
        
        self.setCentralWidget(self.tabs)

    def initListTab(self, tab):
        self.cocktail_name_label = QLabel('Cocktail Name', self)
        self.ingredients_label = QLabel('Ingredients', self)
        self.measurements_label = QLabel('Measurements', self)
        self.topup_label = QLabel('Top-Up', self)
        self.garnish_label = QLabel('Garnish', self)
        self.glass_label = QLabel('Glass', self)
        self.index_label = QLabel('Index', self)

        next_button = QPushButton('Next', self)
        next_button.clicked.connect(self.next_cocktail)
        
        prev_button = QPushButton('Previous', self)
        prev_button.clicked.connect(self.prev_cocktail)

        vbox = QVBoxLayout()
        vbox.addWidget(self.cocktail_name_label)
        vbox.addWidget(self.ingredients_label)
        vbox.addWidget(self.measurements_label)
        vbox.addWidget(self.topup_label)
        vbox.addWidget(self.garnish_label)
        vbox.addWidget(self.glass_label)

        index_hbox = QHBoxLayout()
        index_hbox.addStretch(1)
        index_hbox.addWidget(self.index_label)
        index_hbox.addStretch(1)
        vbox.addLayout(index_hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(prev_button)
        hbox.addWidget(next_button)

        vbox.addLayout(hbox)

        tab.setLayout(vbox)

    def initTestTab(self, tab):
        start_quiz_button = QPushButton('Start Quiz', self)
        start_quiz_button.clicked.connect(self.start_quiz)

        vbox = QVBoxLayout()
        vbox.addWidget(start_quiz_button)
        
        tab.setLayout(vbox)

    def update_display(self):
        cocktail = cocktails[self.current_cocktail_index]
        self.cocktail_name_label.setText(f"Cocktail Name: {cocktail['name']}")
        self.ingredients_label.setText("Ingredients: " + ", ".join(cocktail['ingredients']))
        self.measurements_label.setText("Measurements: " + ", ".join(cocktail['measurements']))
        self.topup_label.setText(f"Top-Up: {cocktail['topup']}")
        self.garnish_label.setText("Garnish: " + ", ".join(cocktail['garnish']))
        self.glass_label.setText(f"Glass: {cocktail['glass']}")
        self.index_label.setText(f"{self.current_cocktail_index + 1} of {len(cocktails)}")

    def next_cocktail(self):
        self.current_cocktail_index = (self.current_cocktail_index + 1) % len(cocktails)
        self.update_display()

    def prev_cocktail(self):
        self.current_cocktail_index = (self.current_cocktail_index - 1) % len(cocktails)
        self.update_display()

    def start_quiz(self):
        # Placeholder for quiz functionality
        self.cocktail_name_label.setText("Quiz not implemented yet")

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = CocktailMemorizer()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
