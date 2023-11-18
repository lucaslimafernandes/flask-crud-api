# def test_insert_user():
#    user = User()
#    response = user.insert_user(
#        nome='Teste',
#        email='teste@teste.com',
#        sexo='M',
#        data_nascimento='01/01/2000',
#        profissao='Engenheiro',
#        endereco='Rua Teste, 123'
#    )
#    assert response['response'] == 'Usuário inserido com sucesso!'


# def test_user_insert_route(client):
#    response = client.post('/user/insert', data={
#        'nome': 'Teste',
#        'email': 'teste@teste.com',
#        'sexo': 'M',
#        'data_nascimento': '01/01/2000',
#        'profissao': 'Engenheiro',
#        'endereco': 'Rua Teste, 123'
#    })
#    assert response.status_code == 200
#    assert 'Usuário inserido com sucesso!' in response.data
