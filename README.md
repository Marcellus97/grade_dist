# grade_dist

A lot of python here. I attempted to parse some old pdfs that used to be on Miami University's website.
They contained grade distribution data from every single class from 1999 to 2015.
Every single class, professor, and grade was there.

I thought it would be really cool to parse through these pdfs, extract the data, and store it in a database.
Then maybe display in a grid, filter and sort, etc.

The problem is pdf parsing is...difficult. THere are around ~50 pdfs. Each pdf has ~500 pages.
Automation is the only sane way to approach this.

Unfortunately, pdf parsers can be thrown off by weird pdf fomratting (which isnt exactly standard by the way. 
THe format changes so many times that some data is always corrupted or missing from parsing.

using OCR (optical character recognition) worked better sometimes, but not quite good enough.


with more effort this could be possible...
