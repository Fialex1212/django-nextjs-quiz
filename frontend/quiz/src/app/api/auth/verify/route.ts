import { NextResponse } from 'next/server';
import axios from 'axios';

export async function POST(request) {
  const { token } = await request.json();

  try {
    const response = await axios.get('http://localhost:8000/api/auth/verify/', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return NextResponse.json(response.data);
  } catch (error) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }
}