from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError

import factories


DEFAULT_NUMBER_OF_ITEMS_TO_CREATE = 1000


class Command(BaseCommand):
    """Create test data."""

    help = "Create test images data."

    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument('--number',
                            action='store',
                            dest='number',
                            type=int,
                            default=DEFAULT_NUMBER_OF_ITEMS_TO_CREATE,
                            help="Number of items to create.")
        parser.add_argument('--no-books',
                            action='store_false',
                            dest='with_images',
                            default=True,
                            help="No images.")

    def handle(self, *args, **options):
        if options.get('number'):
            number = options['number']
        else:
            number = DEFAULT_NUMBER_OF_ITEMS_TO_CREATE

        with_images = bool(options.get('with_images'))

        if with_images:
            try:
                images = factories.BookFactory.create_batch(number)
                print("{} image objects created.".format(number))
            except Exception as err:
                raise CommandError(str(err))

            try:
                image = factories.SingleBookFactory()
                print("A single image object is created.")
            except Exception as err:
                raise CommandError(str(err))

        try:
            addresses = factories.AddressFactory.create_batch(number)
            print("{} address objects created.".format(number))
        except Exception as err:
            raise CommandError(str(err))