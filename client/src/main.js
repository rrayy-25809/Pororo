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
    const text = userInput.value.trim(); // 입력값 앞뒤 공백 제거
    userInput.value = ''; // 입력 필드 비우기

    if (text) {
        const formData = new FormData(); // 폼 데이터 객체 생성 (파일 업로드나 POST 요청에 사용)

        formData.append("message", text); // 폼 데이터에 'message' 필드로 사용자 입력 추가
        addMessage(text, 'user'); // 사용자 메시지를 화면에 추가

        const response = await fetch("/chat", { // 서버에 POST 요청 (비동기)
            method: "POST", // HTTP 메서드 지정
            body: formData, // 요청 본문에 폼 데이터 포함
        });

        if (response.ok) { // 응답이 성공적이면
            const json = await response.json(); // 응답을 JSON으로 파싱 (비동기)
            addMessage(json["response"], 'bot'); // 서버 응답 메시지를 화면에 추가
        }
    } else {
        return; // 입력값이 없으면 함수 종료
    }
}

sendBtn.addEventListener('click', sendMessage); // 전송 버튼 클릭 시 sendMessage 실행
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage(); // 엔터키 누르면 sendMessage 실행
});