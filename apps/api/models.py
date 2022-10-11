from django.db import models


class SpaceX(models.Model):
    message = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name_plural = 'Space X'


class Results(models.Model):
    static_fire_date_utc = models.DateTimeField(
        null=True,
        blank=True
    )

    static_fire_date_unix = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )

    net = models.BooleanField(
        null=True,
        blank=True
    )

    window = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    rocket = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    success = models.BooleanField(
        null=True,
        blank=True
    )

    failures_ships = models.JSONField(
        null=True,
        blank=True
    )

    details = models.TextField(
        max_length=255,
        null=True,
        blank=True
    )

    crew_ships = models.JSONField(
        null=True,
        blank=True
    )

    ships_ships = models.JSONField(
        null=True,
        blank=True
    )

    capsules_ships = models.JSONField(
        null=True,
        blank=True
    )

    payloads_ships = models.JSONField(
        null=True,
        blank=True
    )

    launchpad = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    flight_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_utc = models.DateTimeField(
        null=True,
        blank=True)
    date_unix = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )

    date_local = models.DateTimeField(
        null=True,
        blank=True
    )

    date_precision = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    upcoming = models.BooleanField(
        null=True,
        blank=True
    )

    cores = models.JSONField(
        null=True,
        blank=True
    )

    auto_update = models.BooleanField(
        null=True,
        blank=True
    )

    tbd = models.BooleanField(
        null=True,
        blank=True
    )

    launch_library_id = models.BooleanField(
        null=True,
        blank=True
    )

    iid = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Results'


class Fairings(models.Model):
    reused = models.BooleanField(
        null=True,
        blank=True
    )

    recovery_attempt = models.BooleanField(
        null=True,
        blank=True
    )

    recovered = models.BooleanField(
        null=True,
        blank=True
    )

    ships = models.JSONField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Fairings'


class Links(models.Model):
    presskit = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    webcast = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    youtube_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    article = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    wikipedia = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Links'


class Patch(models.Model):
    small = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    large = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )


class Reddit(models.Model):
    campaign = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    launch = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    media = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    recovery = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )


class Flickr(models.Model):
    small_ships = models.JSONField(
        null=True,
        blank=True
    )

    original = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

class Result(models.Model):
    spacex_api = models.JSONField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Result'