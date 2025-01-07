const botao = document.getElementById('botaoCadastrar')

botao.addEventListener('click', async function cadastrar(event) {
    const nome = document.getElementById('nomeInput').value
    const email = document.getElementById('emailInput').value
    const password = document.getElementById('senhaInput').value
    const responseElement = document.getElementById('responseElement')

    const cadastroData = {
        nome: nome,
        email: email,
        password: password
    }

    try {
        response = await fetch('http://127.0.0.1:8000/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(cadastroData)
        })

        if (response.ok) {
            const data = await response.json();
            responseElement.textContent = data.message || 'Cadastro sucedido.'
            responseElement.tagName = 'mt-4 text-sm text-green-500'
        } else {
            const errorData = await response.json();
            responseElement.textContent = errorData.message || 'Erro no cadastro.'
        }
    }
    
})