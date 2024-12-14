# MIDI Analysis and Neo-Riemannian Theory (NRT) Python Script

This project provides a Python script for analyzing MIDI files and applying **Neo-Riemannian Theory (NRT)** transformations to the chords found within them. The script reads MIDI files, extracts chords, applies transformations such as **Parallel**, **Relative**, and **Leading-tone exchange**, and outputs the resulting chord progressions along with the transformation paths.

## Features
- **MIDI File Analysis**: Analyzes MIDI files, extracts chords, and identifies their root and quality.
- **Neo-Riemannian Transformations**: Applies transformations such as Parallel, Relative, and Leading-tone exchange to chords.
- **Chord Progression**: Outputs the transformation paths between chords and displays the results.
- **Flexible Output**: Prints the transformations that were applied between each chord in the progression.
- **Conflict Resolution**: Handles potential conflicts during branch merging using `git`.

## Requirements

Make sure you have the following dependencies installed:

- **Python 3.x** (preferably Python 3.7 or later)
- **mido** library: Used for reading MIDI files in Python.
- **music21** library: Used for chord analysis.

MIDI Analysis and Neo-Riemannian Theory (NRT) Python Script

This project provides a Python script for analyzing MIDI files and applying Neo-Riemannian Theory (NRT) transformations to the chords found within them. The script reads MIDI files, extracts chords, applies transformations such as Parallel, Relative, and Leading-tone exchange, and outputs the resulting chord progressions along with the transformation paths.

Install the required libraries using pip:

pip install mido music21

Setup and Usage

1. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/ezrasandzerbell/Neo-riemannean-theory-python.git

2. Analyze a MIDI File
To run the script, pass the path of a MIDI file as a command-line argument. For example:

python3 midi_script.py /path/to/your/midi_file.mid

The script will:
1. Read the MIDI file.
2. Extract the chords from the MIDI notes.
3. Apply Neo-Riemannian Theory (NRT) transformations.
4. Output the chord progressions and transformations to the console.

3. Modify the MIDI File
You can modify the script to handle different types of chord transformations or adjust the MIDI file processing logic as needed.

4. Push Changes to GitHub
To push changes to the GitHub repository, make sure you commit your changes first:

git add .
git commit -m "Describe your changes here"
git push origin main  # Or 'master' depending on the branch you're working with

If you encounter issues pushing, you might need to first pull the latest changes:

git pull origin main --rebase

Then you can force-push if necessary:

git push origin main --force

Chord Transformations
This script applies three types of Neo-Riemannian transformations to chords:

1. Parallel (P)
- Converts a major chord to its parallel minor chord and vice versa.

2. Relative (R)
- Converts a major chord to its relative minor (down a minor third) and vice versa.

3. Leading-tone Exchange (L)
- Exchanges a major chord for a minor chord with a leading-tone relationship.

Example Output
After running the script, you may see output like the following:

C# major -> F minor: L

This means that the C# major chord has been transformed into the F minor chord using the Leading-tone Exchange transformation.

Troubleshooting

Git Push Errors
- If you encounter issues with pushing to GitHub, you may need to fetch and merge the latest changes first:

git fetch origin
git merge origin/main

After resolving any conflicts, you can push your changes with:

git push origin main

MIDI Note Errors
- If the script encounters unexpected notes in the MIDI file (e.g., A- or E#), the note_to_int function can be updated to handle these notes gracefully. You can modify the function to map non-standard notes to their correct counterparts (e.g., mapping A- to Ab).

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
- mido: MIDI file processing library for Python.
- music21: Toolkit for analyzing and working with musical notation.
