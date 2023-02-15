from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        music_articles = [['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_music_keyword_to_titles_results = {'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'and': ['French pop music', 'Edogawa, Tokyo'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}
        self.assertEqual(keyword_to_titles(music_articles), expected_music_keyword_to_titles_results)
        self.assertEqual(keyword_to_titles([]), {})
        wake_forest_article = [["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745, ['the', 'wake', 'forest', 'deacons', 'team', 'ncaa', 'their', '2007', 'all', 'acc', 'first', 'season', 'coach', 'and', '2008', '2009', '2015', '2017', '2016', 'players', 'plays', 'for', 'mls', 'usl', 'united', '2013']]]
        expected_wake_forest_keyword_to_titles_results = {'the': ["Wake Forest Demon Deacons men's soccer"], 'wake': ["Wake Forest Demon Deacons men's soccer"], 'forest': ["Wake Forest Demon Deacons men's soccer"], 'deacons': ["Wake Forest Demon Deacons men's soccer"], 'team': ["Wake Forest Demon Deacons men's soccer"], 'ncaa': ["Wake Forest Demon Deacons men's soccer"], 'their': ["Wake Forest Demon Deacons men's soccer"], '2007': ["Wake Forest Demon Deacons men's soccer"], 'all': ["Wake Forest Demon Deacons men's soccer"], 'acc': ["Wake Forest Demon Deacons men's soccer"], 'first': ["Wake Forest Demon Deacons men's soccer"], 'season': ["Wake Forest Demon Deacons men's soccer"], 'coach': ["Wake Forest Demon Deacons men's soccer"], 'and': ["Wake Forest Demon Deacons men's soccer"], '2008': ["Wake Forest Demon Deacons men's soccer"], '2009': ["Wake Forest Demon Deacons men's soccer"], '2015': ["Wake Forest Demon Deacons men's soccer"], '2017': ["Wake Forest Demon Deacons men's soccer"], '2016': ["Wake Forest Demon Deacons men's soccer"], 'players': ["Wake Forest Demon Deacons men's soccer"], 'plays': ["Wake Forest Demon Deacons men's soccer"], 'for': ["Wake Forest Demon Deacons men's soccer"], 'mls': ["Wake Forest Demon Deacons men's soccer"], 'usl': ["Wake Forest Demon Deacons men's soccer"], 'united': ["Wake Forest Demon Deacons men's soccer"], '2013': ["Wake Forest Demon Deacons men's soccer"]}
        self.assertEqual(keyword_to_titles(wake_forest_article), expected_wake_forest_keyword_to_titles_results)
   
    def test_title_to_info(self):
        music_articles = [['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_music_title_to_info = {'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(music_articles), expected_music_title_to_info)
        self.assertEqual(title_to_info([]),{})
        wake_forest_article = [["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745, ['the', 'wake', 'forest', 'deacons', 'team', 'ncaa', 'their', '2007', 'all', 'acc', 'first', 'season', 'coach', 'and', '2008', '2009', '2015', '2017', '2016', 'players', 'plays', 'for', 'mls', 'usl', 'united', '2013']]]
        expected_wake_forest_title_to_info = {"Wake Forest Demon Deacons men's soccer": {'author': 'Burna Boy', 'timestamp': 1260577388, 'length': 26745}}
        self.assertEqual(title_to_info(wake_forest_article), expected_wake_forest_title_to_info)

    def test_search(self):
        music_keyword_to_titles_results = {'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'and': ['French pop music', 'Edogawa, Tokyo'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}
        expected_search_results = ['French pop music', 'Edogawa, Tokyo']
        self.assertEqual(search('and', music_keyword_to_titles_results), expected_search_results)
        self.assertEqual(search('french', music_keyword_to_titles_results), ['French pop music'])
        self.assertEqual(search('ferrari', music_keyword_to_titles_results), [])
        self.assertEqual(search('car', {}), [])

    def test_article_length(self):
        canadian_article_titles = ['List of Canadian musicians', 'French pop music']
        canadian_title_to_length = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}}        
        self.assertEqual(article_length(0, canadian_article_titles, canadian_title_to_length), [])
        self.assertEqual(article_length(999999999999999, canadian_article_titles, canadian_title_to_length), ['List of Canadian musicians', 'French pop music'])
        self.assertEqual(article_length(21023, canadian_article_titles, canadian_title_to_length), ['List of Canadian musicians', 'French pop music'])
        self.assertEqual(article_length(5569, canadian_article_titles, canadian_title_to_length), ['French pop music'])
        self.assertEqual(article_length(99999999999, [], canadian_title_to_length), [])
        self.assertEqual(article_length(99999999999, canadian_article_titles, {}), [])

    def test_key_by_author(self):
        canadian_article_titles = ['List of Canadian musicians', 'French pop music']
        canadian_title_to_info = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}}
        self.assertEqual(key_by_author(canadian_article_titles, canadian_title_to_info), {'Jack Johnson': ['List of Canadian musicians'], 'Mack Johnson': ['French pop music']})
        self.assertEqual(key_by_author([], canadian_title_to_info), {})
        self.assertEqual(key_by_author([], {}), {})

    def test_filter_to_author(self):
        canadian_article_titles = ['List of Canadian musicians', 'French pop music']
        canadian_title_to_info = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}}
        self.assertEqual(filter_to_author('Jack Johnson', canadian_article_titles, canadian_title_to_info), ['List of Canadian musicians'])
        self.assertEqual(filter_to_author('jack johnson', canadian_article_titles, canadian_title_to_info), [])
        self.assertEqual(filter_to_author('Jack Johnson', [], canadian_title_to_info), [])

 
    def test_filter_out(self):
        keyword_to_titles_dict = {'beach': ['Spain national beach soccer team'], 'soccer': ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'fifa': ['Spain national beach soccer team'], 'johnson': ['Will Johnson (soccer)'], 'canadian': ['Will Johnson (soccer)'], 'player': ['Will Johnson (soccer)'], 'played': ['Will Johnson (soccer)'], 'for': ['Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'league': ['Will Johnson (soccer)'], 'canada': ['Will Johnson (soccer)'], 'was': ['Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'the': ['Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'his': ['Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'and': ['Will Johnson (soccer)', 'Steven Cohen (soccer)'], 'team': ['Will Johnson (soccer)'], 'season': ['Will Johnson (soccer)'], 'after': ['Will Johnson (soccer)'], 'year': ['Will Johnson (soccer)'], 'mls': ['Will Johnson (soccer)'], 'first': ['Will Johnson (soccer)'], 'scored': ['Will Johnson (soccer)'], 'goal': ['Will Johnson (soccer)'], 'with': ['Will Johnson (soccer)'], 'december': ['Will Johnson (soccer)'], '2008': ['Will Johnson (soccer)'], 'real': ['Will Johnson (soccer)'], 'salt': ['Will Johnson (soccer)'], 'lake': ['Will Johnson (soccer)'], 'against': ['Will Johnson (soccer)'], 'cup': ['Will Johnson (soccer)'], '2013': ['Will Johnson (soccer)'], '2016': ['Will Johnson (soccer)'], 'cohen': ['Steven Cohen (soccer)'], 'world': ['Steven Cohen (soccer)'], 'daily': ['Steven Cohen (soccer)'], 'club': ['Steven Cohen (soccer)'], 'liverpool': ['Steven Cohen (soccer)'], 'that': ['Steven Cohen (soccer)']}

        self.assertEqual(filter_out('beach', ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'], keyword_to_titles_dict), ['Will Johnson (soccer)', 'Steven Cohen (soccer)'])
        self.assertEqual(filter_out('randomword', ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'], keyword_to_titles_dict), ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'])
        self.assertEqual(filter_out('', ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'], keyword_to_titles_dict), ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)'])
        self.assertEqual(filter_out('beach', [], keyword_to_titles_dict), [])
        self.assertEqual(filter_out('', [], []), [])
    
    def test_articles_from_year(self):
        title_to_info = {'2018': {'author': 'author_1', 'timestamp': 1520946000.0, 'length': 5}, '2019': {'author': 'author_2', 'timestamp': 1546261200.0, 'length': 6}, 'another_2018': {'author': 'author_1', 'timestamp': 1514725200.0, 'length': 16}}

        self.assertEqual(articles_from_year(2018, ['2018', '2019', 'another_2018'], title_to_info), ['2018', 'another_2018'])
        self.assertEqual(articles_from_year(2019, ['2018', '2019', 'another_2018'], title_to_info), ['2019'])
        self.assertEqual(articles_from_year(2030, ['2018', '2019', 'another_2018'], title_to_info), [])
        self.assertEqual(articles_from_year(2018, [], title_to_info), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_1(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_2(self, input_mock):
        keyword = 'computer'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Mack Johnson': ['Ken Kennedy (computer scientist)'], 'Bearcat': ['Human computer', 'List of dystopian music, TV programs, and games'], 'Gary King': ['Single-board computer'], 'Pegship': ['Personal computer', 'Mode (computer interface)'], 'Mr Jake': ['Digital photography']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_3(self, input_mock):
        keyword = 'program'
        advanced_option = 3
        advanced_response = 'RussBot'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Fisk University']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_4(self, input_mock):
        keyword = 'programming'
        advanced_option = 4
        advanced_response = 'program'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_6(self, input_mock):
        keyword = 'state'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of dystopian music, TV programs, and games', '2009 Louisiana Tech Bulldogs football team', 'Mode (computer interface)']\n"

        self.assertEqual(output, expected)





# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
