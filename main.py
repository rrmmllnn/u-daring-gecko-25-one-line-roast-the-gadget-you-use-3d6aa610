# One roast line about the gadget strapped to the wrist all day.
# The gag: applause for getting up, then a panic alert about getting up.
from pathlib import Path

def build_line():
    opener = "My smartwatch buzzes to congratulate me"
    twist = " for standing, then warns my heart rate"
    punch_a = " is high \u2014 from standing. It's a coach"
    punch_b = ' that cheers the warm-up and reports the workout.'
    return opener + twist + punch_a + punch_b

def run():
    roast = build_line()
    chars = len(roast)
    if not 1 <= chars <= 200:
        raise ValueError(f'roast is {chars} chars, must be 1-200')
    if not roast.strip():
        raise ValueError('roast came out blank')
    out_dir = Path('/output')
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'entry.txt').write_text(roast, encoding='utf-8')

run()
