from pedalboard import Pedalboard, Reverb, load_plugin
from pedalboard.io import AudioFile
import time

start = time.time()

# Let's upload an existing third-party plugin (VST3)
vst = load_plugin("/Library/Audio/Plug-Ins/VST3/Auburn Sounds Graillon 2.vst3")

# Now we print the parameters possessed by the plugins
print(vst.parameters.keys())

# We change the 'pitch_shift_st' parameter so that we have a voice gender transformation. Check it out!
vst.pitch_shift_st = 3.84

# Let's add a stock reverb plugin to the effects chain
board = Pedalboard([vst, Reverb()])

# Let's open an audio file and apply our board
with AudioFile('media/input_file.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

effected = board(audio, samplerate)

# Write the audio back as a wav file:
with AudioFile('media/output_file.wav', 'w', samplerate, effected.shape[0]) as f:
  f.write(effected)

end = time.time()
total_time = end - start
print("\nTime elapsed: " + str(total_time) + " seconds")
