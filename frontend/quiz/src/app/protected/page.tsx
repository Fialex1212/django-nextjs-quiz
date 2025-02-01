// app/protected/page.tsx
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';

export default async function ProtectedPage() {
  // Получаем cookies
  const cookieStore = cookies();
  const token = cookieStore.get('token')?.value;

  if (!token) {
    redirect('/login');
  }

  // Проверка токена через API-роут
  const response = await fetch('http://localhost:3000/api/auth/verify', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ token }),
  });

  if (!response.ok) {
    redirect('/login');
  }

  const user = await response.json();

  return (
    <div>
      <h1>Protected Page</h1>
      <p>Welcome, user!</p>
    </div>
  );
}