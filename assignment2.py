from PIL import Image, ImageDraw, ImageFont
import os

def create_card(name, father_name, Gender, Country_of_Stay, CNIC_Number, DOB, DOI, Validity, picture_path, output_path):
    # Create a blank white image
    width, height = 550, 250
    card = Image.new('RGB', (width, height), 'lightgreen')
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        small_font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    draw = ImageDraw.Draw(card)

    # Draw the picture
    try:
        picture = Image.open(picture_path).resize((150, 160))
        card.paste(picture, (60, 40))
    except IOError:
        draw.rectangle([50, 50, 200, 200], outline="black", fill="grey")
        draw.text((75, 100), "No Image", fill="black", font=small_font)
    
    # Draw text on the card
    text_x = 220

    draw.text((text_x, 40), f"Name: {name}", fill="black", font=font)
    draw.text((text_x, 60), f"Father's Name: {father_name}", fill="black", font=font)
    draw.text((text_x, 80), f"Gender: {Gender}", fill="black", font=font)
    draw.text((text_x, 100), f"Country of Stay: {Country_of_Stay}", fill="black", font=font)
    draw.text((text_x, 120), f"CNIC Number: {CNIC_Number}", fill="black", font=font)
    draw.text((text_x, 140), f"Date of Birth: {DOB}", fill="black", font=font)
    draw.text((text_x, 160), f"Date of Issuance: {DOI}", fill="black", font=font)
    draw.text((text_x, 180), f"Card Validity: {Validity}", fill="black", font=font)

    # Save the card
    card.save(output_path)

def main():

    name = input("Enter your Name : ")
    father_name = input(" Enter your Father's Name : ")
    Gender = input("Are you Male or Female : ")
    Country_of_Stay = "Pakistan"
    CNIC_Number = input("Input CNIC Number : ")
    DOB = input("Input Date of Birth \"dd-mm-yyyy\" : ")
    DOI = input("Input Date of Issuance \"dd-mm-yyyy\" : ")
    Validity = input("Input CNIC Expiry Date \"dd-mm-yyyy\" : ")
    
    picture_path = "path/pic.jpg"           #define path of your jpg file <c:/desktop/pic.jpg>
    output_path = f"output_card {CNIC_Number}.pdf" # Card will be generated with unique CNIC number
    

# Validate picture path
    if not os.path.isfile(picture_path):
        print(f"Picture file '{picture_path}' not found. Using placeholder.")
        picture_path = None
    
    create_card(name, father_name, Gender, Country_of_Stay, CNIC_Number, DOB, DOI, Validity, picture_path or "placeholder.png", output_path)
    #print(f"Card created and saved as {output_path}")

if __name__ == "__main__":
    main()