    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function addMessage(content, className) {
        const msg = document.createElement('div');
        msg.classList.add('message', className);
        msg.textContent = content;
        chatContainer.appendChild(msg);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;
        addMessage(text, 'user');
        userInput.value = '';
        // Simulated response
        setTimeout(() => {
        addMessage('This is a simulated response from your LLM.', 'bot');
    }, 500);
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') sendMessage();
    });