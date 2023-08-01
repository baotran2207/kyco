import React from 'react';
import { Navigate, Route } from 'react-router-dom';

export const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={(props) =>
      localStorage.getItem('token') ? (
        <Component {...props} />
      ) : (
        <Navigate to={{ pathname: '/login', state: { from: props.location } }} />
      )
    }
  />
);
