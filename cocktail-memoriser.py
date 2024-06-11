import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QTabWidget, QTableWidget, QComboBox, QLineEdit, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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

        self.topup_label.setObjectName('topup_label')
        self.glass_label.setObjectName('glass_label')

        # Connect the buttons to update_display
        next_button.clicked.connect(self.update_display)
        prev_button.clicked.connect(self.update_display)



    def initTestTab(self, tab):
        # Widgets
        self.quiz_cocktail_name_label = QLabel('Cocktail Name', self)
        self.ingredients_table = QTableWidget()
        self.topup_dropdown = QComboBox()  # Define topup_dropdown here
        self.glass_dropdown = QComboBox()
        self.garnish_line_edits = []
        self.garnish_labels = []  # Initialize list for garnish labels
        self.check_button = QPushButton('Check', self)
        self.next_button = QPushButton('Next', self)

        # Set font for quiz cocktail name label
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.quiz_cocktail_name_label.setFont(font)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.quiz_cocktail_name_label)
        vbox.addWidget(self.ingredients_table)
        vbox.addWidget(QLabel('Top-Up', self))
        vbox.addWidget(self.topup_dropdown)  # Add topup_dropdown to the layout
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

        # Set object names for the 'Top-Up' and 'Glass' labels
        for widget in tab.findChildren(QLabel):
            if widget.text() == 'Top-Up':
                widget.setObjectName('Top-Up')  # Set object name for 'Top-Up' label
                self.topup_label = widget
            elif widget.text() == 'Glass':
                widget.setObjectName('Glass')  # Set object name for 'Glass' label
                self.glass_label = widget




    def update_display(self):
        cocktail = cocktails[self.current_cocktail_index]
        self.cocktail_name_label.setText(f"Cocktail Name: {cocktail['name']}")
        self.ingredients_label.setText("Ingredients: " + ", ".join(cocktail['ingredients']))
        self.measurements_label.setText("Measurements: " + ", ".join(cocktail['measurements']))
        self.topup_label.setText(f"Top-Up: {cocktail['topup']}")
        self.garnish_label.setText("Garnish: " + ", ".join(cocktail['garnish']))
        self.glass_label.setText(f"Glass: {cocktail['glass']}")
        self.index_label.setText(f"{self.current_cocktail_index + 1} of {len(cocktails)}")

        # Reset font to normal for all relevant labels and items
        normal_font = QFont()
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLabel) or isinstance(widget, QTableWidgetItem):
                widget.setFont(normal_font)


    def next_cocktail(self):
        self.current_cocktail_index = (self.current_cocktail_index + 1) % len(cocktails)
        self.update_display()

    def prev_cocktail(self):
        self.current_cocktail_index = (self.current_cocktail_index - 1) % len(cocktails)
        self.update_display()

    def start_quiz(self):
        # Select a random cocktail
        self.current_cocktail = random.choice(cocktails)
        
        # Populate UI elements with cocktail data
        self.quiz_cocktail_name_label.setText(f"Cocktail Name: {self.current_cocktail['name']}")
        
        # Populate Ingredients table
        self.ingredients_table.setRowCount(len(self.current_cocktail['ingredients']))
        self.ingredients_table.setColumnCount(2)
        self.ingredients_table.setHorizontalHeaderLabels(["Ingredient", "Measurement"])  # Set column labels
        for i, (ingredient, measurement) in enumerate(zip(self.current_cocktail['ingredients'], self.current_cocktail['measurements'])):
            self.ingredients_table.setItem(i, 0, QTableWidgetItem(''))
            self.ingredients_table.setItem(i, 1, QTableWidgetItem(''))
        
        # Populate Top-Up and Glass dropdowns with empty choices for user input
        self.topup_dropdown.clear()
        self.topup_dropdown.addItems(['--Please choose an option--','None', 'Soda water', 'Lemonade', 'Sparkling rose', 'Tomato juice', 'Prosecco'])
        self.glass_dropdown.clear()
        self.glass_dropdown.addItems(['--Please choose an option--','Cocktail', 'Short', 'Tall', 'Coupe', 'Margarita', 'Aperol', 'Sparkling flute'])

        # Clear Garnish line edits and labels for user input
        for i in range(len(self.garnish_line_edits)):
            self.garnish_line_edits[i].clear()
            self.garnish_line_edits[i].setVisible(i < len(self.current_cocktail['garnish']))
            self.garnish_labels[i].setVisible(i < len(self.current_cocktail['garnish']))

        # Connect buttons
        self.check_button.clicked.connect(self.check_answer)
        self.next_button.clicked.connect(self.start_quiz)

    def check_answer(self):
        # Retrieve the selected cocktail data
        correct_cocktail = self.current_cocktail

        # Reset fonts to normal for all labels
        normal_font = QFont()
        bold_font = QFont()
        bold_font.setBold(True)

        for row in range(self.ingredients_table.rowCount()):
            self.ingredients_table.item(row, 0).setFont(normal_font)
            self.ingredients_table.item(row, 1).setFont(normal_font)

        for label in self.garnish_labels:
            label.setFont(normal_font)

        for widget in self.findChildren(QWidget):
            if widget.objectName() == 'topup_label':
                for child in widget.children():
                 if isinstance(child, QLabel):
                     child.setFont(normal_font)
                break


        for widget in self.findChildren(QWidget):
            if widget.objectName() == 'glass_label':
                for child in widget.children():
                    if isinstance(child, QLabel):
                        child.setFont(normal_font)
                break




        # Check the ingredients and measurements
        ingredient_results = []
        all_ingredients_correct = True
        for i in range(self.ingredients_table.rowCount()):
            entered_ingredient = self.ingredients_table.item(i, 0).text().strip().lower()
            entered_measurement = self.ingredients_table.item(i, 1).text().strip().lower()
            correct_ingredient = correct_cocktail['ingredients'][i].strip().lower()
            correct_measurement = correct_cocktail['measurements'][i].strip().lower()

            if entered_ingredient != correct_ingredient or entered_measurement != correct_measurement:
                ingredient_results.append(f"Incorrect. Correct answer: {i + 1}) {correct_ingredient} ({correct_measurement})")
                all_ingredients_correct = False
                # Bold incorrect entries
                self.ingredients_table.item(i, 0).setFont(bold_font)
                self.ingredients_table.item(i, 1).setFont(bold_font)

        # Display results for ingredients
        if all_ingredients_correct:
            ingredient_result_text = "Correct!"
        else:
            ingredient_result_text = "\n".join(ingredient_results)
        
        ingredient_result_label = QLabel(ingredient_result_text)
        self.ingredients_table.setCellWidget(self.ingredients_table.rowCount(), 0, ingredient_result_label)

        # Check the top-up
        entered_topup = self.topup_dropdown.currentText().strip().lower()
        correct_topup = correct_cocktail['topup'].strip().lower()
        if entered_topup == correct_topup:
            topup_result_text = "Correct!"
        else:
            topup_result_text = f"Incorrect. Correct answer: {correct_topup}"
            # Bold incorrect entry
            self.findChild(QLabel, 'Top-Up').setFont(bold_font)
        
        topup_result_label = QLabel(topup_result_text)
        self.topup_dropdown.setToolTip(topup_result_text)

        # Check the glass
        entered_glass = self.glass_dropdown.currentText().strip().lower()
        correct_glass = correct_cocktail['glass'].strip().lower()
        if entered_glass == correct_glass:
            glass_result_text = "Correct!"
        else:
            glass_result_text = f"Incorrect. Correct answer: {correct_glass}"
            # Bold incorrect entry
            self.findChild(QLabel, 'Glass').setFont(bold_font)
        
        glass_result_label = QLabel(glass_result_text)
        self.glass_dropdown.setToolTip(glass_result_text)

        # Check the garnishes
        garnish_results = []
        all_garnishes_correct = True
        for i in range(len(self.garnish_line_edits)):
            if i < len(correct_cocktail['garnish']):
                entered_garnish = self.garnish_line_edits[i].text().strip().lower()
                correct_garnish = correct_cocktail['garnish'][i].strip().lower()
                if entered_garnish != correct_garnish:
                    garnish_results.append(f"Incorrect. Correct answer: Garnish {i + 1}) {correct_garnish}")
                    all_garnishes_correct = False
                    # Bold incorrect entry
                    self.garnish_labels[i].setFont(bold_font)
        
        # Display results for garnishes
        if all_garnishes_correct:
            garnish_result_text = "Correct!"
        else:
            garnish_result_text = "\n".join(garnish_results)
        
        for i in range(len(self.garnish_line_edits)):
            if i < len(correct_cocktail['garnish']):
                self.garnish_line_edits[i].setToolTip(garnish_result_text if not all_garnishes_correct else "Correct!")
        
        # Display overall result in the status bar
        overall_result_text = "All answers are correct!" if all_ingredients_correct and entered_topup == correct_topup and entered_glass == correct_glass and all_garnishes_correct else "Some answers are incorrect. Please check again."
        self.statusBar().showMessage(overall_result_text, 5000)  # Display message for 5 seconds


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = CocktailMemorizer()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
