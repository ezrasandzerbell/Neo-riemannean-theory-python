import mido
from music21 import chord, note

class Chord:
    def __init__(self, root, quality):
        self.root = root  # Root as an integer (e.g., 0 = C, 1 = C#, ..., 11 = B)
        self.quality = quality  # 'major' or 'minor'

    def __repr__(self):
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return f"{note_names[self.root]} {self.quality}"

def apply_transformation(chord, transformation):
    if transformation == 'P':  # Parallel
        return Chord(chord.root, 'minor' if chord.quality == 'major' else 'major')
    elif transformation == 'R':  # Relative
        if chord.quality == 'major':
            return Chord((chord.root + 9) % 12, 'minor')
        elif chord.quality == 'minor':
            return Chord((chord.root + 3) % 12, 'major')
    elif transformation == 'L':  # Leading-tone exchange
        if chord.quality == 'major':
            return Chord((chord.root + 4) % 12, 'minor')
        elif chord.quality == 'minor':
            return Chord((chord.root + 8) % 12, 'major')
    return chord

def find_transformation_path(start_chord, end_chord):
    transformations = ['P', 'R', 'L']
    visited = set()
    queue = [(start_chord, [])]

    while queue:
        current_chord, path = queue.pop(0)

        # Skip self-transformation (no change)
        if current_chord.root == end_chord.root and current_chord.quality == end_chord.quality:
            # If we reached the end chord, stop and return the path
            return path

        # Skip previously visited chords (to avoid infinite loops)
        if (current_chord.root, current_chord.quality) in visited:
            continue

        visited.add((current_chord.root, current_chord.quality))

        # Apply transformations and log if a transformation is actually applied
        for t in transformations:
            new_chord = apply_transformation(current_chord, t)

            # Skip self-transformation (no change)
            if new_chord.root == current_chord.root and new_chord.quality == current_chord.quality:
                continue

            # Only log the transformation when it's a valid change
            if new_chord.root != current_chord.root or new_chord.quality != current_chord.quality:
                # Only log the successful transformation
                if new_chord.root == end_chord.root and new_chord.quality == end_chord.quality:
                    return path + [t]

            # Add new chord to queue if not visited
            if (new_chord.root, new_chord.quality) not in visited:
                queue.append((new_chord, path + [t]))

    return None  # No valid path found

def note_to_int(note):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'A-': 8, 'A': 9, 'A#': 10, 'B-': 10, 'B': 11,
        'E#': 5,  # Add this line to map 'E#' to the same value as 'F'
    }

    # Handle cases like 'A-' by checking if the note includes any non-standard symbols
    if note not in note_map:
        raise ValueError(f"Unexpected note name: {note}")

    return note_map[note]

def trace_chord_progression(start_chord, path):
    traced_chords = [str(start_chord)]
    current_chord = start_chord

    for t in path:
        current_chord = apply_transformation(current_chord, t)
        traced_chords.append(str(current_chord))

    return traced_chords

def identify_chord(midi_notes):
    try:
        pitches = [note.pitch.midi for note in midi_notes]
        chord_symbol = chord.Chord(pitches)
        if len(pitches) >= 3:  # Only consider full triads
            return chord_symbol.root().name, chord_symbol.quality
        return None, None
    except Exception as e:
        return None, None

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

        if active_notes and msg.type in ['note_on', 'note_off']:
            midi_notes = [note.Note(midi_note) for midi_note in active_notes]
            root, quality = identify_chord(midi_notes)
            if root and quality:
                chord_progression.append(Chord(note_to_int(root), quality))

    return chord_progression

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 MIDI_chord_analyzer.py <path_to_midi_file>")
        sys.exit(1)

    filename = sys.argv[1]
    chord_progression = analyze_midi_file(filename)

    for i in range(len(chord_progression) - 1):
        start_chord = chord_progression[i]
        end_chord = chord_progression[i + 1]
        path = find_transformation_path(start_chord, end_chord)
        if path:
            # Only print the result if path is non-empty
            print(f"{start_chord} -> {end_chord}: {' -> '.join(path)}")

if __name__ == "__main__":
    main()
