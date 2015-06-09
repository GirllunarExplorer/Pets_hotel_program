# Pets_hotel_program

This program automates the process of going through the petsmarthotel.com survey.  It takes a 16 digit code as an argument:

    python new_coupon.py "0000 0000 0000 0000"

The program opens a page in Firefox and inputs the initial code and clicks through the buttons to get to the final page where the coupon code is printed.  All options are set to "extremely satisfied" as a default, but the other options are stored as variables if the user wishes to change anything.
