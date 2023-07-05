# Scraping

For	each URL,	scrapes	the	content	of the	page and removes	stop words, hyphens, punctuation,	etc.
Writes each	URL in a new line in	a	 text	 file, with	 the	remaining	content	of	the	page of	the	URL,	in	the	following	format:

<URL1> -> word1:: f1 word2:: f2

Where	f1 is	the	frequency	of	word1	in	URL1,	f2	is	the	frequency	of	word2	in	URL1

If	there	are	more	webpages	in	the	seed	URL,	uses a tab	for	listing	
those	subsequent	URLs.	Thus,	if	URL1 has	2	URLs	listed	in	that	page,	then	the	text	file	will	include:

<	URL1> -> word1:: f1  word2:: f2

    <URLa> -> word3::f3	 word8::f8  word4::f4
    
    <URLb> -> word1::f1(in URLb)  word2::f2	(in	URLb)
