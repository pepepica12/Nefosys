import fetch from "node-fetch";

const RAILWAY_URL = process.env.RAILWAY_URL || "";

export async function callRailway(path: string, body: any = {}) {
  try {
    const response = await fetch(`${RAILWAY_URL}${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    return await response.json();
  } catch (error) {
    return {
      error: true,
      message: "Error conectando a Railway",
      details: String(error)
    };
  }
}
