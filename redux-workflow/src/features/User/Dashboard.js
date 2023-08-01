import React, { Fragment, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { userSelector, fetchUserBytoken, clearState } from './UserSlice';
import { Rings } from 'react-loader-spinner';
import { useNavigate, Outlet, Navigate } from 'react-router-dom';

const Dashboard = () => {
  const navigate = useNavigate();

  const dispatch = useDispatch();
  const { isFetching, isError } = useSelector(userSelector);
  useEffect(() => {
    dispatch(fetchUserBytoken({ token: localStorage.getItem('token') }));
  }, []);

  const { username, email } = useSelector(userSelector);

  useEffect(() => {
    if (isError) {
      dispatch(clearState());
      navigate.push('/login');
    }
  }, [isError]);

  const onLogOut = () => {
    localStorage.removeItem('token');

    navigate.push('/login');
  };
  return <Outlet />;
  // return (
  //   <div className="container mx-auto">
  //     {isFetching ? (
  //       <Rings type="Puff" color="#00BFFF" height={100} width={100} />
  //     ) : (
  //       <Outlet>
  //         <div className="container mx-auto">
  //           Welcome back <h3>{username}</h3>
  //         </div>

  //         <button onClick={onLogOut} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
  //           Log Out
  //         </button>
  //       </Outlet>
  //     )}
  //   </div>
  // );
};

export default Dashboard;
