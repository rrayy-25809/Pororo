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

async function sendMessage() {
    const text = userInput.value.trim();
    userInput.value = '';

    if (text) {
        const formData = new FormData()

        formData.append("message", text)
        addMessage(text, 'user');

        const response = await fetch("/chat", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const json = await response.json();
            addMessage(json["response"], 'bot');
        }
    } else {
        return;
    }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage();
});