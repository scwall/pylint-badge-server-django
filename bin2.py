from pylint.pylint_generator import PylintGenerator

test = {'messages': [
    {'message-id': 'C0301', 'message': 'Line too long (105/100)', 'type': 'convention', 'line': 10, 'obj': '',
     'symbol': 'line-too-long', 'path': 'bin1.py', 'module': 'bin1', 'column': 0},
    {'message-id': 'C0330', 'message': "Wrong hanging indentation (add 4 spaces).\n'user_id': 1,\n^   |",
     'type': 'convention', 'line': 41, 'obj': '', 'symbol': 'bad-continuation', 'path': 'bin1.py', 'module': 'bin1',
     'column': 0}, {'message-id': 'C0330',
                    'message': "Wrong hanging indentation (add 4 spaces).\n'repository_id': 1}, SECRET_KEY, algorithm='HS256').decode('utf-8')\n^   |",
                    'type': 'convention', 'line': 42, 'obj': '', 'symbol': 'bad-continuation', 'path': 'bin1.py',
                    'module': 'bin1', 'column': 0},
    {'message-id': 'C0301', 'message': 'Line too long (171/100)', 'type': 'convention', 'line': 43, 'obj': '',
     'symbol': 'line-too-long', 'path': 'bin1.py', 'module': 'bin1', 'column': 0},
    {'message-id': 'C0304', 'message': 'Final newline missing', 'type': 'convention', 'line': 45, 'obj': '',
     'symbol': 'missing-final-newline', 'path': 'bin1.py', 'module': 'bin1', 'column': 0},
    {'message-id': 'C0111', 'message': 'Missing module docstring', 'type': 'convention', 'line': 1, 'obj': '',
     'symbol': 'missing-docstring', 'path': 'bin1.py', 'module': 'bin1', 'column': 0},
    {'message-id': 'C0103', 'message': 'Constant name "token" doesn\'t conform to UPPER_CASE naming style',
     'type': 'convention', 'line': 40, 'obj': '', 'symbol': 'invalid-name', 'path': 'bin1.py', 'module': 'bin1',
     'column': 0},
    {'message-id': 'C0103', 'message': 'Constant name "test" doesn\'t conform to UPPER_CASE naming style',
     'type': 'convention', 'line': 44, 'obj': '', 'symbol': 'invalid-name', 'path': 'bin1.py', 'module': 'bin1',
     'column': 0},
    {'message-id': 'E1101', 'message': "Class 'Repository' has no 'objects' member", 'type': 'error', 'line': 44,
     'obj': '', 'symbol': 'no-member', 'path': 'bin1.py', 'module': 'bin1', 'column': 7}],
        'stats': {'dependencies': {'pylint_badge_server.settings': ['bin1'], 'users.models': ['bin1'], 'jwt': ['bin1']},
                  'class': 0, 'badname_method': 0, 'function': 0, 'refactor': 0, 'undocumented_function': 0,
                  'module': 1, 'by_msg': {'no-member': 1, 'invalid-name': 2, 'bad-continuation': 2, 'line-too-long': 2,
                                          'missing-docstring': 1, 'missing-final-newline': 1}, 'statement': 7,
                  'cycles': [], 'convention': 8, 'badname_const': 2, 'info': 0, 'badname_module': 0,
                  'nb_duplicated_lines': 0, 'badname_argument': 0, 'percent_duplicated_lines': 0.0, 'error': 1,
                  'method': 0, 'badname_class': 0, 'warning': 0, 'undocumented_class': 0, 'badname_inlinevar': 0,
                  'badname_variable': 0, 'badname_function': 0, 'undocumented_method': 0, 'undocumented_module': 1,
                  'fatal': 0, 'by_module': {
                'bin1': {'info': 0, 'convention': 8, 'warning': 0, 'error': 1, 'fatal': 0, 'refactor': 0,
                         'statement': 0}}, 'badname_attr': 0, 'badname_class_attribute': 0}, 'previous': {
        'dependencies': {'pylint_badge_server.settings': ['bin1'], 'users.models': ['bin1'], 'jwt': ['bin1']},
        'class': 0, 'badname_method': 0, 'function': 0, 'total_lines': 47, 'refactor': 0, 'undocumented_function': 0,
        'module': 1,
        'by_msg': {'no-member': 1, 'invalid-name': 2, 'bad-continuation': 2, 'line-too-long': 2, 'missing-docstring': 1,
                   'missing-final-newline': 1}, 'statement': 7, 'cycles': [], 'convention': 8, 'badname_module': 0,
        'info': 0, 'badname_const': 2, 'nb_duplicated_lines': 0, 'badname_function': 0,
        'global_note': -8.571428571428573, 'badname_class': 0, 'percent_duplicated_lines': 0.0, 'error': 1, 'method': 0,
        'by_module': {
            'bin1': {'info': 0, 'convention': 8, 'warning': 0, 'error': 1, 'fatal': 0, 'refactor': 0, 'statement': 0}},
        'badname_argument': 0, 'warning': 0, 'undocumented_class': 0, 'badname_inlinevar': 0, 'badname_variable': 0,
        'code_lines': 8, 'undocumented_method': 0, 'comment_lines': 34, 'empty_lines': 3, 'undocumented_module': 1,
        'fatal': 0, 'docstring_lines': 2, 'badname_attr': 0, 'badname_class_attribute': 0}}

# for message in test['messages']:
#     print(message)
#     print(message['type'])
#     print(message['column'])
pylint = PylintGenerator(test)
