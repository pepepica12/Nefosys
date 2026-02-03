import fetch from "node-fetch";

const TELEMETRY_URL = process.env.TELEMETRY_URL || "";

export async function checkTelemetry() {
  if (!TELEMETRY_URL) {
    return {
      alive: false,
      error: "TELEMETRY_URL no está definida"
    };
  }

  try {
    const response = await fetch(`${TELEMETRY_URL}/api/event`);
    const data = await response.text();

    return {
      alive: true,
      response: data
    };
  } catch (error) {
    return {
      alive: false,
      error: String(error)
    };
  }
}
