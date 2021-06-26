from os.path import basename
import re
from django.core.management.base import BaseCommand
from app.models import Sentence

end = re.compile(r'[.!?]')
punc = re.compile(r'''[,;:\()"'_]''')


class Command(BaseCommand):
    help = 'Load sentences from a book in a text file'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        author, book = basename(options['file']).split('.')[0].split('-', 1)
        lines = []
        with open(options['file'], 'r') as f:
            for line in f:
                if line.strip():
                    lines.append(line.strip().lower())

        sentences = []
        for sentence in end.split(' '.join(lines)):
            sentence = sentence.strip()
            sentence = punc.sub('', sentence)
            sentence = sentence.replace('-', ' ')
            sentence = sentence.replace('—', ' ')
            if sentence:
                sentences.append(Sentence(author=author,
                                          book=book,
                                          sentence=sentence))

            if len(sentences) > 999:
                Sentence.objects.bulk_create(sentences)
                sentences = []

        if sentences:
            Sentence.objects.bulk_create(sentences)

        self.stdout.write(self.style.SUCCESS('Successfully loaded %s - %s' % 
                          (author, book)))
