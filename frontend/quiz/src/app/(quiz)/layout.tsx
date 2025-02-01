export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <>
      <div>Header</div>
      {children}
      <div>Footer</div>
    </>
  );
}
