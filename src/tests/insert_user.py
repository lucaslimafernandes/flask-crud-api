import sys

sys.path.append("./")


from models.users import User


def test_insert_user():
    """
        Múltiplo teste, de inserção e delete
    """

    errors = []

    user = User()
    insert = user.insert_user(
        nome='Teste',
        email='teste@teste.com',
        sexo='M',
        data_nascimento='01/01/2000',
        profissao='Engenheiro',
        endereco='Rua Teste, 123'
    )
    
    id_insert = insert['response']['user']['id']

    delete = user.delete_user(id_insert)

    if insert['response']['status'] != 'successful':
        errors.append("Insert operation failed")

    if delete['response']['status'] != 'successful':
        errors.append("Delete operation failed")

    assert not errors
    


def test_insert_update_user():
    """
        Múltiplo teste, de inserção, update e delete
    """

    errors = []

    user = User()
    insert = user.insert_user(
        nome='Teste',
        email='teste@teste.com',
        sexo='M',
        data_nascimento='01/01/2000',
        profissao='Engenheiro',
        endereco='Rua Teste, 123'
    )
    
    id_insert = insert['response']['user']['id']

    dados_update = {
        'email':    'ok@teste.br' ,
        'profissao':    'dev' ,
    }
    update = user.update_user(id_insert, dados_update)



    delete = user.delete_user(id_insert)

    if insert['response']['status'] != 'successful':
        errors.append("Insert operation failed")
    
    if update['response']['status'] != 'successful':
        errors.append("Update operation failed")

    if delete['response']['status'] != 'successful':
        errors.append("Delete operation failed")

    assert not errors


def teste_get_users():
    """
        Teste de resposta do get all users
    """
    user = User()

    res = user.get_all()

    assert isinstance(res, list) == True



