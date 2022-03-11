# Koma values of pitch classes a whole tone is 9, semitone is 4 koma
# Taken from Şentürk 2016
PITCH_CLASS = {
        'C':0,
        'D':9,
        'E':18,
        'F':22,
        'G':31,
        'A':40,
        'B':44
}

# Koma differences of accidentals
# Taken from Şentürk 2016
ACCIDENTALS = {
        'quarter-flat':-1,
        'slash-flat':-4,
        'flat':-5,
        'double-slash-flat':-8,
        'natural': 0,
        'quarter-sharp':+1,
        'sharp':+4,
        'slash-quarter-sharp':+5,  
        'slash-sharp':+8
}

# a tonic reference https://www.researchgate.net/figure/Twenty-four-makams-that-appear-in-this-paper-are-represented-in-the-AEU-system-Special_fig2_276132262
# for those not in the paper, cross-referenced from recordings and other sources e.g. http://muzik.name/
TONICS = {
        'Uşşak': PITCH_CLASS['G'],
        'Nihâvent': PITCH_CLASS['G'],
        'Kürdîlihicazkâr': PITCH_CLASS['D'],
        'Sabâ': PITCH_CLASS['D'],
        'Rast': PITCH_CLASS['C'],
        'Mâhur': PITCH_CLASS['G'],
        'Segâh': PITCH_CLASS['A'] + ACCIDENTALS['sharp'],
        'Hicaz': PITCH_CLASS['G'],
        'Hüseynî': PITCH_CLASS['G'],
        'Bûselik': PITCH_CLASS['G'] + ACCIDENTALS['sharp'],
        'Muhayyer': PITCH_CLASS['G'],
        'Hüzzam': PITCH_CLASS['A'],
        'Hicazkâr': PITCH_CLASS['F'] + ACCIDENTALS['sharp'],
        'Beyâtî': PITCH_CLASS['G'],
        'Karcığar': PITCH_CLASS['A'],
        'Acemaşîrân': PITCH_CLASS['F']
}

# Taken from https://islamansiklopedisi.org.tr/
DOMINANTS ={
        'Uşşak': ['Neva'],
        'Nihâvent': ['Neva'],
        'Kürdîlihicazkâr': ['Gerdaniye'],
        'Sabâ': ['Çargah'],
        'Rast': ['Neva'],
        'Mâhur': ['Gerdaniye'], # Tiz Durak
        'Segâh': ['Neva'],
        'Hicaz': ['Neva'],
        'Hüseynî': ['Hüseyni'],
        'Bûselik': ['Hüseyni', 'Çargah'],
        'Muhayyer': ['Muhayyer', 'Hüseyni'], # Tiz Durak
        'Hüzzam': ['Neva'],
        'Hicazkâr': ['Gerdaniye'], # Tiz Durak
        'Beyâtî': ['Neva'],
        'Karcığar': ['Neva'],
        'Acemaşîrân': ['Acem', 'Çargah', 'Dügah']
}

# Taken from Yarman 2008
AEU_PERDE = {
            'Kaba Çargah': 0,
            'Kaba Nim Hicaz': 4,
            'Kaba Hicaz': 5,
            'Kaba Dik Hicaz': 8,
            'Yegah': 9,
            'Kaba Nim Hisar': 13,
            'Kaba Hisar': 14,
            'Kaba Dik Hisar': 17,
            'Hüseyni Aşiran': 18,
            'Acem Aşiran': 22,
            'Dik Acem Aşiran': 23,
            'Irak': 26,
            'Geveşt': 27,
            'Dik Geveşt': 30,
            'Rast': 31,
            'Nim Zirgüle': 35,
            'Zirgüle': 36,
            'Dik Zirgüle': 39,
            'Dügah': 40,
            'Kürdi': 44,
            'Dik Kürdi': 45,
            'Segah': 48,
            'Buselik': 49,
            'Dik Buselik': 52,
            'Çargah': 53,
            'Nim Hicaz': 57,
            'Hicaz': 58,
            'Dik Hicaz': 61,
            'Neva': 62,
            'Nim Hisar': 66,
            'Hisar': 67,
            'Dik Hisar': 70,
            'Hüseyni': 71,
            'Acem': 75,
            'Dik Acem': 76,
            'Eviç': 79,
            'Mahur': 80,
            'Dik Mahur': 83,
            'Gerdaniye': 84,
            'Nüm Şehnaz': 88,
            'Şehnaz': 89,
            'Dik Şehnaz': 92,
            'Muhayyer': 93,
            'Sünbüle': 97,
            'Dik Sünbüle': 98,
            'Tiz Segah': 101,
            'Tiz Buselik': 102,
            'Tiz Dik Buselik': 105,
            'Tiz Çargah': 106   
}

# Koma values in an octave
AEU_OCTAVE_KOMA=[i for i in list(AEU_PERDE.values()) if i<53]