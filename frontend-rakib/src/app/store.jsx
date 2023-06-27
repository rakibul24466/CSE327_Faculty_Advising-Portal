import { configureStore } from "@reduxjs/toolkit";
import roleinfoReducer from "../features/roleSlice";
import userinfoReducer from "../features/userinfoSlice";
export const store = configureStore({
    reducer: {
        //posts: postReducer,
        userinfo: userinfoReducer,
        roleinfo: roleinfoReducer,
    },
    //   middleware: (getDefaultMiddleware) =>
    //     getDefaultMiddleware().concat([
    //     ]),
});
