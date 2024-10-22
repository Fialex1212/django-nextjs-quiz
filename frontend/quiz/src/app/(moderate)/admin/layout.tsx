import React from "react";

const AdminLayout = ({ children }) => {
  return (
    <>
      <div>admin header</div>
      {children}
    </>
  );
};

export default AdminLayout;