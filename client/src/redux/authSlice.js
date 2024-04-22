import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
  name: "auth",
  initialState: {
    login: {
      user: null,
      isFetching: false,
      error: false,
    },
    register: {
      isFetching: false,
      error: false,
      success: false,
    },
  },
  reducers: {
    loginStart: (state) => {
      state.login.isFetching = true;
      state.login.error = false;
    },
    loginSuccess: (state, action) => {
      state.login.isFetching = false;
      state.login.user = action.payload;
    },
    loginFailed: (state) => {
      state.login.isFetching = false;
      state.login.error = true;
    },
    registerStart: (state) => {
      state.register.isFetching = true;
      state.register.error = false;
      state.register.success = false;
    },
    registerSuccess: (state) => {
      state.register.isFetching = false;
      state.register.success = true;
    },
    registerFailed: (state) => {
      state.register.isFetching = false;
      state.register.error = true;
    },
  },
});

export const { loginStart, loginSuccess, loginFailed } = authSlice.actions;
export const { registerStart, registerSuccess, registerFailed } = authSlice.actions;
export default authSlice.reducer;
