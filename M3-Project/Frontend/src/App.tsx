import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import io from "socket.io-client";

const socket = io("http://localhost:5000"); // Replace with the Flask server's URL and port

function App() {
  const [count, setCount] = useState(0);
  const [direction, setDirection] = useState("null");

  function handleKeyPress(event: any) {
    switch (event.key) {
      case "ArrowLeft":
        setDirection("Left");
        break;
      case "ArrowRight":
        setDirection("Right");
        break;
      case "ArrowUp":
        setDirection("Up");
        break;
      case "ArrowDown":
        setDirection("Down");
        break;
      default:
        setDirection("null");
    }
  }

  // Send the direction to the server
  socket.emit("direction_event", { direction });
  console.log(direction);


  function sendEventToServer() {
    // Send an event to the server
    console.log("sent");
    socket.emit("custom_event_name", { message: "Hello from React!" });
  }

  useEffect(() => {
    // Connect to the Socket.IO server
    socket.on('connect', () => {
      console.log('Connected to Flask-SocketIO server');
    });

    // Listen for messages from the server
    socket.on('after connect', (data) => {
      console.log('Received data from Flask-SocketIO:', data);
    });

    window.addEventListener('keydown', handleKeyPress);

    return () => {
      // Disconnect from the Socket.IO server when the component unmounts
      socket.disconnect();
      window.removeEventListener('keydown', handleKeyPress);
    };
  }, []);
  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button
          onClick={() => {
            setCount((count) => count + 1);
            sendEventToServer();
          }}
        >
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
