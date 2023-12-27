note_marker = 0 # Represents the octave of the note
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # List of note names
note_frequencies = {}   # Dictionary to store note frequencies
midi_notes_range = range(12, 118) # MIDI note range from 12 to 117

# Iterate through MIDI notes range
for i in midi_notes_range:
     # Calculate frequency based on MIDI note number
    frequency = round(440 * 2**((i - 69) / 12), 2)

    # Determine note name and index within the octave
    note_index = i % len(note_names)
    note_name = note_names[note_index]

       # Convert note marker to string for appending to note name
    note_marker_str = str(note_marker)

    # Create the full note name with the note marker
    full_note_name = note_name + note_marker_str

     # Store the note frequency in the dictionary
    note_frequencies[full_note_name] = frequency

    # Increment the note marker every 12 notes (an octave)
    if (i + 1) % 12 == 0:
        note_marker += 1

# Print the resulting note frequencies dictionary
print(note_frequencies)