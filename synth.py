import numpy as np
import pyaudio
import wave
from notes import treble_clef


class Note:
    def __init__(self, sampling_rate=44100):
        """
        Initialize a Note object with default values.

        Parameters:
        - sampling_rate: Sampling rate for audio (default is 44100 Hz).
        """
        self.frequency = None
        self.instrument = None
        self.duration = None
        self.sampling_rate = sampling_rate
        self.volume = None
        self.wave = None
        self.w = None

    def sine_wave(self):
        """
        Generate a sine wave for the current note.
        t = time
        """
        t = np.arange(int(self.sampling_rate * self.duration)) / self.sampling_rate
        self.wave = self.volume * np.sin(2 * np.pi * self.frequency * t)

    def square_wave(self):
        """
        Generate a square wave for the current note.
        t = time
        """
        t = np.arange(int(self.sampling_rate * self.duration)) / self.sampling_rate
        self.wave = self.volume * np.sign(np.sin(2 * np.pi * self.frequency * t))

    def triangle_wave(self):
        """
        Generate a triangle wave for the current note.
        t = time
        """
        t = np.arange(int(self.sampling_rate * self.duration)) / self.sampling_rate
        self.wave = (
            self.volume
            * (2 / np.pi)
            * np.arcsin(np.sin(2 * np.pi * self.frequency * t))
        )

    def sawtooth_wave(self):
        """
        Generate a sawtooth wave for the current note.
        t = time
        """
        t = np.arange(int(self.sampling_rate * self.duration)) / self.sampling_rate
        self.wave = self.volume * (
            2 * (self.frequency * t - np.floor(0.5 + self.frequency * t))
        )

    def bell_instrument(self):
        # my attempt at trying to make a bell like sound for jingle bells
        t = np.arange(int(self.sampling_rate * self.duration)) / self.sampling_rate
        modulation_frequency = 5
        modulate = 0.5 * np.sin(2 * np.pi * modulation_frequency * t) + 0.5
        self.wave *= modulate

    def fade_in(self):
        """
        Apply fade-in to the beginning of the note's wave.
        """
        fade_samples = int(0.05 * self.sampling_rate)  # Adjust the fade-in duration
        fade = np.linspace(0, 1, fade_samples)
        self.wave[:fade_samples] *= fade

    def fade_out(self):
        """
        Apply fade-out to the end of the note's wave.
        handles note popping
        setting up a attack decay sustain release would probably be a better idea?
        """
        fade_samples = int(0.05 * self.sampling_rate)  # Adjust the fade-out duration
        fade = np.linspace(1, 0, fade_samples)
        self.wave[-fade_samples:] *= fade

    def apply_fades(self):
        # self.fade_in()
        self.fade_out()

    def play(self, song_sequence):
        """
        Play a sequence of notes.

        Parameters:
        - song_sequence: List of tuples containing note information (name, instrument, duration, volume).
        """
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paFloat32, channels=1, rate=self.sampling_rate, output=True
        )

        for note_info in song_sequence:
            note_name, instrument, duration, volume = note_info
            self.frequency = treble_clef[note_name]
            self.duration = duration
            self.volume = volume

            # change what wave you want to use here.
            self.sine_wave()

            # things that come after the wave/ossilator change how it sounds like the apply_fades as a exmaple here.
            self.apply_fades()

            stream.write(self.wave.astype(np.float32).tobytes())

        stream.stop_stream()
        stream.close()
        p.terminate()

    def create_song_wave(self, song_sequence):
        """
        Create a waveform for a sequence of notes.

        Parameters:
        - song_sequence: List of tuples containing note information (name, instrument, duration, volume).
        """
        song_wave = np.array([])

        for note_info in song_sequence:
            note_name, instrument, duration, volume = note_info
            self.frequency = treble_clef[note_name]
            self.duration = duration
            self.volume = volume

            # change what wave you want to use here.
            self.sine_wave()

            # things that come after the wave/ossilator change how it sounds like the apply_fades as a exmaple here.
            self.apply_fades()

            if self.wave is not None:
                song_wave = np.concatenate((song_wave, self.wave), axis=None)

        self.w = song_wave

    def create_and_play(self, song_sequence):
        """
        Create a waveform for a sequence of notes and play it.

        Parameters:
        - song_sequence: List of tuples containing note information (name, instrument, duration, volume).
        """

        song_wave = np.array([])

        # Play the song while creating the waveform
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paFloat32, channels=1, rate=self.sampling_rate, output=True
        )

        for note_info in song_sequence:
            note_name, instrument, duration, volume = note_info
            self.frequency = treble_clef[note_name]
            self.duration = duration
            self.volume = volume

            # change what wave you want to use here.
            self.sine_wave()

            # things that come after the wave/ossilator change how it sounds like the apply_fades as a exmaple here.
            self.apply_fades()

            if self.wave is not None:
                song_wave = np.concatenate((song_wave, self.wave), axis=None)
                stream.write(self.wave.astype(np.float32).tobytes())

        stream.stop_stream()
        stream.close()
        p.terminate()

        self.w = song_wave

    def save_wave(self, file_path):
        """
        Save the generated waveform to a WAV file.

        Parameters:
        - file_path: Path to the WAV file.
        """
        if self.w is not None:
            scaled_wave = np.int16(self.w * 32767)

            with wave.open(file_path, "w") as wave_file:
                wave_file.setnchannels(1)  # Mono
                wave_file.setsampwidth(2)  # 2 bytes for 16-bit PCM
                wave_file.setframerate(self.sampling_rate)
                wave_file.writeframes(scaled_wave.tobytes())
        else:
            print("Waveform not generated. Call a waveform generation method first.")
