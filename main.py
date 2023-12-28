"""
https://www.reddit.com/r/audioengineering/comments/971wcm/what_causes_popping_sound_synthesis_abrupt_cuts/
So like a sine wave. It gets sent to a speaker in the form of varying voltage levels, right? And those varying voltage levels are translated by the speaker into movements of the cone. Those movements become different levels of air pressure, and that translates to a tone we can hear.

Now let’s say you have some sort of anomaly in the sine wave—say it goes from maximum amplitude to minimum in an instant. The voltage goes from 5v to 0v in that same amount of time, and that voltage gets translated into cone movements and then audible sound. And this is where you get a “pop.” The speaker moves as best it can to follow the sudden voltage drop, and that sudden change in air pressure sounds like a pop.

I have no idea if this is a satisfying answer, but if you clarify your level of knowledge on the topic, I can maybe try to clarify my explanation.

"""
# this is explains note popping very well.

from songs import *
from synth import Note


def main():
    """
    Main function to demonstrate the usage of the Note class for playing and saving songs.
    """
    note = Note()

    # Choose between note.create_and_play or note.create_song_wave.
    # To change the instrument, modify the synth_wave parameter in the play() method.
    song_waveform = note.create_and_play(jingle_bells)  # Play the 'jingle_bells' song
    note.save_wave(f"jingle_bells.wav")  # Save the waveform as a WAV file


if __name__ == "__main__":
    main()

# TODO set up instrument slot
# add other waves
# add envelopes
# filters for low pass, hihg pass, band pass, notch filters
# effects such as reverb, delay, chourus
# maybe add a file with links to subject matrial for people to read up on
# figure out what would be required to be able to play the following songs
# add never going to give. https://musescore.com/punctuationless/never-gonna-give-you-up
# sandstorm https://musescore.com/user/38235231/scores/5114801
# add interface?
