from django.test import TestCase

from .models import Platform

# Create your tests here.
class PlatformTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. """
        self.assertEqual(True, True)

    def test_platform_pk(self):

        platform = Platform(platform='Netflix', username='test', password='test')
        platform.save()

        self.assertEqual(platform.pk, 1)


class PlatformListViewTests(TestCase):
    def test_multiple_platforms(self):

        # dummy data
        platform1 = Platform.objects.create(platform='Netflix', username='test', password='test')
        platform2 = Platform.objects.create(platform='Hulu', username='test', password='test')

        platform1.save()
        platform2.save()

        # when platform list page requested, get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check if number of platforms passed to the template
        # matches the number of platforms we have in the database.

        responses = response.context['platforms']
        self.assertEqual(len(responses), 2)
      

class PlatformDetailViewTests(TestCase):
    def test_detail_of_platform(self):
        platform = Platform.objects.create(platform='HBO', username='test', password='test')

        pk = platform.pk
        response = self.client.get(f'/{pk}/')

        self.assertEqual(response.status_code, 200)