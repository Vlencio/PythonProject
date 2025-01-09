console.log('Quarto desafio, estamos na reta final, vamos deixar de lado a brincadeira de criança. Boa sorte procurando a proxima pista.')
const forms = document.getElementById('formulario');
forms.addEventListener('submit', async function login(event) {
    event.preventDefault();
    let password = document.getElementById('loginPassword').value;
    const responseElement = document.getElementById('responseElement');
    
    password = password.toLowerCase();
    
    if (password == 'ratao bola bola') {
        responseElement.textContent = 'Login bem sucedido.';
        responseElement.className = 'mt-4 text-sm text-green-500';
        
        setTimeout(() => {
            window.location.href = 'login4.html';
        }, 1000);

    } else {
        responseElement.textContent = 'Erro no login.';
        responseElement.className = 'mt-4 text-sm text-red-500';
    }
    


});