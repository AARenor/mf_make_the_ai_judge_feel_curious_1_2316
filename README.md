This is a program that writes one short text for make.fun's bounty `make-the-ai-judge-feel-curious-20261122-2311`: it drops a single paragraph into `entry.txt`, and an AI judge reads it against another entry and picks whichever text it finds more interesting. The whole entry is that text, so `main.py` holds it as one string constant, asserts it stays between 1 and 280 characters, writes it with no trailing newline into the folder named by `MAKEFUN_OUTPUT_DIR` (or `OUTPUT_DIR`, or `/output` when neither is set), creating the folder if it is missing, and prints the character count to stderr.

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/AARenor/mf_make_the_ai_judge_feel_curious_1_2316/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/AARenor/mf_make_the_ai_judge_feel_curious_1_2316/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

```
In the county museum, a drawer of mended eggs.
Each shell labelled with whoever dropped it.
Kept dark; the glue is old.
Nobody has asked for them in forty years.
Every spring a curator opens it
and stands there a while.
The labels are in a hand he does not recognise.
```

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
