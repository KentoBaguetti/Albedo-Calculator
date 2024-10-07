# Kentaro Barnes
# This was made for calculating the albedo of a surface based on an images
# For EOSC 212 2024 W1

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load and convert the image to grayscale. Darker means lower albedo as more light is absorbed
img = Image.open("SA_12-2020.jpg")
gray_img = img.convert("L")
print("convtered image")

# Convert the image into an array. Each value in the array represents a pixel and its luminosity. 0-255. 255 meaning pure white and 0 meaing pure black
img_array = np.array(gray_img)

# Display the image
plt.imshow(img_array, cmap="gray")
plt.title("Grayscale Image of Surface")
plt.colorbar(label="Pixel Intensity")
plt.show()
print("display image")

# Define the incident light intensity
# I don't know where to get exact data for this from images, so I decied on the value 255 (assuming maximum pixel intensity of 255)
incident_light_intensity = 255

# Calculate albedo for each pixel
# I'm using the equation: Albedo = Reflected light / Incident light, which in this python code becomes Pixel Intensity / Incident light intensity.
# Assuming the light from the sun is the max value and no more light can be reflected than what was sent in
albedo_array = img_array / incident_light_intensity
print("calculated albedo per pixel")

# Display the albedo map
plt.imshow(albedo_array, cmap="gray")
plt.title("Albedo Map")
plt.colorbar(label="Albedo")
plt.show()
print("displaying albedo map")

# Calculate and print the average albedo of the surface
average_albedo = np.mean(albedo_array)
print(f"average albedo of the Surface: {average_albedo:.3f}")
