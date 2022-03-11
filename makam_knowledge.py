# Koma values of pitch classes
# a whole tone is 9, semitone is 4 koma
PITCH_CLASS = {
        'C':0,
        'D':9,
        'E':18,
        'F':22,
        'G':31,
        'A':40,
        'B':44
}

PERDE_LOCS=list(PITCH_CLASS.values())

# Koma differences of accidentals
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

# Taken from Yarman 2008
AEU_PERDE = {
            'Kaba Çargah': 0,
            'Kaba Nim Hicaz': 4,
            'Kaba Hicaz': 1,
            'Kaba Dik Hicaz': 3,
            'Yegah': 1,
            'Kaba Nim Hisar': 4,
            'Kaba Hisar': 1,
            'Kaba Dik Hisar': 3,
            'Hüseyni Aşiran': 1,
            'Acem Aşiran': 4,
            'Dik Acem Aşiran': 1,
            'Irak': 3,
            'Geveşt': 1,
            'Dik Geveşt': 3,
            'Rast': 1,
            'Nim Zirgüle': 4,
            'Zirgüle': 1,
            'Dik Zirgüle': 3,
            'Dügah': 1,
            'Kürdi': 4,
            'Dik Kürdi': 1,
            'Segah': 3,
            'Buselik': 1,
            'Dik Buselik': 3,
            'Çargah': 1,
            'Nim Hicaz': 4,
            'Hicaz': 1,
            'Dik Hicaz': 3,
            'Neva': 1,
            'Nim Hisar': 4,
            'Hisar': 1,
            'Dik Hisar': 3,
            'Hüseyni': 1,
            'Acem': 4,
            'Dik Acem': 1,
            'Eviç': 3,
            'Mahur': 1,
            'Dik Mahur': 3,
            'Gerdaniye': 1,
            'Nüm Şehnaz': 4,
            'Şehnaz': 1,
            'Dik Şehnaz': 3,
            'Muhayyer': 1,
            'Sünbüle': 4,
            'Dik Sünbüle': 1,
            'Tiz Segah': 3,
            'Tiz Buselik': 1,
            'Tiz Dik Buselik': 3,
            'Tiz Çargah': 1   
}