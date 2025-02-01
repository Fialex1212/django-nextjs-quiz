import axios from 'axios';
import useAuthStore from '../stores/useAuthStore';

export const checkAuth = async () => {
  const { token, login, logout } = useAuthStore.getState();

  if (!token) {
    logout();
    return false;
  }

  try {
    const response = await axios.post('/api/auth/verify/', { token });
    if (response.data.user) {
      login(response.data.user, token);
      return true;
    } else {
      logout();
      return false;
    }
  } catch (error) {
    logout();
    return false;
  }
};