import { Card, CardBody, Stack, Heading, IconButton } from "@chakra-ui/react";
import {
  IoArrowBack,
  IoArrowDown,
  IoArrowForward,
  IoArrowUp,
} from "react-icons/io5";

export default function Controller({
  pressedKey,
  setPressedKey,
}: {
  pressedKey: String | null;
  setPressedKey: any;
}) {
  return (
    <>
      <Card>
        <CardBody>
          <Heading textAlign={"center"} mb={"20px"} size="md">
            Car Controls
          </Heading>

          <Stack direction="row" spacing="3" align="center">
            <Stack direction="column" spacing="3" align="center">
              <IconButton
                onClick={() => {
                  setPressedKey("Up");
                }}
                onBlur={() => {
                  setPressedKey(null);
                }}
                bg={pressedKey === "Up" ? "gray.300" : "gray.200"}
                aria-label="Move up"
                icon={<IoArrowUp />}
              />
              <Stack direction="row" spacing="3" align="center">
                <IconButton
                  onClick={() => {
                    setPressedKey("Left");
                  }}
                  bg={pressedKey === "Left" ? "gray.300" : "gray.200"}
                  aria-label="Move left"
                  icon={<IoArrowBack />}
                />
                <IconButton
                  onClick={() => {
                    setPressedKey("Down");
                  }}
                  bg={pressedKey === "Down" ? "gray.300" : "gray.200"}
                  aria-label="Move down"
                  icon={<IoArrowDown />}
                />
                <IconButton
                  onClick={() => {
                    setPressedKey("Right");
                  }}
                  bg={pressedKey === "Right" ? "gray.300" : "gray.200"}
                  aria-label="Move right"
                  icon={<IoArrowForward />}
                />
              </Stack>
            </Stack>
          </Stack>
        </CardBody>
      </Card>
    </>
  );
}
