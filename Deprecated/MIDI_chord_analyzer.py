import mido
from music21 import converter, chord
import sys

def analyze_chords(midi_file_path):
    try:
        # Load the MIDI file into music21
        midi_score = converter.parse(midi_file_path)
        
        # Extract simplified chord names from the score
        chord_list = []
        for element in midi_score.recurse():
            if isinstance(element, chord.Chord):
                root = element.root().name
                quality = element.commonName.replace(" triad", "").replace("seventh chord", "7")
                chord_name = f"{root} {quality}"
                chord_list.append(chord_name)

        # Join and print the results
        if chord_list:
            print(" | ".join(chord_list))
        else:
            print("No chords detected.")

    except Exception as e:
        print(f"Error processing MIDI file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python midi_chord_analysis.py <path_to_midi_file>")
    else:
        midi_file_path = sys.argv[1]
        analyze_chords(midi_file_path)
