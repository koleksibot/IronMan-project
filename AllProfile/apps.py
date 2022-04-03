from django.apps import AppConfig


class AllprofileConfig(AppConfig):
    name = 'AllProfile'

    def ready(self):
        import AllProfile.AllProfileSignals

