# README

## Introduction
This script is written in Python and uses the `pandas`, `os`, and `PIL` libraries to create image files from data in an Excel file. The Excel file should contain information about the title of the image, the font to be used, the font size, and the color of the image background.

## Prerequisites
To run this script, you will need Python 3 installed on your computer, along with the following libraries:
- pandas
- PIL (Python Imaging Library)

## How to use the script
1. Save an Excel file with the necessary information about the images you want to create. The Excel file should have a header row with the following column names: `title`, `font`, `size`, `color`.
2. In the `save_path` variable, replace the directory path with the directory where you want the image files to be saved.
3. In the `df = pd.read_excel()` line, replace `C:/Excel/file.xlsx` with the path to your Excel file.
4. Run the script.

## Explanation of the script
1. The script imports the necessary libraries: `pandas`, `os`, and `PIL`.
2. It then gets the current working directory and joins it with the desired directory where the image files will be saved.
3. The script reads the Excel file using the `pd.read_excel()` function and stores it in the `df` variable.
4. A loop is used to iterate over each row in the `df` dataframe.
5. The script extracts the necessary information for each image from the row: title, font path, font size, and background color.
6. If the background color is either "transparent" or empty, a transparent image is created using the `Image.new()` function from the PIL library. The text is then added to the image using the `ImageDraw.Draw()` function and the appropriate font and font size. The image is saved as a PNG file with the appropriate file name.
7. If the background color is not transparent or empty, an image with the specified color is created using the `Image.new()` function. The text is then added to the image using the `ImageDraw.Draw()` function and the appropriate font and font size. The image is saved as a PNG file with the appropriate file name.
8. The script prints a message indicating that the image has been saved successfully.
9. The script finishes executing and prints a message indicating that it has finished.
