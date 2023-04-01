"""
The enums used in this project - Vocals, Instrument
"""

from enum import Enum


class Vocals(Enum):

    LEAD_VOCALS = 'lead vocals'
    BACKGROUND_VOCALS = 'background vocals'


class Instrument(Enum):

    LEAD_GUITAR = 'lead guitar'
    RHYTHM_GUITAR = 'rhythm guitar'
    BASS = 'bass'
    DRUMS = 'drums'
#%%
