output columns:
userid, OpenC, CloseC, PCC, mobileC, TabletC, bookmarkC, MemoC, MarkerC, PageJumpC, SearchC, PrevC, NextC, BacktrackRate, Readtime, Readpages

結尾C: 該項目的count
ex: PCC = 該名user的devicecode為pc的次數

其他:
BacktrackRate = PrevC / NextC
MemoC = ADD Memo + Delete Memo + Change Memo
Readtime = sum (userid_CLOSE_eventtime - userid_OPEN_eventtime)
Readpages = sum (userid_CLOSE_pageno - userid_OPEN_pageno + 1)