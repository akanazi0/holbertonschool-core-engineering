const WS_URL = "ws://localhost:8000/ws";

const statusEl = document.getElementById("status");
const usernameInput = document.getElementById("username");
const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");

function formatTime() {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

function appendMessage(text, type, sender = "") {
  const item = document.createElement("li");
  item.className = `message ${type}`;

  if (type !== "system") {
    const meta = document.createElement("span");
    meta.className = "message-meta";
    meta.textContent = `${sender} • ${formatTime()}`;
    item.appendChild(meta);
  }

  const content = document.createElement("span");
  content.textContent = text;
  item.appendChild(content);

  messagesEl.appendChild(item);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

const socket = new WebSocket(WS_URL);

socket.addEventListener("open", () => {
  statusEl.textContent = "Connected";
  statusEl.className = "status connected";
  sendBtn.disabled = false;
  appendMessage("Connected to server", "system");
});

socket.addEventListener("message", (event) => {
  appendMessage(event.data, "received", "Server");
});

socket.addEventListener("close", () => {
  statusEl.textContent = "Disconnected";
  statusEl.className = "status disconnected";
  sendBtn.disabled = true;
  appendMessage("Connection closed", "system");
});

socket.addEventListener("error", () => {
  appendMessage("WebSocket connection error", "system");
});

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const text = messageInput.value.trim();
  if (!text || socket.readyState !== WebSocket.OPEN) {
    return;
  }

  const username = usernameInput.value.trim() || "Anonymous";
  const payload = `${username}: ${text}`;

  socket.send(payload);
  appendMessage(text, "sent", username);

  messageInput.value = "";
  messageInput.focus();
});
