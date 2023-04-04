{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2548c690",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the name (ex:- all letter are in capital):MAX\n",
      "Enter the course name (ex:- all letter are in capital):PYTHON\n",
      "Enter the Date (ex:- March 21,2023):march 25,2023\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image, ImageDraw, ImageFont\n",
    "import secrets\n",
    "\n",
    "background_image = Image.open(\"C:\\\\Users\\\\hp\\\\OneDrive\\\\Desktop\\\\certificate_program\\\\Certificate_Template.png\")\n",
    "\n",
    "certificate = Image.new(\"RGBA\", background_image.size, (680, 1280, 680, 1280))\n",
    "\n",
    "certificate.paste(background_image, (0, 0))\n",
    "\n",
    "draw = ImageDraw.Draw(certificate)\n",
    "\n",
    "font_name = ImageFont.truetype('arial.ttf', size=30)\n",
    "name = str(input('Enter the name (ex:- all letter are in capital):'))\n",
    "draw.text((670,310), f' {name}', fill='white', font=font_name, anchor='ms')\n",
    "\n",
    "font_course = ImageFont.truetype('arial.ttf', size=24)\n",
    "course = str(input('Enter the course name (ex:- all letter are in capital):'))\n",
    "draw.text((680,440), f'{course}', fill='green', font=font_course, anchor='ms')\n",
    "\n",
    "font_Date = ImageFont.truetype('arial.ttf', size=20)\n",
    "Date = str(input('Enter the Date (ex:- March 21,2023):'))\n",
    "draw.text((640,555), f'{Date}', fill='white', font=font_Date, anchor='ms')\n",
    "\n",
    "font_code = ImageFont.truetype('arial.ttf', size=20)\n",
    "code = secrets.token_hex(5).upper()\n",
    "draw.text((300,555), f'{code}', fill='white', font=font_code, anchor='ms')\n",
    "\n",
    "\n",
    "certificate.save('C:\\\\Users\\\\hp\\\\OneDrive\\\\Desktop\\\\certificate_program\\\\generated_certificated_data\\\\Certificate_{}.png'.format(name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a14510ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
