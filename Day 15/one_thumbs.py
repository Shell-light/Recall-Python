import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

clip = VideoFileClip(source_path)
print(clip.reader.fps) # frames per second
print(clip.reader.nframes)
print(clip.duration) # second