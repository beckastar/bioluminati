from django.core.management.base import BaseCommand, CommandError
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from biocore.models import Meal


class Command(BaseCommand):
    args = 'start_date end_date'
    help = "Creates meals for a year's burn"
    requires_model_validation = True

    def handle(self, *args, **options):
        if len(args) < 2:
            raise CommandError("start and end dates are required")
        start_date = parse(args[0])
        end_date = parse(args[1])

        message = "Creating meals %s to %s: confirm? " % (start_date, end_date)
        confirmed = raw_input(message)
        if confirmed != 'y':
            print "exiting"
            return

        day = relativedelta(days=1)

        current_date = start_date

        days = []
        while current_date <= end_date:
            days.append(current_date)
            current_date += day

        for current_date in days:
            for is_AM in [True, False]:
                Meal.objects.create(
                    is_am = is_AM,
                    start_time = current_date,
                    kps_needed = 1,
                    sous_needed = 1,
                    courier_needed = False,
                    description = "chef supplies",
                    courier_description  = "comestibles",
                )

