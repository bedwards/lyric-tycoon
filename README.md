# Lyric Tycoon

Write a song or poem with inspiration from public domain prose.

Song lyrics and poems follow a pattern in their lines' meter and rhyme. Prose does not, but what if we used the computer to find compatible phrases within an author's prose that could be used for the lines of a song or poem.

Writing songs/poems is hard. Creativity is hard. Writing this program is hard, but I only have to do it once, and I can show off my coding skills and get a job. Then we can all reuse it and never have to be creative again! ;-)


## Nerd Alert

This project shows off Brian Edwards' skills with...

* Python (and Django)
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


## Database schema

Five books by Thoreau providing 600k phrases.

    select s.book, count(p.*) from phrase p join sentence s on p.sentence_id = s.id group by s.book;

            book               | count
    ---------------------------+-------
    canoeing_in_the_wilderness |  46002
    thoreau_journal_1          | 177759
    thoreau_journal_2          | 212770
    walden                     | 145538
    walking                    |  17098

Where a `phrase` is a start/end word index pair pointing to a sentence. The meter of the phrase is encoded with 0 meaning unstressed and 1 meaning stressed.

    select sentence_id, start_word_index as start, end_word_index as end, meter from phrase limit 18;

    sentence_id  | start | end |   meter
    -------------+-------+-----+------------
             596 |     0 |   6 | 1111011
             596 |     0 |   7 | 11110111
             596 |     0 |   8 | 111101111
             596 |     0 |   9 | 1111011111
             596 |     1 |   6 | 111011
             596 |     1 |   7 | 1110111
             596 |     1 |   8 | 11101111
             596 |     1 |   9 | 111011111
             596 |     2 |   3 | 1

    select content from sentence where id = 596;

    how could youths better learn to live than by at once trying the experiment of living

So to find a couple of phrases with iambic pentameter...

    select 
      array_to_string((string_to_array(s.content, ' '))[p.start_word_index:p.end_word_index], ' ')
    from phrase p join sentence s on p.sentence_id = s.id
    where meter = '0101010101' limit 12;

                   array_to_string
    ---------------------------------------------
     contains eleven acres mostly growing up
     of the stone a nation hammers goes toward
     are a thousand hacking at the branches of
     the poet or the artist never yet
     in a summer morning having taken my
     the village after hoeing or perhaps
     making another hole directly over it
     the voracious caterpillar when transformed
     to the sick the doctors wisely recommend
     hyde the tinker standing on the gallows was
     and the conversation are about costume
     only divided states and churches it divides

And the poems just write themselves ;-)


## Django, ORM and API

I defined that initial database with straight SQL, because I wasn't exactly sure where I was going, and I didn't want added layers of complexity to get in my way. Now that I have a more concrete idea of how this will work and what it will do, I am going to add a server-side, business-logic layer. Namely I'm going to use Django. More namely, Django ORM to define the database schema and access it in code (as opposed to direct SQL), Django views/serializers to return a JSON representation of the data (and apply any business-logic manipulations), and Django management commands to load the database from text files of various books (again utilizing the ORM instead of straight SQL queries.)

Too make a clear distinction of this V2 of this prototype/app, I'm switching from Thoreau to Twain.

    ./manage.py load_sentences books/twain-tom_sawyer.txt
    Successfully loaded twain - tom_sawyer

    >>> from app.models import Sentence
    >>> Sentence.objects.count()
    4957

Use the httpie command-line client to send a request to the API...

    http localhost:8000/sentences/

    [
        {
            "fields": {
                "author": "twain",
                "book": "tom_sawyer",
                "sentence": "she seldom or never looked through them for so small a thing as a boy they were her state pair the pride of her heart and were built for ???style??? not service she could have seen through a pair of stove lids just as well"
            },
            "model": "app.sentence",
            "pk": 4009
        },
        {
            "fields": {
                "author": "twain",
                "book": "tom_sawyer",
                "sentence": "she looked perplexed for a moment and then said not fiercely but still loud enough for the furniture to hear ???well i lay if i get hold of you i???ll ??? she did not finish for by this time she was bending down and punching under the bed with the broom and so she needed breath to punctuate the punches with"
            },
            "model": "app.sentence",
            "pk": 4010
        }
    ]

That demonstrates the basic workings of the stack. I will add business-logic to give a simpler API tailored to the needs of the front-end. Namely for a sonnet API, we want 14 pairs of rhyming phrases in iambic pentameter.
