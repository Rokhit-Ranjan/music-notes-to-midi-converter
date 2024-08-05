from flask import Flask, request, send_file
from flask_cors import CORS
from midiutil import MIDIFile
import io

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    notes = data['notes'].split()
    
    # Create the MIDIFile Object
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Track")
    midi.addTempo(track, time, 120)
    
    note_map = {
        "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63, "E": 64,
        "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, "Ab": 68, "A": 69,
        "A#": 70, "Bb": 70, "B": 71
    }
    
    duration = 1  # Duration of each note in beats
    for i, note in enumerate(notes):
        midi.addNote(track, 0, note_map[note], time + i, duration, 100)
    
    # Prepare MIDI file as response
    midi_data = io.BytesIO()
    midi.writeFile(midi_data)
    midi_data.seek(0)
    
    return send_file(midi_data, as_attachment=True, download_name='music.mid', mimetype='audio/midi')

if __name__ == '__main__':
    app.run(debug=True)
