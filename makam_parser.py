import numpy as np

import xml.etree.ElementTree as ET

PITCH_CLASS = {
            'C':0,
            'D':9,
            'E':18,
            'F':22,
            'G':31,
            'A':40,
            'B':44
}

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

def read_score(score_path):
    tree=ET.parse(score_path)
    root=tree.getroot()
    return root

def get_composer_info(root):
    composition_name=root.find('work/work-title').text
    composer_name=root.find('identification/creator').text
    return composition_name,composer_name 

def get_makam_form_usul(root):
    makam_form_usul=root.find('part/measure/direction/direction-type/words').text.split(', ')
    makam=makam_form_usul[0].split(': ')[-1]
    form=makam_form_usul[1].split(': ')[-1]
    usul=makam_form_usul[2].split(': ')[-1][:-1]
    return makam, form, usul

def note_to_number(p,o,a):
    """Convert NoteAEU to AEU53 Comma numbering. """
    if p!='Rest':
        return 53*(int(o)+1) + PITCH_CLASS[p] + ACCIDENTALS[a]
    else:
        return -1

def parse_notes(root, record_embellishment=True):
    """
    Returns a 2D array of [[measure_idx,note_idx,note_duration,note_number, *note_name]]
    Note name can only be "PitchClass Octave", "PitchClass Octave Accidental" or "Rest"
    If a note_name is not Rest and it has zero duration, that note is an embellishment.
    """
    notes=[]
    for m_idx,measure in enumerate(root.findall('part/measure')):   
        if len(measure.findall('note'))>0: # Check if the measure contains at least one note
            grace_count=0 # Count grace notes in case you don't want to record them
            for n_idx,note in enumerate(measure.findall('note')):
                dur=note.find('duration')
                if dur is None:
                    if not record_embellishment:
                        grace_count+=1
                        continue # skip the grace note
                    else:
                        dur='0' # Embellishment/Grace Note
                else:
                    dur=dur.text
                step=note.find('pitch/step')
                if step is not None:
                    step=step.text
                    octave=note.find('pitch/octave').text
                    acc = note.find('accidental')
                    if acc is None:
                        n=[step,octave,'natural']
                    else:
                        n=[step,octave,acc.text]
                else:
                    rest = note.find('rest')
                    assert rest is not None, "The note doesn't have a pitch and is not a rest!"
                    n=['Rest','','']
                note_number=note_to_number(*n)
                note = [m_idx, n_idx-grace_count, dur, note_number, *n]
                notes.append(note)
    return np.array(notes)

def get_time_signatures(root):
    """Returns all time signatures in the score as a list of tupples.
    Assumes it is possible to have time change in makam pieces."""
    beats = [t.text for t in root.findall('part/measure/attributes/time/beats')]
    types = [t.text for t in root.findall('part/measure/attributes/time/beat-type')]
    all_time_signatures=[(int(b),int(t)) for b,t in zip(beats,types)]
    return all_time_signatures

def get_bpm(root):
    return float(root.find('part/measure/direction/sound').attrib['tempo'])

def get_divisions(root):
    return float(root.find('part/measure/attributes/divisions').text)

def find_key_signature_accidentals(root):
    notes, accidentals = [], []
    for k in root.iter('key'):
        for ks in k.findall('key-step'):
            notes.append(ks.text)
        for ka in k.findall('key-accidental'):
            accidentals.append(ka.text)
    return ['{} {}'.format(n,k) for n,k in zip(notes,accidentals)]

def find_all_accidentals(root):
    return set([a.text for a in root.iter('accidental')])

def get_measure_change_indices(composition):
    """Returns the indices of notes in the composition where the next measure begins."""
    measure_indices=composition['notes'][:,0].astype(int)
    measure_changes=np.insert(np.where(np.diff(measure_indices, prepend=0))[0],0,0)
    return measure_changes

def find_return_to_tonic_durations(composition):
    """Find out how many notes it took between two tonic apppearances"""
    note_array=composition['notes'][:,3].astype(int)
    tonic_positions=np.where((note_array%53)==composition['tonic'])[0]
    return_to_tonic_durations=np.diff(tonic_positions)
    return return_to_tonic_durations

def find_return_to_tonic_ranges(piece):
    """Excluding the rests, finds out the pitch range between each tonic appearances."""
    note_array=piece['notes'][:,3].astype(int)
    note_array=note_array[note_array!=-1] # remove rests for calculating pitch range
    tonic_positions=np.where((note_array%53)==piece['tonic'])[0]    
    ranges=[]
    for i in range(len(tonic_positions)-1):
        s_idx, e_idx = tonic_positions[i],tonic_positions[i+1]
        tonic=note_array[s_idx] # each note segment starts with a T-53, T, or T+53
        between_two_tonics=note_array[s_idx+1:e_idx] # exclude the tonic
        between_two_tonics-=tonic # center around zero
        if between_two_tonics.size>0:
            if np.all(between_two_tonics>0): # If all notes greater than tonic
                max_note=between_two_tonics.max()
                min_note=0
            elif np.all(between_two_tonics<0): # If all notes smaller than tonic
                max_note=0
                min_note=between_two_tonics.min()
            else: # Up and down
                max_note=between_two_tonics.max()
                min_note=between_two_tonics.min()
            ranges.append(max_note-min_note)
    return ranges

def get_melodic_contour(piece):
    values = piece['notes'][:, 3].astype(np.int64)
    values = values[values!=-1]
    return np.array(values)

def sort_dict_by_key(dct):
    return {k:dct[k] for k in sorted(dct.keys())}