import { Flex } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import io, { Socket } from "socket.io-client";
import SensorData from "./components/SensorData";
import Controller from "./components/Controller";

const LOCAL_MODE = false;
const RASPI_IP = "192.168.68.110";

function App() {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [pressedKey, setPressedKey] = useState<String | null>(null);

  const [distance, setDistance] = useState(0);
  const [pressure, setPressure] = useState(0);
  const [temperature, setTemperature] = useState(0);

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
    const socket = io(
      LOCAL_MODE ? "http://0.0.0.0:5000" : `http://${RASPI_IP}:5000/`
    );
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
      <Flex h={"100vh"} bg={"gray.100"} direction={"column"}>
        <Flex h={"175px"} w={"100%"}>
          <SensorData
            distance={distance}
            pressure={pressure}
            temperature={temperature}
            xac={0}
            yac={0}
            zac={0}
          />
        </Flex>
        <Flex>
          <Flex w={"50%"}>*</Flex>
          <Flex p={10} w={"50%"}>
            <Controller pressedKey={pressedKey} setPressedKey={setPressedKey} />
          </Flex>
        </Flex>
      </Flex>
    </>
  );
}

export default App;

//
//       <Heading>Temp: {Math.round(temperature)}</Heading>
//       <Heading>Press: {Math.round(pressure)}</Heading>
//       <Heading>Dist: {Math.round(distance)}</Heading>
