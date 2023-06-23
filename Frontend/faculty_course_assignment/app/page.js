import Image from "next/image";

// Required imports from the example.
import { TextField, InputAdornment, IconButton } from "@mui/material";
import * as React from "react";
import Stack from "@mui/material/Stack";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import  LoadingButton  from '@mui/lab';

export default function Home() {
  const [showPassword, setShowPassword] = React.useState(false);
  const handleClickShowPassword = () => setShowPassword(!showPassword);
  const handleMouseDownPassword = () => setShowPassword(!showPassword);
  const someChangeHandler = () => {
    console.log("123");
  };
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <Stack spacing={2}>
          <TextField label="your username" id="demo-helper-text-misaligned" />
          <TextField
            label="Password"
            variant="outlined"
            type={showPassword ? "text" : "password"} // <-- This is where the magic happens
            onChange={someChangeHandler}
            InputProps={{
              // <-- This is where the toggle button is added.
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                  >
                    {showPassword ? <Visibility /> : <VisibilityOff />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
          {/* <LoadingButton loading variant="outlined">
            Submit
          </LoadingButton> */}
          
        </Stack>
      </div>
    </main>
  );
}
