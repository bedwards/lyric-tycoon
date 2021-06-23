# Lyric Tycoon

Write a song or poem with inspiration from public domain prose.

Song lyrics and poems follow a pattern in their lines' meter and rhyme. Prose does not, but what if we used the computer to find compatible phrases within an author's prose that could be used for the lines of a song or poem.

Writing songs/poems is hard. Creativity is hard. Writing this program is hard, but I only have to do it once, and I can show off my coding skills and get a job. Then we can all reuse it and never have to be creative again! ;-)


## Nerd Alert

This project shows off Brian Edwards' skills with...

* Python
* React
* Redux
* relational databases
* Markdown ;-) (that's a joke)


## How it works

A PostgreSQL database holds all the sentences of prose ever written by Henry David Thoreau. This database encodes the meter of each phrase in each sentence. This is done with the help of the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).

The server-side code is written in Python and uses Django (especially the Django ORM to help interface with the database.) The server-side is mostly just an API for the front-end.

The front-end runs in a web browser and is based on the infamous Mark Zuckerberg's famous React library (that's a joke about it being Mark's invention and about him being infamous.)

Furthermore, I'm going to deploy this thing! That's right, you will be able to use it without figuring out how to build it and deploy it yourself. Happy song/poem writing!


## Component detail: Parser/loader

Parse prose text from Henry David Thoreau. It can be from any author, I just chose Thoreau. [Project Gutenberg](https://www.gutenberg.org/files/205/205-0.txt) is an excellent source for public domain prose.
