import { createTheme, ThemeProvider } from "@mui/material/styles";
import { LineChart } from "@mui/x-charts/LineChart";
import React, { useEffect } from "react";
import axios from "axios";

const APU_URI = "https://agile-polymer-405915.uc.r.appspot.com";
const GRAPH_RANGE = 10;

const theme = createTheme({
  palette: {
    primary: {
      main: "#030187",
    },
    secondary: {
      main: "#B021F3",
    },
  },
});

interface ISensorData {
  id: number;
  value: number;
  date: string;
}

function App() {
  const [tempData, setTempData] = React.useState<ISensorData[]>([]);
  const [pressData, setPressData] = React.useState<ISensorData[]>([]);
  const [distanceData, setDistanceData] = React.useState<ISensorData[]>([]);
  const [accData, setAccData] = React.useState<ISensorData[]>([]);

  function fetchData() {
    axios.get(`${APU_URI}/BMP280`).then((response) => {
      setTempData(response.data.temp);
      setPressData(response.data.press);
    });

    axios.get(`${APU_URI}/HC_SR04`).then((response) => {
      setDistanceData(response.data);
    });

    axios.get(`${APU_URI}/GY_61`).then((response) => {
      setAccData(response.data);
    });
  }

  useEffect(() => {
    const intervalId = setInterval(fetchData, 2000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        {
          <>
            {tempData.length > 0 ? (
              <LineChart
                xAxis={[
                  {
                    data: tempData.slice(-GRAPH_RANGE).map((v, i) => {
                      return i;
                    }),
                    label: "Tiempo",
                  },
                ]}
                series={[
                  {
                    data: tempData.slice(-GRAPH_RANGE).map((v) => v.value),
                    label: "tempData",
                  },
                ]}
                width={500}
                height={300}
              />
            ) : (
              "No tempData"
            )}

            {pressData.length > 0 ? (
              <LineChart
                xAxis={[
                  {
                    data: pressData.slice(-GRAPH_RANGE).map((v, i) => {
                      return i;
                    }),
                    label: "Tiempo",
                  },
                ]}
                series={[
                  {
                    data: pressData.slice(-GRAPH_RANGE).map((v) => v.value),
                    label: "pressData",
                  },
                ]}
                width={500}
                height={300}
              />
            ) : (
              "No pressData"
            )}

            {distanceData.length > 0 ? (
              <LineChart
                xAxis={[
                  {
                    data: distanceData.slice(-GRAPH_RANGE).map((v, i) => {
                      return i;
                    }),
                    label: "Tiempo",
                  },
                ]}
                series={[
                  {
                    data: distanceData.slice(-GRAPH_RANGE).map((v) => v.value),
                    label: "distanceData",
                  },
                ]}
                width={500}
                height={300}
              />
            ) : (
              "No distanceData"
            )}

            {accData.length > 0 ? (
              <LineChart
                xAxis={[
                  {
                    data: accData.slice(-GRAPH_RANGE).map((v, i) => {
                      return i;
                    }),
                    label: "Tiempo",
                  },
                ]}
                series={[
                  {
                    data: accData.slice(-GRAPH_RANGE).map((v) => v.value),
                    label: "accData",
                  },
                ]}
                width={500}
                height={300}
              />
            ) : (
              "No accData"
            )}
          </>
        }
      </div>
    </ThemeProvider>
  );
}

export default App;
