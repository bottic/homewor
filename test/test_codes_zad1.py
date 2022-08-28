import pytest
from work_test.scr import get_all_doc_owners_names, get_doc_owner_name, remove_doc_from_shelf, \
    check_document_existance, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    add_new_doc

fixture_for_test_get_doc_owner_name = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов')
]

fixture_for_check_document_existance = [
    ('2207 876234', True),
    ('11-2', True),
    ('10006', True)
]

fixture_for_remove_doc_from_shelf = [
    ('11-2', ['2207 876234', '5455 028765']),
    ('2207 876234', ['5455 028765']),
    ('5455 028765', []),
    ('10006', [])
]

fixture_for_add_new_shelf = [
    ('1', ('1', False)),
    ('11', ('11', True))
]

fixture_for_append_doc_to_shelf = [
    ('1', '1', {'1': ['2207 876234', '11-2', '5455 028765', '1'], '2': ['10006'], '3': []}),
    ('1', '2', {'1': ['2207 876234', '11-2', '5455 028765', '1'], '2': ['10006', '1'], '3': []}),
    ('1', '3', {'1': ['2207 876234', '11-2', '5455 028765', '1'], '2': ['10006', '1'], '3': ['1']}),
    ('1', '4', {'1': ['2207 876234', '11-2', '5455 028765', '1'], '2': ['10006', '1'], '3': ['1'], '4': ['1']})
]

fixture_for_delete_doc = [
    ('2207 876234', ('2207 876234', True)),
    ('11-2', ('11-2', True)),
    ('10006', ('10006', True)),
    ('11', None)
]

fixture_for_get_doc_shelf = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('5455 028765', None),
    ('10006', '2'),
    ('1', None)
]

fixture_for_add_new_doc = [
    (1, 11, 111, 1111, [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                        {'type': 11, 'number': 1, 'name': 111}])
]

fixture_for_move_doc_to_shelf = [
    ('11-2', '2',
     (['2207 876234', '5455 028765'], {'1': ['2207 876234', '5455 028765'], '2': ['10006', '11-2'], '3': []})),
    ('10006', '1', (['11-2'], {'1': ['2207 876234', '5455 028765', '10006'], '2': ['11-2'], '3': []})),
    ('11', '1', (None, {'1': ['2207 876234', '5455 028765', '10006', '11'], '2': ['11-2'], '3': []}))
]


def test_get_all_doc_owners_names():
    assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}


@pytest.mark.parametrize('number, result', fixture_for_test_get_doc_owner_name)
def test_get_doc_owner_name(number, result):
    calc_res = get_doc_owner_name(number)
    assert calc_res == result


@pytest.mark.parametrize('number, result', fixture_for_check_document_existance)
def test_check_document_existance(number, result):
    calc_res = check_document_existance(number)
    assert calc_res == result


@pytest.mark.parametrize('number, result', fixture_for_remove_doc_from_shelf)
def test_remove_doc_from_shelf(number, result):
    calc_res = remove_doc_from_shelf(number)
    assert calc_res == result


@pytest.mark.parametrize('number, result', fixture_for_add_new_shelf)
def test_add_new_shelf(number, result):
    calc_res = add_new_shelf(number)
    assert calc_res == result


@pytest.mark.parametrize('number_doc, number_shelf, result', fixture_for_append_doc_to_shelf)
def test_append_doc_to_shelf(number_doc, number_shelf, result):
    calc_res = append_doc_to_shelf(number_doc, number_shelf)
    assert calc_res == result


@pytest.mark.parametrize('user_doc_number, result', fixture_for_delete_doc)
def test_delete_doc(user_doc_number, result):
    calc_res = delete_doc(user_doc_number)
    assert calc_res == result


@pytest.mark.parametrize('user_doc_number, result', fixture_for_get_doc_shelf)
def test_get_doc_shelf(user_doc_number, result):
    calc_res = get_doc_shelf(user_doc_number)
    assert calc_res == result


@pytest.mark.parametrize('user_doc_number, user_shelf_number, result', fixture_for_move_doc_to_shelf)
def test_move_doc_to_shelf(user_doc_number, user_shelf_number, result):
    calc_res = move_doc_to_shelf(user_doc_number, user_shelf_number)
    assert calc_res == result


@pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result',
                         fixture_for_add_new_doc)
def test_add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result):
    calc_res = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
    assert calc_res == result
