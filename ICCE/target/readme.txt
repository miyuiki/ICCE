output columns:
userid, OpenC, CloseC, PCC, mobileC, TabletC, bookmarkC, MemoC, MarkerC, PageJumpC, SearchC, PrevC, NextC, BacktrackRate, Readtime, Readpages

����C: �Ӷ��ت�count
ex: PCC = �ӦWuser��devicecode��pc������

��L:
BacktrackRate = PrevC / NextC
MemoC = ADD Memo + Delete Memo + Change Memo
Readtime = sum (userid_CLOSE_eventtime - userid_OPEN_eventtime)
Readpages = sum (userid_CLOSE_pageno - userid_OPEN_pageno + 1)