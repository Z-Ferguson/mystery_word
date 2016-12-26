import unittest
from mystery_word import organize_words
from mystery_word import get_random_word


class TestMysteryWordMethods(unittest.TestCase):

    def test_word_organization(self):
        word_list = ['three', 'normals', 'resources']
        easy_words, normal_words, hard_words = organize_words(word_list)
        self.assertEqual(easy_words, ['three'])
        self.assertEqual(normal_words, ['normals'])
        self.assertEqual(hard_words, ['resources'])

    def test_get_random_word(self):
        user_diff_choice_one = 'e'
        user_diff_choice_two = 'n'
        user_diff_choice_three = 'h'
        easy = ['three']
        normal = ['normals']
        hard = ['resources']
        random_word_one = get_random_word(user_diff_choice_one, easy, normal, hard)
        random_word_two = get_random_word(user_diff_choice_two, easy, normal, hard)
        random_word_three = get_random_word(user_diff_choice_three, easy, normal, hard)
        self.assertEqual(random_word_one, 'three')
        self.assertEqual(random_word_two, 'normals')
        self.assertEqual(random_word_three, 'resources')

suite = unittest.TestLoader().loadTestsFromTestCase(TestMysteryWordMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
