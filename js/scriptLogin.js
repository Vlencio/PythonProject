console.log('Bem vinda ao primeiro desafio,como voce pode ver, se trata apenas de uma tela de login, agora, como voce vai conseguir o email e a senha corretas para acessa-lo? Bom, o que devemos fazer antes de podermos fazer login?')
const forms = document.getElementById('formulario');
forms.addEventListener('submit', async function login(event) {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    const responseElement = document.getElementById('responseElement');
    

    const loginData = {
        email: email,
        password: password
    }
    
    try {
        const response = await fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(loginData),
        });
        
        if (response.ok) {
            const data = await response.json();
            responseElement.textContent = data.message || 'Login Bem Sucedido!';
            responseElement.className = 'mt-4 text-sm text-green-500'

            setTimeout(() => {
                window.location.href = 'login2.html';
            }, 1000);
            
        } else {
            const errorData = await response.json();
            responseElement.textContent = errorData.message || 'Erro no login.';
            responseElement.className = 'mt-4 text-sm text-red-500';
            
        }
    } catch (error) {
        responseElement.textContent = 'Erro ao se contectar ao servidor.';
        responseElement.className = 'mt-4 text-sm text-red-500'
    }
});