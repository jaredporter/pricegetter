postcodes = ["E1", "E2", "E3", "E5", "E7", "E8", "E9", "E10", "E13", "E14", "E15", "E16", "E17", "E20", "EC1", "EC2", "EC3", "EC4", "N1", "N2","N3", "N4", "N5", "N6", "N7", "N8", "N10", "N15", "N16", "N17", "N19", "N22", "NW1", "NW2", "NW3", "NW4", "NW5", "NW6", "NW8", "NW11", "SE1", "SE3", "SE4", "SE5", "SE7", "SE8", "SE10", "SE11", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE22", "SE24", "SW1", "SW2", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW10", "SW11", "SW12", "SW18", "W1", "W2", "W3", "W4", "W5", "W6", "W8", "W9", "W10", "W11", "W12", "W14", "WC1", "WC2"]

with open("postcode.txt", "w") as codes:
    for i in postcodes:
        codes.write(i + "\n")

