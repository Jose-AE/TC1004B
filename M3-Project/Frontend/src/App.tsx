import { Center } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import io, { Socket } from "socket.io-client";

function App() {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [pressedKey, setPressedKey] = useState<String | null>(null);

  function handleKeyDown(e: KeyboardEvent) {
    if (e.key.startsWith("Arrow")) {
      const key = e.key.replace("Arrow", "");
      setPressedKey(key);
    }
  }

  function handleKeyUp(e: KeyboardEvent) {
    if (e.key.startsWith("Arrow")) {
      setPressedKey(null);
    }
  }

  socket?.emit("direction_event", { direction: pressedKey });

  useEffect(() => {
    const socket = io("http://127.0.0.1:5000");
    setSocket(socket);

    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    // Connect to the Socket.IO server
    socket.on("connect", () => {
      console.log("Connected to Flask-SocketIO server");
    });

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
      // Disconnect from the Socket.IO server when the component unmounts
      socket.disconnect();
    };
  }, []);

  return (
    <>
      <Center>{pressedKey ? pressedKey : "None"}</Center>
    </>
  );
}

export default App;
