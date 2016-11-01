import ctypes
import fuzzy

def test_basic_soundex():
        soundex = fuzzy.Soundex(4)
        assert soundex('fuzzy') == 'F200'

def test_basic_dmetaphone():
        dmeta = fuzzy.DMetaphone()
        assert dmeta('fuzzy') == ['FS', None]

def test_basic_nysiis():
        assert fuzzy.nysiis('fuzzy') == 'FASY'
