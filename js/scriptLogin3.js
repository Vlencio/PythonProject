console.log('')
const forms = document.getElementById('formulario');
forms.addEventListener('submit', async function login(event) {
    event.preventDefault();
    let password = document.getElementById('loginPassword').value;
    const responseElement = document.getElementById('responseElement');
    
    password = password.toLowerCase();
    
    if (password == 'tempestade de aço') {
        responseElement.textContent = 'Login bem sucedido.';
        responseElement.className = 'mt-4 text-sm text-green-500';
        
        setTimeout(() => {
            window.location.href = 'login3.html';
        }, 1000);

    } else {
        responseElement.textContent = 'Erro no login.';
        responseElement.className = 'mt-4 text-sm text-red-500';
    }
    


});