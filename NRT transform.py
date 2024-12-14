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
        if (current_chord.root, current_chord.quality) in visited:
            continue

        visited.add((current_chord.root, current_chord.quality))
        if current_chord.root == end_chord.root and current_chord.quality == end_chord.quality:
            return path

        for t in transformations:
            new_chord = apply_transformation(current_chord, t)
            if (new_chord.root, new_chord.quality) not in visited:
                queue.append((new_chord, path + [t]))

    return None  # No path found

# Updated to handle both sharps and flats
def note_to_int(note):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }
    return note_map[note]

def trace_chord_progression(start_chord, path):
    traced_chords = [str(start_chord)]
    current_chord = start_chord

    for t in path:
        current_chord = apply_transformation(current_chord, t)
        traced_chords.append(str(current_chord))

    return traced_chords

def main():
    import sys

    print("Enter the starting chord (e.g., C major or D# minor):")
    start_input = input().strip().split()
    print("Enter the ending chord (e.g., G major or F# minor):")
    end_input = input().strip().split()

    if len(start_input) != 2 or len(end_input) != 2:
        print("Invalid input. Please use the format 'Note Quality' (e.g., C major).")
        sys.exit(1)

    start_chord = Chord(note_to_int(start_input[0]), start_input[1].lower())
    end_chord = Chord(note_to_int(end_input[0]), end_input[1].lower())

    path = find_transformation_path(start_chord, end_chord)
    if path:
        print(f"Transformation from {start_chord} to {end_chord}: {' -> '.join(path)}")
        print("Chord progression:")
        print(" | ".join(trace_chord_progression(start_chord, path)))
    else:
        print(f"No transformation found from {start_chord} to {end_chord}.")

if __name__ == "__main__":
    main()
