import mido
from music21 import chord, note


def identify_chord(midi_notes):
    try:
        pitches = [note.pitch.midi for note in midi_notes]
        chord_symbol = chord.Chord(pitches)
        if len(pitches) >= 3:  # Only consider full triads
            return chord_symbol.root().name + " " + chord_symbol.quality
        return None
    except Exception as e:
        return None


def analyze_midi_file(filename):
    midi = mido.MidiFile(filename)
    active_notes = set()
    current_time = 0
    chord_progression = []

    for msg in midi:
        current_time += msg.time

        if msg.type == 'note_on' and msg.velocity > 0:
            active_notes.add(msg.note)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            active_notes.discard(msg.note)

        # Analyze when there are active notes
        if active_notes and msg.type in ['note_on', 'note_off']:
            midi_notes = [note.Note(midi_note) for midi_note in active_notes]
            chord_name = identify_chord(midi_notes)
            if chord_name and (not chord_progression or chord_progression[-1] != chord_name):
                chord_progression.append(chord_name)

    print(" | ".join(chord_progression))
    print("\nAnalysis complete.")


if __name__ == "__main__":
    filename = input("Enter the path to your MIDI file: ").strip()
    analyze_midi_file(filename)
