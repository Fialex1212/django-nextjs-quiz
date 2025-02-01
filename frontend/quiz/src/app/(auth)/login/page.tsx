"use client";

import { useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";
import useAuthStore from "@/stores/useAuthStore";
import { setCookie } from 'cookies-next'; // Используем cookies-next для работы с cookies

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();
  const { login } = useAuthStore();

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log(email, password);
    
    try {
      const response = await axios.post(
        "http://localhost:8000/api/token/",
        {
          email,
          password,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.data.access) {
        // Сохраняем токен в cookies
        setCookie('token', response.data.access, { maxAge: 60 * 60 * 24 }); // Токен на 1 день
        login(response.data.user, response.data.access);
        router.push("/protected");
      }
    } catch (error) {
      console.error("Login failed", error.response?.data || error.message);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}