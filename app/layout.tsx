export const metadata = {
  metadataBase: new URL("https://telemetr-a-frontend.vercel.app"),
  title: {
    default: "Telemetr‑A",
    template: "%s | Telemetr‑A",
  },
  description:
    "Plataforma avanzada de telemetría, análisis y visualización de datos en tiempo real.",

  openGraph: {
    type: "website",
    locale: "es_MX",
    url: "https://telemetr-a-frontend.vercel.app/",
    siteName: "Telemetr‑A",
    title: "Telemetr‑A",
    description:
      "Plataforma avanzada de telemetría, análisis y visualización de datos en tiempo real.",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Telemetr‑A — Vista previa",
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: "Telemetr‑A",
    description:
      "Plataforma avanzada de telemetría, análisis y visualización de datos en tiempo real.",
    images: ["/og-image.jpg"],
    creator: "@telemetra",
  },

  icons: {
    icon: "/favicon.ico",
    apple: "/apple-touch-icon.png",
  },
};
