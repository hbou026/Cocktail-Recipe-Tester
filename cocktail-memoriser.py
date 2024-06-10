import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QTabWidget, QTableWidget, QComboBox, QLineEdit, QTableWidgetItem

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
        # Widgets
        self.quiz_cocktail_name_label = QLabel('Cocktail Name', self)
        self.ingredients_table = QTableWidget()
        self.topup_dropdown = QComboBox()
        self.glass_dropdown = QComboBox()
        self.garnish_line_edits = []
        self.garnish_labels = []  # Initialize list for garnish labels
        self.check_button = QPushButton('Check', self)
        self.next_button = QPushButton('Next', self)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.quiz_cocktail_name_label)
        vbox.addWidget(self.ingredients_table)
        vbox.addWidget(QLabel('Top-Up', self))
        vbox.addWidget(self.topup_dropdown)
        vbox.addWidget(QLabel('Glass', self))
        vbox.addWidget(self.glass_dropdown)
        
        for i in range(3):  # Assuming maximum 3 garnishes per cocktail
            garnish_label = QLabel(f'Garnish {i + 1}', self)
            self.garnish_labels.append(garnish_label)  # Add label to the list
            garnish_line_edit = QLineEdit()
            self.garnish_line_edits.append(garnish_line_edit)
            vbox.addWidget(garnish_label)
            vbox.addWidget(garnish_line_edit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.check_button)
        hbox.addWidget(self.next_button)
        vbox.addLayout(hbox)

        tab.setLayout(vbox)

        self.start_quiz()


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
        # Select a random cocktail
        cocktail = random.choice(cocktails)
        
        # Populate UI elements with cocktail data
        self.quiz_cocktail_name_label.setText(f"Cocktail Name: {cocktail['name']}")
        
        # Populate Ingredients table
        self.ingredients_table.setRowCount(len(cocktail['ingredients']))
        self.ingredients_table.setColumnCount(2)
        self.ingredients_table.setHorizontalHeaderLabels(["Ingredient", "Measurement"])  # Set column labels
        for i, (ingredient, measurement) in enumerate(zip(cocktail['ingredients'], cocktail['measurements'])):
            self.ingredients_table.setItem(i, 0, QTableWidgetItem(ingredient))
            self.ingredients_table.setItem(i, 1, QTableWidgetItem(measurement))
        
        # Populate Top-Up and Glass dropdowns
        self.topup_dropdown.clear()
        self.topup_dropdown.addItems(['None'] + [cocktail['topup']])
        self.glass_dropdown.clear()
        self.glass_dropdown.addItems([''] + [cocktail['glass']])
        
        # Populate Garnish line edits and labels
        for i, garnish in enumerate(cocktail['garnish']):
            if i < len(self.garnish_line_edits):
                self.garnish_line_edits[i].setText(garnish)
                self.garnish_line_edits[i].setVisible(True)  # Set visibility to True for existing line edits
                self.garnish_labels[i].setVisible(True)  # Set visibility to True for existing labels
            else:
                break
        
        # Hide extra line edits and labels if there are no more garnishes
        for j in range(i + 1, len(self.garnish_line_edits)):
            self.garnish_line_edits[j].setVisible(False)
            self.garnish_labels[j].setVisible(False)
        
        # Connect buttons
        self.check_button.clicked.connect(self.check_answer)
        self.next_button.clicked.connect(self.start_quiz)





    def check_answer(self):
        # Placeholder for checking user's answer
        pass

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = CocktailMemorizer()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
