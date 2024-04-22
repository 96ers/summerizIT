import axios from 'axios';
import { loginStart, loginFailed, loginSuccess } from './authSlice';
import { registerStart, registerFailed, registerSuccess } from './authSlice';

// API request to login user
export const loginUser = async (user, dispatch, navigate) => {
    dispatch(loginStart());
    try {
        // đính kèm token vào header của request
        const res = await axios.post("/api/v1/login", user);
        dispatch(loginSuccess(res.data));
        navigate("/");
    } catch (err) {
        dispatch(loginFailed());
    }
}

// API request to register user
export const registerUser = async (user, dispatch, navigate) => {
    dispatch(registerStart());
    try {
        const res = await axios.post("/api/v1/register", user);
        dispatch(registerSuccess(res.data));
        navigate("/login");
    } catch (err) {
        dispatch(registerFailed());
    }
}