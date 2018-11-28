# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet  # We will code our `Repository` class in `app/models.py`
from app.db import TweetRepository


class TestRepository(TestCase):
    def test_instance_variables(self):
        repository = TweetRepository()
        self.assertEqual(len(repository.tweets), 0)

    # not good as we test all things in one test !!
    def test_repository_populate(self):
        # Create an instance of the `Repository`
        repository = TweetRepository()
        for i in range(1, 4):
            tweet = Tweet(f"my tweet #{i}")
            tweet_id = repository.add(tweet)
            self.assertEqual(tweet_id, i)
            self.assertIsInstance(repository.get(1), Tweet)
        self.assertEqual(len(repository.tweets), 3)

    def test_add_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(len(repository.tweets), 1)

    def test_auto_increment_of_ids(self):
        repository = TweetRepository()
        first_tweet = Tweet("a first tweet")
        repository.add(first_tweet)
        self.assertEqual(first_tweet.id, 1)
        second_tweet = Tweet("a second tweet")
        repository.add(second_tweet)
        self.assertEqual(second_tweet.id, 2)

    def test_get_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(tweet, repository.get(1))
        self.assertIsNone(repository.get(2))
