import api from "./api";
import { loginFailed, loginStart, loginSuccess } from "./authSlice";
import { registerFailed, registerStart, registerSuccess } from "./authSlice";
import { logoutFailed, logoutStart, logoutSuccess } from "./authSlice";

export const loginUser = async (user, dispatch, navigate) => {
  try {
    dispatch(loginStart());
    const res = await api.post("login", user);
    dispatch(loginSuccess(res.data));
    navigate("/auth");
  } catch (error) {
    dispatch(loginFailed());
    // handle error 400
    if (error.response.status === 400) {
      console.log(error.response.data.message);
      throw error.response.data.message;
    }

    // handle error 422
    if (error.response.status === 422) {
      throw "Invalid email or password";
    }
  }
};

export const registerUser = async (user, dispatch, navigate) => {
  dispatch(registerStart());
  try {
    await api.post("register", user);
    dispatch(registerSuccess());
    navigate("/login");
  } catch (error) {
    dispatch(registerFailed());
    if (error.response.status === 400) {
      console.log(error.response.data.message);
      throw error.response.data.message;
    }

    // handle error 422
    if (error.response.status === 422) {
      throw "Invalid email or password";
    }
    console.log(error);
  }
};

export const logOut = async (dispatch, navigate, access_token, user_id) => {
  dispatch(logoutStart());
  try {
    await api.post(
      "logout",
      {},
      {
        // add user_id and access_token to the request headers
        headers: {
          "user-id": user_id,
          "authorization": access_token,
        },
      }
    );
    dispatch(logoutSuccess());
    navigate("/");
  } catch (error) {
    dispatch(logoutFailed());
    console.log(error);
  }
};
