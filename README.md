# Albedo-Calculator
Calculates the average albedo of an image based on the equation ```Albedo = Reflected Light / Incident Light``` based on the greyscale pixels luminosity of the image

## How to use
1. Clone the repository
2. Create a virtual environment with ```python -m venv venv``` in the terminal
3. Enter the venv with ```source venv/bin/activate``` in the terminal
4. Download the required libraries by entering ```pip3 install -r requirements.txt``` in the terminal
5. In albedo_calc.py switch whats inside ```img = Image.open("SA_12-2020.jpg")``` to whatever image you want to calculate the albedo of
6. Run the python file with ```python3 albedo_calc.py```
7. You'll be given popups of different images (greyscale image, albedo image), to continue to the final value, keep exiting out of the images and the terminal will print the average albedo of the image
8. Optional: Comment out the ```plt.show()``` functions if you don't want to keep exiting out of them
