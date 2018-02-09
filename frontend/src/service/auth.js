import AuthAction from '../actions/auth';

const login(username, password) => {
  const authUser = username.trim().toLowerCase();
  let returnData = {}
  if(authUser = "rahul@kippie.co"){
    returnData =  {
      user: 'rahul',
      auth_token: 'rahul',
    };
  } else if (authUser = "issac@kippie.co") {
    returnData =  {
      user: 'issac',
      auth_token: 'issac',
    };
  } else {
    returnData = {
      error: 'Invalid Username or Password';
    };
  }

  if (returnData.user){
    dispatch(AuthAction.loginSuccess(returnData));
  } else {
    dispatch(AuthAction.loginFailed(returnData));
  }

}

const logout = () => {
  
}

export {
  login,
  logout,
}
