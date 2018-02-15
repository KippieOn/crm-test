import * as actionType from '../actions/types';

export default function reducer(state = {
  isLoginSuccess: false,
  isLoginPending: false,
  loginError: null,
  token: null,
  email: null,
}, action) {
  switch (action.type) {
    case actionType.SET_LOGIN_PENDING:
      return Object.assign({}, state, {
        isLoginPending: action.isLoginPending
      });

    case actionType.SET_LOGIN_SUCCESS:
      return Object.assign({}, state, {
        isLoginSuccess: action.isLoginSuccess,
      });

    case actionType.SET_USER_LOGIN_DATA:
      console.log(action);
      let newState =  Object.assign({}, state, {
        token: action.token,
        email: action.email,
      });
      console.log(newState);
      return newState;

    case actionType.SET_LOGIN_ERROR:
      return Object.assign({}, state, {
        loginError: action.loginError,
      });

    default:
      return state;
  }
}
