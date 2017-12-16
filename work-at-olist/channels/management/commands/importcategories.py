from django.core.management.base import BaseCommand
from channels.models import Channel


class Command(BaseCommand):
    help = "Import Channel's categories"

    def add_arguments(self, parser):
        parser.add_argument('channel_name', type=str, nargs=1)
        parser.add_argument('file_name', type=str, nargs=1)

    def handle(self, *args, **options):
        channel_name = options['channel_name'][0]
        file_name = options['file_name'][0]

        with open(file_name, 'r') as f:
            read_data = f.read()

        Channel.create_channel_from_txt(channel_name, read_data.strip())

        self.stdout.write(self.style.SUCCESS('Successfully imported'))
