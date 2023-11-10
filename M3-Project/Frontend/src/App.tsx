import { Center, Heading } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import io, { Socket } from "socket.io-client";

function App() {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [pressedKey, setPressedKey] = useState<String | null>(null);

  const [distance, setDistance] = useState(0)
  const [pressure, setPressure] = useState(0)
  const [temperature, setTemperature] = useState(0)


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


    // Connect to the Socket.IO server
    socket.on("sensors_updated", (data) => {
      setDistance(data.distance);
      setTemperature(data.temperature);
      setPressure(data.pressure);
      //console.log(data);
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
      <Heading>Temp: {temperature}</Heading>
      <Heading>Press: {pressure}</Heading>
      <Heading>Dist: {distance}</Heading>

    </>
  );
}

export default App;
