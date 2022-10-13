from django.core.management import BaseCommand, CommandError
from api.models import *
import requests


class StoreLaunchingData:
    def __init__(self, url):
        self.API_LINK = url

    def request(self):
        self.data = requests.get(self.API_LINK)
        self.data_json = self.data.json()

    def variable(self):
        # =======patch=======
        self.patch_small = self.data_json['links']['patch']['small']
        self.patch_large = self.data_json['links']['patch']['large']

        # =======reddit=======
        self.reddit_campaign = self.data_json['links']['reddit']['campaign']
        self.reddit_launch = self.data_json['links']['reddit']['launch']
        self.reddit_media = self.data_json['links']['reddit']['media']
        self.reddit_recovery = self.data_json['links']['reddit']['recovery']

        # =======flickr=======
        self.flickr_small = self.data_json['links']['flickr']['small']
        self.flickr_original = self.data_json['links']['flickr']['original']

        # =======links=======
        self.links_presskit = self.data_json['links']['presskit']
        self.links_webcast = self.data_json['links']['webcast']
        self.links_youtube_id = self.data_json['links']['youtube_id']
        self.links_article = self.data_json['links']['article']
        self.links_wikipedia = self.data_json['links']['wikipedia']

        # =======cores=======

        # =======Results=======
        self.results_fairings = self.data_json['fairings']
        self.results_static_fire_date_utc = self.data_json['static_fire_date_utc']
        self.results_static_fire_date_unix = self.data_json['static_fire_date_unix']
        self.results_net = self.data_json['net']
        self.results_window = self.data_json['window']
        self.results_rocket = self.data_json['rocket']
        self.results_success = self.data_json['success']
        self.results_failures = self.data_json['failures']
        self.results_details = self.data_json['details']
        self.results_crew = self.data_json['crew']
        self.results_ships = self.data_json['ships']
        self.results_capsules = self.data_json['capsules']
        self.results_payloads = self.data_json['payloads']
        self.results_launchpad = self.data_json['launchpad']
        self.results_flight_number = self.data_json['flight_number']
        self.results_name = self.data_json['name']
        self.results_date_utc = self.data_json['date_utc']
        self.results_date_unix = self.data_json['date_unix']
        self.results_date_local = self.data_json['date_local']
        self.results_date_precision = self.data_json['date_precision']
        self.results_upcoming = self.data_json['upcoming']
        self.results_core = self.data_json['cores'][0]
        self.results_auto_update = self.data_json['auto_update']
        self.results_tbd = self.data_json['tbd']
        self.results_launch_library_id = self.data_json['launch_library_id']
        self.id = self.data_json['id']

    def insert_information_in_model(self):
        patch = Patch.objects.create(
            small=self.patch_small,
            large=self.patch_large,
        )

        reddit = Reddit.objects.create(
            campaign=self.reddit_campaign,
            launch=self.reddit_launch,
            media=self.reddit_media,
            recovery=self.reddit_recovery,
        )

        flickr = Flickr.objects.create(
            small=self.flickr_small,
            original=self.flickr_original,
        )

        links = Links.objects.create(
            patch=patch,
            reddit=reddit,
            flickr=flickr,
            presskit=self.links_presskit,
            webcast=self.links_webcast,
            youtube_id=self.links_youtube_id,
            article=self.links_article,
            wikipedia=self.links_wikipedia,
        )

        Results.objects.create(
            fairings=self.results_fairings,
            links=links,
            static_fire_date_utc=self.results_static_fire_date_utc,
            static_fire_date_unix=self.results_static_fire_date_unix,
            net=self.results_net,
            window=self.results_window,
            rocket=self.results_rocket,
            success=self.results_success,
            failures=self.results_failures,
            details=self.results_details,
            crew=self.results_crew,
            ships=self.results_ships,
            capsules=self.results_capsules,
            payloads=self.results_payloads,
            launchpad=self.results_launchpad,
            flight_number=self.results_flight_number,
            name=self.results_name,
            date_utc=self.results_date_utc,
            date_unix=self.results_date_unix,
            date_local=self.results_date_local,
            date_precision=self.results_date_precision,
            upcoming=self.results_upcoming,
            cores=self.results_core,
            auto_update=self.results_auto_update,
            tbd=self.results_tbd,
            launch_library_id=self.results_launch_library_id,
        )


class Command(BaseCommand):
    help = 'testando'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            store_launching_data = StoreLaunchingData(
                url='https://api.spacexdata.com/v5/launches/latest'
            )
            store_launching_data.request()
            store_launching_data.variable()
            store_launching_data.insert_information_in_model()
            self.stdout.write(self.style.SUCCESS(f"Sucesso!!!"))

        except requests.exceptions.JSONDecodeError:
            self.stderr.write("Error na Url!!!")
