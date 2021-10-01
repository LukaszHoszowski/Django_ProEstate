def create_email_subject_neighbour(first_name, last_name, username):
    if first_name is None or last_name is None or username is None:
        raise ValueError(f'Wrong user data')

    return f"Prośba o kontakt od użytkownika {first_name} {last_name} ({username})"


def create_email_message_neighbour(flat, phone, email, first_name, last_name, contact_flag):
    if first_name is None or \
            last_name is None or \
            flat is None or \
            phone is None or \
            email is None:
        raise ValueError(f'Wrong user data')

    message = f"""Witam,

Jestem Państwa sąsiadem z mieszkania {flat}. 
Bardzo proszę o kontakt pod poniższym numerem telefonu lub przez pocztę elektroniczną:

Telefon: {phone if contact_flag == True else 'Użytkownik nie wyraził zgody na udostępnienie nr telefonu'}
Email: {email} 

Z góry dziękuję i pozdrawiam,
{first_name.title()} {last_name.title()}
     """

    return message


def create_email_subject_failure(building, failure_type):
    if building is None:
        raise ValueError(f'Wrong building data')

    return f"Zgłoszenie awarii - {building} - {failure_type}"


def create_email_message_failure(first_name, last_name, email, username, flat, building, failure_type):
    if username is None or building is None:
        raise ValueError(f'Wrong user or building data')

    message = f"""
    
użytkownik:     {first_name} {last_name} / {email} / {username}
budynek:        {building}
mieszkanie:     {flat}
typ awarii:     {failure_type}
            """

    return message
