import unittest
import os
import sys

sys.path.append(".")
from tempfile import NamedTemporaryFile
from notes import treble_clef
from synth import Note


class TestNoteClass(unittest.TestCase):
    def setUp(self):
        self.note = Note()

    def test_sine_wave(self):
        self.note.frequency = 440  # A4
        self.note.duration = 1.0
        self.note.volume = 0.8
        self.note.sine_wave()
        self.assertIsNotNone(self.note.wave)

    def test_square_wave(self):
        self.note.frequency = 440  # A4
        self.note.duration = 1.0
        self.note.volume = 0.8
        self.note.square_wave()
        self.assertIsNotNone(self.note.wave)

    def test_triangle_wave(self):
        self.note.frequency = 440  # A4
        self.note.duration = 1.0
        self.note.volume = 0.8
        self.note.triangle_wave()
        self.assertIsNotNone(self.note.wave)

    def test_sawtooth_wave(self):
        self.note.frequency = 440  # A4
        self.note.duration = 1.0
        self.note.volume = 0.8
        self.note.sawtooth_wave()
        self.assertIsNotNone(self.note.wave)

    def test_apply_fades(self):
        self.note.frequency = 440  # A4
        self.note.duration = 1.0
        self.note.volume = 0.8
        self.note.sine_wave()
        self.note.apply_fades()
        self.assertIsNotNone(self.note.wave)

    def test_create_and_play(self):
        song_sequence = [("C4", "sine", 1.0, 0.8), ("E4", "sine", 1.0, 0.8)]
        self.note.create_and_play(song_sequence)
        # Manually verify the audio output

    def test_save_wave(self):
        song_sequence = [("C4", "sine", 1.0, 0.8), ("E4", "sine", 1.0, 0.8)]
        self.note.create_song_wave(song_sequence)

        with NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_file_path = temp_file.name
            self.note.save_wave(temp_file_path)
            self.assertTrue(os.path.exists(temp_file_path))

    def tearDown(self):
        pass  # Clean up if needed


if __name__ == "__main__":
    unittest.main()
