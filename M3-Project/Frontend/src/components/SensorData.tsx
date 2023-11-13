import {
  Card,
  CardBody,
  CardHeader,
  HStack,
  Heading,
  Badge,
} from "@chakra-ui/react";

function DataSquare({
  name,
  data,
  units,
}: {
  name: string;
  data: number;
  units: string;
}) {
  return (
    <Card w={"350px"}>
      <CardHeader pb={0}>
        <Heading size="lg">{name} </Heading>
      </CardHeader>

      <CardBody pt={0}>
        <Badge mt={2} colorScheme="blue" fontSize={"30px"}>
          {data} {units}
        </Badge>
      </CardBody>
    </Card>
  );
}

interface SensorDataI {
  distance: number;
  pressure: number;
  temperature: number;
  xac: number;
  yac: number;
  zac: number;
}

export default function SensorData({
  distance,
  pressure,
  temperature,
  xac,
  yac,
  zac,
}: SensorDataI) {
  return (
    <HStack w={"100%"} p={5} align="flex-start">
      <DataSquare name="Distance" data={Math.round(distance)} units="m" />
      <DataSquare name="Pressure" data={Math.round(pressure)} units="Pa" />
      <DataSquare
        name="Temperature"
        data={Math.round(temperature)}
        units="°C"
      />
      <DataSquare name="X Acceleration" data={Math.round(xac)} units="m/s²" />
      <DataSquare name="Y Acceleration" data={Math.round(yac)} units="m/s²" />
      <DataSquare name="Z Acceleration" data={Math.round(zac)} units="m/s²" />
    </HStack>
  );
}
