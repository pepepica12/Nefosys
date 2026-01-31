export const metadata = {
  metadataBase: new URL("https://telemetr-a-frontend.vercel.app"),
  title: {
    default: "Telemetr‑A",
    template: "%s | Telemetr‑A",
  },
  description:
    "Telemetr‑A: Plataforma avanzada de telemetría, análisis y visualización de datos en tiempo real.",
  keywords: [
    "telemetría",
    "analítica",
    "visualización",
    "datos",
    "dashboard",
    "Nefosys",
    "Railway",
    "Next.js",
  ],
  authors: [{ name: "Telemetr‑A" }],
  creator: "Telemetr‑A",
  publisher: "Telemetr‑A",

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
        url: "/og-image.png",
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
    images: ["/og-image.png"],
    creator: "@telemetra",
  },

  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon.ico",
    apple: "/apple-touch-icon.png",
  },

  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      noimageindex: false,
      "max-image-preview": "large",
    },
  },

  alternates: {
    canonical: "https://telemetr-a-frontend.vercel.app/",
  },
};
