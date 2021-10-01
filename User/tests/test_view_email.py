import pytest

from User.user_helper_functions import create_email_subject_neighbour, create_email_subject_failure, \
    create_email_message_neighbour, create_email_message_failure


def test_email_create_neighbour_subject():
    first_name = 'John'
    last_name = 'Smith'
    username = 'John1908'

    subject = create_email_subject_neighbour(first_name, last_name, username)

    assert 'Prośba o kontakt od użytkownika John Smith (John1908)' == subject


def test_email_create_neighbour_subject_with_incorrect_data():
    first_name = None
    last_name = 'Smith'
    username = 'John1908'

    with pytest.raises(ValueError) as context:
        create_email_subject_neighbour(first_name, last_name, username)

    assert 'Wrong user data' in str(context.value)


def test_email_create_failure_subject():
    building = 'Sesame Street 103'
    failure_type = 'Zalanie'

    subject = create_email_subject_failure(building, failure_type)

    assert 'Zgłoszenie awarii - Sesame Street 103 - Zalanie' == subject


def test_email_create_failure_subject_with_incorrect_data():
    building = None
    failure_type = 'Zalanie'

    with pytest.raises(ValueError) as context:
        create_email_subject_failure(building, failure_type)

    assert 'Wrong building data' in str(context.value)


def test_email_create_neighbour_message():
    flat = 'Sesame Street 103/3'
    phone = 89175852986
    email = 'kermit@hotmail.com'
    first_name = 'kermit'
    last_name = 'defrog'
    contact_flag = True

    message = create_email_message_neighbour(flat, phone, email, first_name, last_name, contact_flag)

    correct_message = """Witam,

Jestem Państwa sąsiadem z mieszkania Sesame Street 103/3. 
Bardzo proszę o kontakt pod poniższym numerem telefonu lub przez pocztę elektroniczną:

Telefon: 89175852986
Email: kermit@hotmail.com 

Z góry dziękuję i pozdrawiam,
Kermit Defrog
     """

    assert correct_message == message


def test_email_create_neighbour_message_flag_false():
    flat = 'Sesame Street 103/3'
    phone = 89175852986
    email = 'kermit@hotmail.com'
    first_name = 'kermit'
    last_name = 'defrog'
    contact_flag = False

    message = create_email_message_neighbour(flat, phone, email, first_name, last_name, contact_flag)

    correct_message = """Witam,

Jestem Państwa sąsiadem z mieszkania Sesame Street 103/3. 
Bardzo proszę o kontakt pod poniższym numerem telefonu lub przez pocztę elektroniczną:

Telefon: Użytkownik nie wyraził zgody na udostępnienie nr telefonu
Email: kermit@hotmail.com 

Z góry dziękuję i pozdrawiam,
Kermit Defrog
     """

    assert correct_message == message


def test_email_create_neighbour_message_with_incorrect_data():
    flat = 'Sesame Street 103/3'
    phone = 89175852986
    email = None
    first_name = 'kermit'
    last_name = 'defrog'
    contact_flag = True

    correct_message = """Witam,

Jestem Państwa sąsiadem z mieszkania Sesame Street 103/3. 
Bardzo proszę o kontakt pod poniższym numerem telefonu lub przez pocztę elektroniczną:

Telefon: 89175852986
Email: kermit@hotmail.com 

Z góry dziękuję i pozdrawiam,
Kermit Defrog
     """

    with pytest.raises(ValueError) as context:
        create_email_message_neighbour(flat, phone, email, first_name, last_name, contact_flag)

    assert 'Wrong user data' in str(context.value)


def test_email_create_failure_message():
    failure_type = 'Zalanie'
    flat = 'Sesame Street 103/3'
    building = 'Sesame Street 103'
    email = 'kermit@hotmail.com'
    first_name = 'kermit'
    last_name = 'defrog'
    username = 'Kermit1999'

    correct_message = """
    
użytkownik:     kermit defrog / kermit@hotmail.com / Kermit1999
budynek:        Sesame Street 103
mieszkanie:     Sesame Street 103/3
typ awarii:     Zalanie
            """

    message = create_email_message_failure(first_name, last_name, email, username, flat, building, failure_type)

    assert correct_message == message


def test_email_create_failure_message_with_incorrect_data():
    failure_type = 'Zalanie'
    flat = 'Sesame Street 103/3'
    building = 'Sesame Street 103'
    email = 'kermit@hotmail.com'
    first_name = 'kermit'
    last_name = 'defrog'
    username = None

    correct_message = """

użytkownik:     kermit defrog / kermit@hotmail.com / Kermit1999
budynek:        Sesame Street 103
mieszkanie:     Sesame Street 103/3
typ awarii:     Zalanie
            """

    with pytest.raises(ValueError) as context:
        create_email_message_failure(first_name, last_name, email, username, flat, building, failure_type)

    assert 'Wrong user or building data' in str(context.value)
