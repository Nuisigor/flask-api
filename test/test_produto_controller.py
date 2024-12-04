def test_get_all_produtos(client):
    """Testa o endpoint GET /produto/"""
    response = client.get("/produto/")
    assert response.status_code == 200
    assert response.json == []


def test_create_produto(client):
    """Testa o endpoint POST /produto/"""
    payload = {
        "nome": "Produto Teste",
        "valor": 100.0,
        "eletronico": True
    }
    response = client.post("/produto/", json=payload)
    assert response.status_code == 201
    assert response.json["message"] == "Produto criado com sucesso!"
    assert response.json["data"]["nome"] == payload["nome"]
    assert response.json["data"]["valor"] == payload["valor"]


def test_get_produto_por_id(client):
    payload = {
        "nome": "Produto Teste",
        "valor": 100.0,
        "eletronico": True
    }
    post_response = client.post("/produto/", json=payload)
    produto_id = post_response.json["data"]["id"]

    # Busca o produto pelo ID
    response = client.get(f"/produto/{produto_id}")
    assert response.status_code == 200
    assert response.json["nome"] == payload["nome"]


def test_delete_produto(client):
    payload = {
        "nome": "Produto Teste",
        "valor": 100.0,
        "eletronico": True
    }
    post_response = client.post("/produto/", json=payload)
    produto_id = post_response.json["data"]["id"]

    # Exclui o produto pelo ID
    delete_response = client.delete(f"/produto/{produto_id}")
    assert delete_response.status_code == 200
    assert delete_response.json["message"] == "Produto deletado com sucesso!"

    # Tenta buscar o produto excluído
    get_response = client.get(f"/produto/{produto_id}")
    assert get_response.status_code == 404


def test_create_produto_with_invalid_data(client):
    payload = {
        "nome": "Produto Inválido",
        "valor": -100.0,  # Valor inválido
        "eletronico": True
    }
    response = client.post("/produto/", json=payload)
    assert response.status_code == 400


def test_update_produto_with_invalid_data(client):
    payload = {
        "nome": "Produto Teste",
        "valor": 100.0,
        "eletronico": True
    }
    post_response = client.post("/produto/", json=payload)
    produto_id = post_response.json["data"]["id"]

    invalid_payload = {
        "valor": -100.0  # Valor inválido
    }
    response = client.patch(f"/produto/{produto_id}", json=invalid_payload)
    assert response.status_code == 400

